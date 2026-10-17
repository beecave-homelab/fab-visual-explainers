#!/bin/bash
# Install contributor dependencies without changing the lockfile.
# Author: elvee
# Version: 0.1.0
# License: MIT
# Created: 17/10/2026
set -euo pipefail

show_help() {
  cat <<'HELP'
Usage: ./install-dependencies.sh [OPTIONS]

Sync the development environment from uv.lock and install Playwright Chromium.
Run from any directory. Requires Bash, macOS or Linux, and internet access.

Options:
  --install-uv        Install uv if missing, using Astral's HTTPS installer.
                     Uses UV_INSTALL_DIR or ~/.local/bin; no shell profile edits.
  --with-system-deps  Also install Chromium's Linux system packages.
                     Playwright may require root or sudo. For Debian/Ubuntu images.
  --skip-browser      Install Python dependencies only.
  -h, --help          Show help without installing anything.

Examples:
  ./install-dependencies.sh
  ./install-dependencies.sh --install-uv --with-system-deps
HELP
}

error_exit() {
  printf 'Error: %s\n' "$*" >&2
  exit 1
}

# Only a temporary downloaded installer is removed by the EXIT trap.
cleanup() {
  if [[ -n "${installer_file:-}" ]]; then
    rm -f -- "${installer_file}"
  fi
}

main() {
  local install_uv=0 system_deps=0 skip_browser=0
  local repo_root platform uv_bin uv_dir
  while [[ $# -gt 0 ]]; do
    case "$1" in
      --install-uv) install_uv=1 ;;
      --with-system-deps) system_deps=1 ;;
      --skip-browser) skip_browser=1 ;;
      -h|--help) show_help; return 0 ;;
      *) error_exit "Unknown option: $1. Use --help." ;;
    esac
    shift
  done

  platform="$(uname -s)"
  case "${platform}" in
    Darwin|Linux) ;;
    *) error_exit 'Supported platforms: macOS and Linux. Use WSL on Windows.' ;;
  esac
  if [[ "${system_deps}" == 1 ]]; then
    [[ "${platform}" == Linux ]] ||
      error_exit '--with-system-deps requires Linux.'
    [[ "${skip_browser}" == 0 ]] ||
      error_exit '--with-system-deps cannot be combined with --skip-browser.'
  fi

  repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
  cd -- "${repo_root}"
  [[ -f pyproject.toml && -f uv.lock ]] ||
    error_exit 'Keep this script beside pyproject.toml and uv.lock.'

  uv_dir="${UV_INSTALL_DIR:-${HOME}/.local/bin}"
  if command -v uv >/dev/null 2>&1; then
    uv_bin="$(command -v uv)"
  elif [[ -x "${uv_dir}/uv" ]]; then
    uv_bin="${uv_dir}/uv"
  elif [[ "${install_uv}" == 1 ]]; then
    command -v curl >/dev/null 2>&1 ||
      error_exit 'Install curl before using --install-uv.'
    installer_file="$(mktemp)"
    trap cleanup EXIT
    curl --fail --silent --show-error --location \
      --proto '=https' --proto-redir '=https' \
      https://astral.sh/uv/install.sh --output "${installer_file}"
    UV_INSTALL_DIR="${uv_dir}" UV_NO_MODIFY_PATH=1 sh "${installer_file}"
    uv_bin="${uv_dir}/uv"
    [[ -x "${uv_bin}" ]] || error_exit 'The uv installer did not provide uv.'
  else
    error_exit 'uv is missing. Install it or rerun with --install-uv.'
  fi

  # Keep the environment in this checkout even inside an activated environment.
  export UV_PROJECT_ENVIRONMENT="${repo_root}/.venv"
  "${uv_bin}" sync --locked --group dev
  if [[ "${skip_browser}" == 0 ]]; then
    local browser_args=(install chromium --only-shell)
    if [[ "${system_deps}" == 1 ]]; then
      browser_args+=(--with-deps)
    fi
    "${uv_bin}" run --locked --no-sync playwright "${browser_args[@]}"
  fi
  printf 'Dependencies installed in %s/.venv\n' "${repo_root}"
}

main "$@"
