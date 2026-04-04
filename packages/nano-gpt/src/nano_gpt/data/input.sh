#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INPUT_FILE="${SCRIPT_DIR}/input.txt"
URL="https://raw.githubusercontent.com/karpathy/ng-video-lecture/refs/heads/master/input.txt"

if [ ! -f "$INPUT_FILE" ]; then
  echo "input.txt not found, downloading..."
  curl -fsSL "$URL" -o "$INPUT_FILE"
  echo "Downloaded input.txt"
fi
