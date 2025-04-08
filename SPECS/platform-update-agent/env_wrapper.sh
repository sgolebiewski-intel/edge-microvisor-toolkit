#!/usr/bin/bash

set -eu

EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
UPDATED_EDGE_NODE_UUID=$(sed -e "s/^GUID: '.*'/GUID: ${EDGE_NODE_UUID}/" /etc/edge-node/node/confs/platform-update-agent.yaml)
echo -E "${UPDATED_EDGE_NODE_UUID}" > /etc/edge-node/node/confs/platform-update-agent.yaml

if [ ! -z "$UPDATE_SERVICE_URL" ]; then
    UPDATED_UPDATE_SERVICE_URL=$(sed -e "s/^updateServiceURL: '.*'/updateServiceURL: '${UPDATE_SERVICE_URL}'/" /etc/edge-node/node/confs/platform-update-agent.yaml)
    echo -E "${UPDATED_UPDATE_SERVICE_URL}" > /etc/edge-node/node/confs/platform-update-agent.yaml
fi

if [ ! -z "$CADDY_APT_PROXY_URL" ]; then
    UPDATED_CADDY_APT_PROXY_URL=$(sed -e "s|^releaseServiceFQDN: '.*'|releaseServiceFQDN: 'https://${CADDY_APT_PROXY_URL}'|" /etc/edge-node/node/confs/platform-update-agent.yaml)
    echo -E "${UPDATED_CADDY_APT_PROXY_URL}" > /etc/edge-node/node/confs/platform-update-agent.yaml
fi

exec "$@"
