#!/bin/bash
set -eu

# Define the IMG_REGISTRY_PORT variable
IMG_REGISTRY_PORT=""

# Check if CADDY_REGISTRY_PROXY_PORT is set and assign it to IMG_REGISTRY_PORT
# If not set, exit the script cleanly
if [ -n "${CADDY_REGISTRY_PROXY_PORT:-}" ]; then
    IMG_REGISTRY_PORT=$CADDY_REGISTRY_PROXY_PORT
else
    exit 0
fi

check_connectivity() {
    # Loop to check if connectivity to Release Service can be established via caddy
    curl --retry 3 --retry-delay 3 --retry-all-errors -f "https://localhost.internal:${IMG_REGISTRY_PORT}/healthz"
}

check_connectivity
