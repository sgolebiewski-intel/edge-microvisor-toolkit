#!/bin/bash

set -eu

update_uuid() {
	local EDGE_NODE_UUID
	local UPDATED_CLUSTER_AGENT_UUID

	EDGE_NODE_UUID="$(sudo dmidecode -s system-uuid)"
	UPDATED_CLUSTER_AGENT_UUID=$(sed "s/^GUID: '.*'/GUID: '${EDGE_NODE_UUID}'/" /etc/edge-node/node/confs/cluster-agent.yaml)
	echo -E "${UPDATED_CLUSTER_AGENT_UUID}" > /etc/edge-node/node/confs/cluster-agent.yaml
}

update_orch_url() {
	if [ -n "$CLUSTER_ORCH_URL" ]; then
		local UPDATED_CLUSTER_AGENT_ORCH_URL
		UPDATED_CLUSTER_AGENT_ORCH_URL=$(sed "s/^clusterOrchestratorURL: '.*'/clusterOrchestratorURL: '$CLUSTER_ORCH_URL'/" /etc/edge-node/node/confs/cluster-agent.yaml)
		echo -E "${UPDATED_CLUSTER_AGENT_ORCH_URL}" > /etc/edge-node/node/confs/cluster-agent.yaml
	fi
}

update_uuid
update_orch_url

exec "$@"
