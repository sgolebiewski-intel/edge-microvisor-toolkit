#!/bin/bash

check() {
    return 0
}
depends() {
    echo "dm rootfs-block crypt"
    return 0
}
install() {
    inst_hook pre-mount 00 "$moddir/tpm-cryptsetup.sh"
    inst_simple "$moddir/tpm-cryptsetup.sh" "/etc/tpm-cryptsetup.sh"
    inst /usr/bin/tpm2-initramfs-tool
    inst_simple "$moddir/tpm-cryptsetup.sh" "/luks_key"

    inst /usr/sbin/cryptsetup

    inst /usr/sbin/veritysetup
    inst /usr/bin/lsblk
    inst /usr/sbin/blkid
    inst /usr/sbin/dmsetup
    inst /usr/sbin/blockdev
    inst /usr/sbin/partx

    inst_simple "$moddir/systemd-cryptsetup@root.service" "$systemdsystemunitdir/systemd-cryptsetup@root.service"
    $SYSTEMCTL -q --root "$initdir" add-wants initrd.target "systemd-cryptsetup@root.service"
}
