#!/bin/bash

set -eu

update_infra_url() {
	if [ -n "$HW_INVENTORY_URL" ]; then
		local UPDATED_HW_DISCOVERY_INFRA_URL
		UPDATED_HW_DISCOVERY_INFRA_URL=$(sed "s/^  serviceURL: '.*'/  serviceURL: '$HW_INVENTORY_URL'/" /etc/edge-node/node/confs/hd-agent.yaml)
		echo -E "${UPDATED_HW_DISCOVERY_INFRA_URL}" > /etc/edge-node/node/confs/hd-agent.yaml
	fi
}

update_infra_url

exec "$@"
