#!/bin/bash

set -e

echo "=== WEB ENTRYPOINT ==="

echo "=== BUNDLING ==="
COMMAND="$1"

case "$COMMAND" in
  server)
    echo "=== RUNNING SERVER ON PORT 3000 ==="
    /opt/conda/bin/jupyter notebook --notebook-dir=/app --ip='*' --port=8888 --no-browser --allow-root
    ;;
  *)
    echo "=== RUNNING COMAND -> $* ==="
    sh -c "$*"
    ;;
esac
