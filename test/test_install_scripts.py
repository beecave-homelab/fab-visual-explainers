"""Installercontracten zonder downloads, systeemwijzigingen of echte browsers."""

import shutil
import subprocess
from pathlib import Path

import pytest
from support import ROOT


@pytest.fixture
def setup_checkout(tmp_path: Path) -> tuple[Path, dict[str, str], Path]:
    """Isoleer checkout, HOME en PATH; registreer externe opdrachten."""
    checkout = tmp_path / "checkout with spaces"
    checkout.mkdir()
    for name in ("install.sh", "install-dependencies.sh", "pyproject.toml", "uv.lock"):
        shutil.copy2(ROOT / name, checkout / name)
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    for command in ("bash", "cat", "dirname", "mkdir", "mktemp", "rm", "sh"):
        target = shutil.which(command)
        assert target
        (bin_dir / command).symlink_to(target)
    home_dir = tmp_path / "home"
    home_dir.mkdir()
    log = tmp_path / "commands.log"
    env = {
        "PATH": str(bin_dir),
        "HOME": str(home_dir),
        "COMMAND_LOG": str(log),
        "TMPDIR": str(tmp_path),
    }
    (bin_dir / "uname").write_text('#!/bin/bash\nprintf "%s\\n" "${TEST_PLATFORM:-Linux}"\n')
    (bin_dir / "uname").chmod(0o755)
    uv_stub = bin_dir / "uv"
    uv_stub.write_text(
        "#!/bin/bash\nset -eu\n"
        'printf "uv %s cwd=%s env=%s\\n" "$*" "$PWD" '
        '"$UV_PROJECT_ENVIRONMENT" >> "$COMMAND_LOG"\n'
        'if [[ "${FAIL_STAGE:-}" == "$1" ]]; then exit 23; fi\n'
    )
    # The real installer invokes Python directly; make the mock executable up front.
    python_stub = checkout / ".venv/bin/python"
    python_stub.parent.mkdir(parents=True)
    python_stub.write_text(
        '#!/bin/bash\nprintf "python verified\\n" >> "$COMMAND_LOG"\n'
        'if [[ "$1" != -c ]]; then\n'
        "  cat >/dev/null\n"
        '  if [[ "${FAIL_BROWSER:-0}" == 1 ]]; then exit 19; fi\n'
        "fi\n"
        'exit "${FAIL_PYTHON:-0}"\n'
    )
    python_stub.chmod(0o755)
    uv_stub.chmod(0o755)
    return checkout, env, log


def run_setup(
    setup: tuple[Path, dict[str, str], Path], script: str, *args: str
) -> subprocess.CompletedProcess[str]:
    """Voer uit buiten de checkout, met een begrensde looptijd."""
    checkout, env, _ = setup
    return subprocess.run(
        ["/bin/bash", str(checkout / script), *args],
        cwd=checkout.parent,
        env=env,
        capture_output=True,
        text=True,
        timeout=10,
    )


@pytest.mark.parametrize("script", ["install.sh", "install-dependencies.sh"])
def test_setup__help_and_invalid_flags_do_not_install(
    setup_checkout: tuple[Path, dict[str, str], Path], script: str
) -> None:
    """Help blijft zonder side effects; typefouten falen vóór installatie."""
    _, _, log = setup_checkout
    assert run_setup(setup_checkout, script, "--help").returncode == 0
    invalid = run_setup(setup_checkout, script, "--typo")
    assert invalid.returncode != 0
    assert "Unknown option" in invalid.stderr
    assert not log.exists()


def test_setup__uses_lockfile_checkout_and_managed_browser(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Een pad met spaties werkt en selecteert uitsluitend Playwright Chromium."""
    checkout, _, log = setup_checkout
    result = run_setup(setup_checkout, "install.sh")
    assert result.returncode == 0, result.stderr
    commands = log.read_text()
    assert "uv sync --locked --group dev" in commands
    assert f"cwd={checkout} env={checkout}/.venv" in commands
    assert "run --locked --no-sync playwright install chromium --only-shell" in commands
    assert commands.count("python verified") == 2
    assert "--browser-channel chromium" in result.stdout
    assert "Setup complete" in result.stdout


def test_setup__skip_browser_does_not_claim_browser_readiness(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Een Python-only installatie slaat browserdownload en browsercheck over."""
    _, _, log = setup_checkout
    result = run_setup(setup_checkout, "install.sh", "--skip-browser")
    assert result.returncode == 0, result.stderr
    commands = log.read_text()
    assert "playwright install" not in commands
    assert commands.count("python verified") == 1
    assert "--browser-channel chromium" not in result.stdout
    assert "skipped" in result.stdout


@pytest.mark.parametrize("stage", ["sync", "run"])
def test_setup__dependency_failure_stops_verification(
    setup_checkout: tuple[Path, dict[str, str], Path], stage: str
) -> None:
    """Een mislukte sync of browserinstallatie krijgt geen succesmelding."""
    _, env, log = setup_checkout
    env["FAIL_STAGE"] = stage
    result = run_setup(setup_checkout, "install.sh")
    assert result.returncode != 0
    assert "Setup complete" not in result.stdout
    assert "python verified" not in log.read_text()


def test_setup__python_failure_stops_success_message(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Een mislukte verificatie mag geen geslaagde setup suggereren."""
    _, env, _ = setup_checkout
    env["FAIL_PYTHON"] = "17"
    result = run_setup(setup_checkout, "install.sh")
    assert result.returncode != 0
    assert "Setup complete" not in result.stdout


def test_setup__system_packages_require_explicit_linux_option(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Alleen de Linux-optie vraagt Playwright om systeempakketten."""
    _, _, log = setup_checkout
    result = run_setup(setup_checkout, "install-dependencies.sh", "--with-system-deps")
    assert result.returncode == 0, result.stderr
    assert "--with-deps" in log.read_text()


def test_setup__browser_start_failure_stays_a_failure(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Een geinstalleerde browser kan nog falen door systeemeisen of sandboxregels."""
    _, env, _ = setup_checkout
    env["FAIL_BROWSER"] = "1"
    result = run_setup(setup_checkout, "install.sh")
    assert result.returncode != 0
    assert "Chromium verification failed" in result.stderr
    assert "Setup complete" not in result.stdout


@pytest.mark.parametrize(
    ("platform", "flags"),
    [
        ("Darwin", ["--with-system-deps"]),
        ("Linux", ["--with-system-deps", "--skip-browser"]),
        ("Unsupported", []),
    ],
)
def test_setup__invalid_platform_or_combination_is_rejected_before_install(
    setup_checkout: tuple[Path, dict[str, str], Path], platform: str, flags: list[str]
) -> None:
    """Ongeldige omgevingen falen zonder gedeeltelijke installatie."""
    _, env, log = setup_checkout
    env["TEST_PLATFORM"] = platform
    result = run_setup(setup_checkout, "install.sh", *flags)
    assert result.returncode != 0
    assert not log.exists()


def test_setup__missing_uv_does_not_download_without_opt_in(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Ontbrekend uv vraagt om een expliciete installatieoptie."""
    _, env, log = setup_checkout
    (Path(env["PATH"]) / "uv").unlink()
    result = run_setup(setup_checkout, "install.sh")
    assert result.returncode != 0
    assert "--install-uv" in result.stderr
    assert not log.exists()


def test_setup__existing_uv_outside_path_is_reused(
    setup_checkout: tuple[Path, dict[str, str], Path],
) -> None:
    """Een eerdere bootstrap blijft bruikbaar zonder shellprofielwijziging."""
    _, env, log = setup_checkout
    install_dir = Path(env["HOME"]) / ".local/bin"
    install_dir.mkdir(parents=True)
    (Path(env["PATH"]) / "uv").rename(install_dir / "uv")
    result = run_setup(setup_checkout, "install-dependencies.sh", "--skip-browser")
    assert result.returncode == 0, result.stderr
    assert "uv sync" in log.read_text()


@pytest.mark.parametrize("download_failure", [False, True])
def test_setup__uv_bootstrap_uses_https_and_cleans_download(
    setup_checkout: tuple[Path, dict[str, str], Path], download_failure: bool
) -> None:
    """Bootstrap is expliciet, wijzigt geen profiel en ruimt ook na fouten op."""
    _, env, log = setup_checkout
    bin_dir = Path(env["PATH"])
    seed = bin_dir / "uv-seed"
    (bin_dir / "uv").rename(seed)
    env["UV_SEED"] = str(seed)
    env["CURL_FAIL"] = "1" if download_failure else "0"
    curl_stub = bin_dir / "curl"
    curl_stub.write_text(
        '#!/bin/bash\nset -eu\nprintf "curl %s\\n" "$*" >> "$COMMAND_LOG"\n'
        'while [[ "$1" != --output ]]; do shift; done\n'
        'printf "%s" "$2" > "$HOME/download-path"\n'
        'if [[ "$CURL_FAIL" == 1 ]]; then exit 22; fi\n'
        "cat > \"$2\" <<'INSTALLER'\n"
        "#!/bin/sh\nset -eu\n"
        '[ "$UV_NO_MODIFY_PATH" = 1 ]\n'
        'mkdir -p "$UV_INSTALL_DIR"\n'
        'cat "$UV_SEED" > "$UV_INSTALL_DIR/uv"\n'
        'chmod +x "$UV_INSTALL_DIR/uv"\n'
        "INSTALLER\n"
    )
    curl_stub.chmod(0o755)
    chmod = shutil.which("chmod")
    assert chmod
    (bin_dir / "chmod").symlink_to(chmod)
    result = run_setup(setup_checkout, "install.sh", "--install-uv", "--skip-browser")
    assert (result.returncode != 0) == download_failure, result.stderr
    commands = log.read_text()
    assert "--proto =https --proto-redir =https https://astral.sh/uv/install.sh" in commands
    download_path = Path((Path(env["HOME"]) / "download-path").read_text())
    assert not download_path.exists()
    assert ("uv sync" in commands) != download_failure
    assert ("Setup complete" in result.stdout) != download_failure
    assert not (Path(env["HOME"]) / ".profile").exists()
