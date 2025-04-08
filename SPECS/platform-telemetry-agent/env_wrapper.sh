#!/usr/bin/bash

set -eu

EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
UPDATED_EDGE_NODE_UUID=$(sed -e "s/nodeid: aaaaaaaa-0000-1111-2222-bbbbbbbbcccc/nodeid: ${EDGE_NODE_UUID}/" /etc/edge-node/node/confs/platform-telemetry-agent.yaml)
echo -E "${UPDATED_EDGE_NODE_UUID}" > /etc/edge-node/node/confs/platform-telemetry-agent.yaml

if [ ! -z "$TELEMETRY_MANAGER_URL" ]; then
    # Extract host and port from TELEMETRY_MANAGER_URL
    extracted_host=$(echo "$TELEMETRY_MANAGER_URL" | cut -d: -f1)
    extracted_port=$(echo "$TELEMETRY_MANAGER_URL" | cut -d: -f2)

    # Update address in platform-telemetry-agent.yaml
    updated_address=$(sed -e "s/address: localhost/address: ${extracted_host}/" /etc/edge-node/node/confs/platform-telemetry-agent.yaml)
    echo -E "$updated_address" > /etc/edge-node/node/confs/platform-telemetry-agent.yaml

    # Update port in platform-telemetry-agent.yaml
    updated_port=$(sed -e "s/port: 5000/port: ${extracted_port}/" /etc/edge-node/node/confs/platform-telemetry-agent.yaml)
    echo -E "$updated_port" > /etc/edge-node/node/confs/platform-telemetry-agent.yaml
fi

exec "$@"
