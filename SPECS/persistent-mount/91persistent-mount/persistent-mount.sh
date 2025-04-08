#!/bin/bash
#
# Reference: https://github.com/kairos-io/
# ../dracut/immutable-rootfs/30cos-immutable-rootfs/cos-mount-layout.sh

function mountOverlayBase {
	echo "Creating ${overlay_base}"
	mkdir -p "/sysroot/${overlay_base}"
	if [ "${overlay%%:*}" = "tmpfs" ]; then
		overlay_size="${overlay#*:}"
		echo "overlay_size = $overlay_size"
		mount -t tmpfs -o "defaults,size=${overlay_size}" tmpfs "/sysroot/${overlay_base}"
	fi
}

function readLayoutConfig {
	if [ -n "${OVERLAY}" ]; then
		overlay=${OVERLAY}
	fi

	state_paths=()
	state_target="${PERSISTENT_BIND_TARGET:-/opt/.mount/persistent}"
	overlay_base="${TMPFS_OVERLAY_TARGET:-/opt/.mount/tmpfs}"

	# An empty TMPFS_OVERLAYS_PATHS is a valid value, default rw_tmpfs_paths are only
	# applied when TMPFS_OVERLAYS_PATHS is unset.
	if [ -n "${TMPFS_OVERLAYS_PATHS+x}" ]; then
		rw_tmpfs_paths=${TMPFS_OVERLAYS_PATHS}
	fi
	if [ -n "${PERSISTENT_BIND_PATHS}" ]; then
		state_paths=${PERSISTENT_BIND_PATHS}
	fi
	persist_partition_mountpoint=$(echo "$state_target" | cut -d "/" -f2)
}

function preserveDirAttributes {
	local src=$1
	local srcdir=$2
	local destdir=$3
	chown --reference=$srcdir/$src $destdir/$src
	chmod --reference=$srcdir/$src $destdir/$src
	cd "${srcdir}"
	getfacl $src > /tmp/${src}.acl
	cd "${destdir}"
	setfacl --restore /tmp/${src}.acl
	rm -rf /tmp/${src}.acl
}

function mountOverlay {
	local mount=$1
	local base="${overlay_base}"
	local merged
	local upperdir
	local workdir
	local targetdir="$(basename $mount)"
	local targetdirpath="/sysroot$(dirname $mount)"

	mount="${mount#/}"
	merged="/sysroot/${mount}"
	base="/sysroot${base}"
	if ! mountpoint -q "${merged}"; then
		if [ -d "${merged}" ]; then
			echo "mountOverlay, merged= $merged"
			upperdir="${base}/${mount//\//-}.overlay/$targetdir"
			workdir="${base}/${mount//\//-}.overlay/work"
			mkdir -p "${upperdir}" "${workdir}"
			upperdirpath="$(dirname $upperdir)"
			preserveDirAttributes $targetdir $targetdirpath $upperdirpath
			mount -t overlay overlay -o "defaults,lowerdir=${merged},upperdir=${upperdir},workdir=${workdir}" "${merged}"
		else
			echo "${base} does not exists !"
		fi
	fi
}

function mountBind {
	local mount=$1
	local base
	local state_dir

	mount="${mount#/}"
	base="/sysroot/${mount}"
	state_dir="/sysroot/${state_target}/${mount//\//-}.bind"
	if ! mountpoint -q "${base}"; then
		# Check if it's a single file
		if test -f "${base}"
		then
			mkdir -p "${state_dir}"
			rsync -aqHX --ignore-existing "${base}" "${state_dir}/"
			base_name=$(basename ${base})
			mount --bind "${state_dir}/${base_name}" "${base}"
		elif test -d "${base}"
		then
			mkdir -p "${state_dir}"
			rsync -aqHX --ignore-existing "${base}/" "${state_dir}/"
			mount -o defaults,bind "${state_dir}" "${base}"
		else
			echo "Persistent path ${base} does not exists !"
		fi
	fi
}

function mount_persistent()
{
    echo "Mounting persistent partition at ${NEWROOT}/${persist_partition_mountpoint}/ ..."
    if [ -e /dev/mapper/edge_persistent ];
    then
	mount -t ext4 -o rw /dev/mapper/edge_persistent "${NEWROOT}"/"${persist_partition_mountpoint}"/ || \
	    die "Failed to mount ${NEWROOT}/${persist_partition_mountpoint}/ partition"
    else
	mount -t ext4 -o rw /dev/disk/by-partlabel/edge_persistent "${NEWROOT}"/"${persist_partition_mountpoint}"/ || \
	    die "Failed to mount ${NEWROOT}/${persist_partition_mountpoint}/ partition"
    fi
}


PATH=/usr/sbin:/usr/bin:/sbin:/bin
declare overlay_base="/srv/local"
declare overlay="tmpfs:25%"
declare rw_tmpfs_paths=("/var")
declare layout="/etc/layout.env"
declare persist_partition_mountpoint="/opt"
declare state_paths
declare state_target

# Source & read layer.env
. "${NEWROOT}"/etc/layout.env

readLayoutConfig

echo "rw_tmpfs_paths = $rw_tmpfs_paths"
echo "overlay = $overlay"
echo "state_paths = $state_paths"
echo "state_target = $state_target"
echo "overlay_base = $overlay_base"
echo "persist_partition_mountpoint = $persist_partition_mountpoint"

# Mount persistent partition
mount_persistent

# Create tmpfs overlay
mountOverlayBase

# Mount overlay on top of tmpfs for TMPFS_OVERLAYS_PATHS
for path in $rw_tmpfs_paths
do
	mountOverlay $path
done

# rsync file/directory and bind mount for PERSISTENT_BIND_PATHS
for path in $state_paths
do
	mountBind $path
done
