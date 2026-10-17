#!/bin/bash
# Set up and verify the contributor environment.
# Author: elvee
# Version: 0.1.0
# License: MIT
# Created: 17/10/2026
set -euo pipefail

main() {
  local repo_root skip_browser=0 option
  repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
  for option in "$@"; do
    case "${option}" in
      -h|--help)
        printf '%s\n' 'Usage: ./install.sh [OPTIONS]' \
          'Install dependencies, verify tools and launch headless Chromium.' \
          'Options are shared with install-dependencies.sh:'
        bash "${repo_root}/install-dependencies.sh" --help
        return 0
        ;;
      --skip-browser) skip_browser=1 ;;
    esac
  done

  bash "${repo_root}/install-dependencies.sh" "$@"
  cd -- "${repo_root}"
  .venv/bin/python -c \
    'import pytest, playwright.sync_api, ruff, mdformat, djlint; print("Python tools verified")'
  if [[ "${skip_browser}" == 0 ]]; then
    if ! .venv/bin/python - <<'PY'
from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    with playwright.chromium.launch(headless=True) as browser:
        page = browser.new_page()
        page.set_content("<h1>FAB setup</h1>")
        assert page.locator("h1").inner_text() == "FAB setup"
        print(f"Playwright Chromium verified: {browser.version}")
PY
    then
      printf '%s\n' \
        'Chromium verification failed. Check system libraries and sandbox policy.' \
        'On Debian/Ubuntu, retry with --with-system-deps if packages are missing.' >&2
      return 1
    fi
  fi
  printf '%s\n' 'Setup complete. Run checks from the repository root:'
  if [[ "${skip_browser}" == 0 ]]; then
    printf '%s\n' '  .venv/bin/pytest --browser-channel chromium'
  else
    printf '%s\n' \
      'Browser installation and verification skipped.' \
      'Rerun ./install.sh before running browser tests.'
  fi
  printf '%s\n' 'See docs/installatie.md for setup options.'
}

main "$@"
