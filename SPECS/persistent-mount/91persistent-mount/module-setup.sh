#!/bin/bash

check() {
    return 0
}

depends() {
    return 0
}

install() {
    inst_multiple \
	mount mountpoint rsync basename cut dirname getfacl setfacl

    inst_hook pre-pivot 91 "$moddir/persistent-mount.sh"
}
