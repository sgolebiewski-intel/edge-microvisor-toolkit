%define dracutlibdir        %{_libdir}/%{name}
%global __requires_exclude  pkg-config

Summary:        dracut to create initramfs
Name:           dracut
Version:        102
Release:        13%{?dist}
# The entire source code is GPLv2+
# except install/* which is LGPLv2+
License:        GPLv2+ AND LGPLv2+
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://github.com/dracut-ng/dracut-ng/wiki

Source0:        https://github.com/dracut-ng/dracut-ng/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://www.gnu.org/licenses/lgpl-2.1.txt
Source3:        megaraid.conf
Source4:        20overlayfs/module-setup.sh
Source5:        20overlayfs/overlayfs-mount.sh
Source6:        00-hostonly.conf
Source7:        00-hyperv.conf
Source8:        00-virtio.conf
Source9:        00-vrf.conf
Source10:       00-xen.conf
Source11:       50-noxattr.conf
# The 90livenet/azl-liveos-artifacts-download.service and 
# 90livenet/azl-liveos-artifacts-download.sh are part of the 
# add-livenet-download-service.patch. They are kept separate for easier
# code reviews given that they are new to Dracut.
Source12:       90livenet/azl-liveos-artifacts-download.service
Source13:       90livenet/azl-liveos-artifacts-download.sh
Source14:       90overlayfs/azl-configure-selinux.sh
Source15:       90tmpfsroot/tmpfsroot-module-setup.sh
Source16:       90tmpfsroot/tmpfsroot-mount.sh

# allow-liveos-overlay-no-user-confirmation-prompt.patch has been introduced by
# the Azure Linux team to allow skipping the user confirmation prompt during
# boot when the overlay of the liveos is backed by ram. This allows the machine
# to boot without being blocked on user input in such a scenario.
Patch:          allow-liveos-overlay-no-user-confirmation-prompt.patch
# add-livenet-download-service.patch has been introduced by the Azure Linux
# team to enable Dracut's livenet module to download and ISO image and proceed
# with a rootfs overlay mouting/pivoting (using Dracut's existing dmsquash-live
# module). This enables PXE booting using an ISO image with an embededed rootfs
# image.
# This is a temporary fix until Dracut is upgraded to 103.
# - For reference, see https://github.com/dracut-ng/dracut-ng/issues/719.
# This patch relies on two new files (azl-liveos-artifacts-download.service and 
# azl-liveos-artifacts-download.sh) - which are included as separate sources in
# this package.
Patch:          add-livenet-download-service.patch
Patch:          0006-dracut.sh-validate-instmods-calls.patch
Patch:          0011-Remove-reference-to-kernel-module-zlib-in-fips-module.patch
Patch:          0012-fix-dracut-functions-avoid-awk-in-get_maj_min.patch
Patch:          0013-revert-fix-crypt-unlock-encrypted-devices-by-default.patch
Patch:          0014-fix-systemd-pcrphase-in-hostonly-mode-do-not-try-to-include-systemd-pcrphase.patch
Patch:          0015-fix-systemd-pcrphase-make-tpm2-tss-an-optional-dependency.patch
Patch:          0016-Handle-SELinux-configuration-for-overlayfs-folders.patch
Patch:          avoid-mktemp-collisions-with-find-not-path.patch
# fix-dracut-systemd-include-systemd-cryptsetup.patch has been introduced  
# by the Azure Linux team to ensure that the systemd-cryptsetup module is included  
# in the initramfs when needed.  
# In dracut 102, systemd-cryptsetup was split from the crypt module and is no longer  
# included by default, causing encrypted volumes in crypttab to be skipped in initrd.  
# This patch modifies dracut-systemd to explicitly include systemd-cryptsetup.  
# The patch can be removed if Dracut is upgraded to 104+.
# - References: https://github.com/dracut-ng/dracut-ng/pull/262  
#               https://github.com/dracut-ng/dracut-ng/commit/e0e5424a7b5e387ccb70e47ffea5a59716bf7b76  
Patch:          fix-dracut-systemd-include-systemd-cryptsetup.patch

BuildRequires:  bash
BuildRequires:  kmod-devel
BuildRequires:  pkg-config
BuildRequires:  asciidoc
BuildRequires:  systemd-rpm-macros

Requires:       bash >= 4
Requires:       kmod
Requires:       sed
Requires:       grep
Requires:       xz
Requires:       gzip
Requires:       cpio
Requires:       filesystem
Requires:       util-linux
Requires:       findutils
Requires:       procps-ng
Requires:       systemd
Requires:       systemd-udev
# Our toolkit cannot handle OR requirements
#Requires:       (coreutils or coreutils-selinux)
Requires:       coreutils

%description
dracut contains tools to create a bootable initramfs for 2.6 Linux kernels.
Unlike existing implementations, dracut does hard-code as little as possible
into the initramfs. dracut contains various modules which are driven by the
event-based udev. Having root on MD, DM, LVM2, LUKS is supported as well as
NFS, iSCSI, NBD, FCoE with the dracut-network package.

%package fips
Summary:        dracut modules to build a dracut initramfs with an integrity check
Requires:       %{name} = %{version}-%{release}
Requires:       libkcapi-hmaccalc
Requires:       nss

%description fips
This package requires everything which is needed to build an
initramfs with dracut, which does an integrity check.

%package hostonly
Summary:        dracut configuration needed to build an initramfs with hostonly enabled
Requires:       %{name} = %{version}-%{release}

%description hostonly
This package contains dracut configuration needed to build an initramfs with hostonly enabled

%package hyperv
Summary:        dracut configuration needed to build an initramfs with hyperv guest drivers
Requires:       %{name} = %{version}-%{release}

%description hyperv
This package contains dracut configuration needed to build an initramfs with hyperv guest drivers

%package megaraid
Summary:        dracut configuration needed to build an initramfs with MegaRAID driver support
Requires:       %{name} = %{version}-%{release}

%description megaraid
This package contains dracut configuration needed to build an initramfs with MegaRAID driver support.

%package noxattr
Summary:        dracut configuration needed to disable preserving of xattr file metadata
Requires:       %{name} = %{version}-%{release}

%description noxattr
This package contains dracut configuration needed to disable preserving of xattr file metadata.

%package tools
Summary:        dracut tools to build the local initramfs
Requires:       %{name} = %{version}-%{release}

%description tools
This package contains tools to assemble the local initrd and host configuration.

%package overlayfs
Summary:        dracut module to build a dracut initramfs with OverlayFS support
Requires:       %{name} = %{version}-%{release}

%description overlayfs
This package contains dracut module needed to build an initramfs with OverlayFS support.

%package systemd-cryptsetup
Summary:        dracut module to build a dracut initramfs with systemd-cryptsetup enabled
Requires:       %{name} = %{version}-%{release}

%description systemd-cryptsetup
This package contains dracut module needed to build an initramfs with systemd-cryptsetup enabled.

%package tmpfsroot
Summary:        dracut module to support root on tmpfs
Requires:       %{name} = %{version}-%{release}

%description tmpfsroot
This package contains dracut module root on tmpfs.

%package virtio
Summary:        dracut configuration needed to build an initramfs with virtio guest drivers
Requires:       %{name} = %{version}-%{release}

%description virtio
This package contains dracut configuration needed to build an initramfs with virtio guest drivers

%package vrf
Summary:        dracut configuration needed to build an initramfs with the vrf driver
Requires:       %{name} = %{version}-%{release}

%description vrf
This package contains dracut configuration needed to build an initramfs with the vrf driver

%package xen
Summary:        dracut configuration needed to build an initramfs with xen guest drivers
Requires:       %{name} = %{version}-%{release}

%description xen
This package contains dracut configuration needed to build an initramfs with xen guest drivers

%prep
%autosetup -p1 -n %{name}-ng-%{version}
cp %{SOURCE1} .

%build
%configure \
    --systemdsystemunitdir=%{_unitdir} \
    --bashcompletiondir=$(pkg-config --variable=completionsdir bash-completion) \
    --libdir=%{_libdir} \
    --disable-documentation

%make_build

%install
%make_install %{?_smp_mflags} libdir=%{_libdir}

echo "DRACUT_VERSION=%{version}-%{release}" > %{buildroot}%{dracutlibdir}/%{name}-version.sh


# we do not support dash in the initramfs
rm -fr -- %{buildroot}%{dracutlibdir}/modules.d/00dash

# remove gentoo specific modules
rm -fr -- %{buildroot}%{dracutlibdir}/modules.d/96securityfs \
          %{buildroot}%{dracutlibdir}/modules.d/97masterkey \
          %{buildroot}%{dracutlibdir}/modules.d/98integrity

mkdir -p %{buildroot}/boot/%{name} \
         %{buildroot}%{_sharedstatedir}/%{name}/overlay \
         %{buildroot}%{_var}/log \
         %{buildroot}%{_var}/opt/%{name}/log \
         %{buildroot}%{_sharedstatedir}/initramfs \
         %{buildroot}%{_sbindir}

install -m 0644 dracut.conf.d/fips.conf.example %{buildroot}%{_sysconfdir}/dracut.conf.d/40-fips.conf
> %{buildroot}%{_sysconfdir}/system-fips

install -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/dracut.conf.d/50-megaraid.conf
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/dracut.conf.d/00-hostonly.conf
install -m 0644 %{SOURCE7} %{buildroot}%{_sysconfdir}/dracut.conf.d/00-hyperv.conf
install -m 0644 %{SOURCE8} %{buildroot}%{_sysconfdir}/dracut.conf.d/00-virtio.conf
install -m 0644 %{SOURCE9} %{buildroot}%{_sysconfdir}/dracut.conf.d/00-vrf.conf
install -m 0644 %{SOURCE10} %{buildroot}%{_sysconfdir}/dracut.conf.d/00-xen.conf
install -m 0644 %{SOURCE11} %{buildroot}%{_sysconfdir}/dracut.conf.d/50-noxattr.conf

install -m 0644 %{SOURCE12} %{buildroot}%{dracutlibdir}/modules.d/90livenet/azl-liveos-artifacts-download.service
install -m 0755 %{SOURCE13} %{buildroot}%{dracutlibdir}/modules.d/90livenet/azl-liveos-artifacts-download.sh

install -m 0755 %{SOURCE14} %{buildroot}%{dracutlibdir}/modules.d/90overlayfs/azl-configure-selinux.sh

mkdir -p %{buildroot}%{dracutlibdir}/modules.d/20overlayfs/
install -p -m 0755 %{SOURCE4} %{buildroot}%{dracutlibdir}/modules.d/20overlayfs/
install -p -m 0755 %{SOURCE5} %{buildroot}%{dracutlibdir}/modules.d/20overlayfs/

mkdir -p %{buildroot}%{dracutlibdir}/modules.d/90tmpfsroot/
install -p -m 0755 %{SOURCE15} %{buildroot}%{dracutlibdir}/modules.d/90tmpfsroot/module-setup.sh
install -p -m 0755 %{SOURCE16} %{buildroot}%{dracutlibdir}/modules.d/90tmpfsroot/

touch %{buildroot}%{_var}/opt/%{name}/log/%{name}.log
ln -srv %{buildroot}%{_var}/opt/%{name}/log/%{name}.log %{buildroot}%{_var}/log/

# create compat symlink
ln -srv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}

%files
%defattr(-,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/lsinitrd
# compat symlink
%{_sbindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/bash-completion/completions/lsinitrd
%dir %{dracutlibdir}
%dir %{dracutlibdir}/modules.d
%{dracutlibdir}/modules.d/*
%exclude %{_libdir}/kernel
%exclude %{dracutlibdir}/modules.d/20overlayfs
%exclude %{dracutlibdir}/modules.d/90systemd-cryptsetup
%exclude %{dracutlibdir}/modules.d/90tmpfsroot
%{_libdir}/%{name}/%{name}-init.sh
%{_datadir}/pkgconfig/%{name}.pc
%{dracutlibdir}/%{name}-functions.sh
%{dracutlibdir}/%{name}-functions
%{dracutlibdir}/%{name}-version.sh
%{dracutlibdir}/%{name}-logger.sh
%{dracutlibdir}/%{name}-initramfs-restore
%{dracutlibdir}/%{name}-install
%{dracutlibdir}/skipcpio
%{dracutlibdir}/%{name}-util
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_sysconfdir}/%{name}.conf.d
%dir %{dracutlibdir}/%{name}.conf.d
%dir %{_var}/opt/%{name}/log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_var}/opt/%{name}/log/%{name}.log
%{_var}/log/%{name}.log
%dir %{_sharedstatedir}/initramfs
%{_unitdir}/%{name}-shutdown.service
%{_unitdir}/sysinit.target.wants/%{name}-shutdown.service
%{_unitdir}/%{name}-cmdline.service
%{_unitdir}/%{name}-initqueue.service
%{_unitdir}/%{name}-mount.service
%{_unitdir}/%{name}-pre-mount.service
%{_unitdir}/%{name}-pre-pivot.service
%{_unitdir}/%{name}-pre-trigger.service
%{_unitdir}/%{name}-pre-udev.service
%{_unitdir}/dracut-shutdown-onfailure.service
%{_unitdir}/initrd.target.wants/%{name}-cmdline.service
%{_unitdir}/initrd.target.wants/%{name}-initqueue.service
%{_unitdir}/initrd.target.wants/%{name}-mount.service
%{_unitdir}/initrd.target.wants/%{name}-pre-mount.service
%{_unitdir}/initrd.target.wants/%{name}-pre-pivot.service
%{_unitdir}/initrd.target.wants/%{name}-pre-trigger.service
%{_unitdir}/initrd.target.wants/%{name}-pre-udev.service

%files fips
%defattr(-,root,root,0755)
%{dracutlibdir}/modules.d/01fips
%{_sysconfdir}/dracut.conf.d/40-fips.conf
%config(missingok) %{_sysconfdir}/system-fips

%files hostonly
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/00-hostonly.conf

%files hyperv
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/00-hyperv.conf

%files megaraid
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/50-megaraid.conf

%files noxattr
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/50-noxattr.conf

%files tools
%defattr(-,root,root,0755)

%files overlayfs
%dir %{dracutlibdir}/modules.d/20overlayfs
%{dracutlibdir}/modules.d/20overlayfs/*

%files systemd-cryptsetup
%dir %{dracutlibdir}/modules.d/90systemd-cryptsetup
%{dracutlibdir}/modules.d/90systemd-cryptsetup/*

%files tmpfsroot
%dir %{dracutlibdir}/modules.d/90tmpfsroot
%{dracutlibdir}/modules.d/90tmpfsroot/*

%files virtio
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/00-virtio.conf

%files vrf
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/00-vrf.conf

%files xen
%defattr(-,root,root,0755)
%{_sysconfdir}/dracut.conf.d/00-xen.conf

%{_bindir}/%{name}-catimages
%dir /boot/%{name}
%dir %{_sharedstatedir}/%{name}
%dir %{_sharedstatedir}/%{name}/overlay

%changelog
* Fri May 16 2025 Swee Yee Fonn <swee.yee.fonn@intel.com> - 102-13
- Add tmpfsroot dracut module

* Thu Apr 28 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 102-12
- merge from Azure Linux tag 3.0.20250423-3.0
- Add fix for systemd-cryptsetup module to be included in initramfs when needed

* Tue Mar 18 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 102-11
- Bump version for merge AZL tag: 3.0.20250311-3.0
- Update overlayfs selinux handling with the full path of chcon
- Fix 0006-dracut.sh-validate-instmods patch to not break crypto module blacklisting
- Avoid mktemp folder name colliding with find filter.

* Thu Mar 13 2025 Mun Chun Yep <mun.chun.yep@intel.com> - 102-10
- Add package for systemd-cryptsetup module.

* Fri Mar 07 2025 Ranjan Dutta <ranjan.dutta@intel.com> - 102-9
- Bump version for merge AZL tag: 3.0.20250206-3.0
- Augment overlayfs with selinux handling.

* Thu Dec 19 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 102-8
- Update vendor and distribution tag.

* Thu Oct 31 2024 George Mileka <gmileka@microsoft.com> - 102-7
- Augment livenet module with a download daemon.

* Thu Oct 10 2024 Thien Trung Vuong <tvuong@microsoft.com> - 102-6
- Add patch to make tpm2-tss an optional dependency for systemd-pcrphase

* Sun Oct 06 2024 Jon Slobodzian <joslobo@microsoft.com> - 102-5
- Bump version to build with latest systemd

* Mon Aug 19 2024 Cameron Baird <cameronbaird@microsoft.com> - 102-4
- Drop 0002-disable-xattr.patch
- Introduce dracut-noxattr subpackage to expose this behavior as an option

* Thu Aug 08 2024 Cameron Baird <cameronbaird@microsoft.com> - 102-3
- Drop 0007-feat-dracut.sh-support-multiple-config-dirs.patch

* Thu Oct 10 2024 Anuj Mittal <anuj.mittal@intel.com> - 102-2
- Remove systemd-cryptsetup for a custom solution

* Tue Aug 06 2024 Thien Trung Vuong <tvuong@microsoft.com> - 102-2
- Add fix for initrd not showing prompt when root device is locked

* Tue Jun 25 2024 Cameron Baird <cameronbaird@microsoft.com> - 102-1
- Update to 102

* Fri Jun 7 2024 Daniel McIlvaney <damcilva@microsoft.com> - 059-20
- Suppress missing awk errors on size-constrained images

* Thu May 30 2024 Chris Gunn <chrisgun@microsoft.com> - 059-19
- Split defaults into separate subpackages: hostonly, hyperv, virtio, vrf, and xen

* Tue May 28 2024 Cameron Baird <cameronbaird@microsoft.com> - 059-18
- Remove reference to zlib from dracut-fips module setup to address
    pedantic initramfs regeneration behavior

* Fri May 03 2024 Rachel Menge <rachelmenge@microsoft.com> - 059-17
- Patch microcode output check based on CONFIG_MICROCODE_AMD/INTEL

* Wed Mar 27 2024 Cameron Baird <cameronbaird@microsoft.com> - 059-16
- Remove x86-specific xen-acpi-processor driver from defaults

* Fri Mar 22 2024 Lanze Liu <lanzeliu@microsoft.com> - 059-15
- Exclude overlayfs module from main dracut package

* Wed Mar 06 2024 Chris Gunn <chrisgun@microsoft.com> - 059-14
- Move defaults to /etc/dracut.conf.d/00-defaults.conf file
- Add VM guest drivers to default config

* Fri Feb 23 2024 Chris Gunn <chrisgun@microsoft.com> - 059-13
- Remove mkinitrd script
- Set hostonly as default in /etc/dracut.conf

* Wed Feb 07 2024 Dan Streetman <ddstreet@ieee.org> - 059-12
- update to 059

* Wed Jan 03 2024 Susant Sahani <susant.sahani@broadcom.com> 059-11
- Include systemd-executor if available

* Tue Oct 03 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-10
- Add gzip, procps-ng, xz to requires

* Thu Jul 27 2023 Piyush Gupta <gpiyush@vmware.com> 059-9
- fix(dracut-systemd): rootfs-generator cannot write outside of generator dir

* Mon Jul 17 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-8
- Fix a bug in finding installed kernel versions during mkinitrd

* Tue Apr 25 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-7
- Code improvements in multiple conf dir support

* Sat Apr 1 2023 Laszlo Gombos <laszlo.gombos@gmail.com> 059-6
- Update wiki link and remove obsolete references

* Wed Mar 15 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-5
- Add systemd-udev to requires

* Wed Mar 08 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-4
- Add /etc/dracut.conf.d to conf dirs list during initrd creation
- Drop multiple conf file support

* Wed Mar 01 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-3
- Fix mkinitrd verbose & add a sanity check

* Wed Jan 25 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-2
- Fix requires
* Mon Jan 02 2023 Shreenidhi Shedi <sshedi@vmware.com> 059-1
- Upgrade to v059

* Wed Sep 28 2022 Shreenidhi Shedi <sshedi@vmware.com> 057-1
- Upgrade to v057

* Mon Jan 29 2024 Lanze Liu <lanzeliu@microsoft.com> - 055-7
- Add overlayfs sub-package.

* Wed Jan 24 2024 George Mileka <gmileka@microsoft.com> - 055-6
- Add an option to supress user confirmation prompt for ram overlays.

* Thu Apr 27 2023 Daniel McIlvaney <damcilva@microsoft.com> - 055-5
- Avoid using JIT'd perl in grep since it is blocked by SELinux.

* Fri Mar 31 2023 Vince Perri <viperri@microsoft.com> - 055-4
- Add dracut-megaraid package.

* Tue Oct 04 2022 Pawel Winogrodzki <pawelwi@microsoft.com> - 055-3
- Fixing default log location.

* Thu Dec 16 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 055-2
- Removing the explicit %%clean stage.

* Wed Dec 01 2021 Henry Beberman <henry.beberman@microsoft.com> - 055-1
- Update to version 055. Port mkinitrd forward for compatibility.

* Wed Sep 29 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 049-8
- Added missing BR on "systemd-rpm-macros".

* Thu Sep 23 2021 Pawel Winogrodzki <pawelwi@microsoft.com> - 049-7
- Adding 'Provides' for 'dracut-caps'.

* Mon Apr 26 2021 Thomas Crain <thcrain@microsoft.com> - 049-6
- Replace incorrect %%{_lib} usage with %%{_libdir}

* Fri Feb 12 2021 Nicolas Ontiveros <niontive@microsoft.com> - 049-5
- Enable kernel crypto testing in dracut-fips

* Wed Feb 10 2021 Nicolas Ontiveros <niontive@microsoft.com> - 049-4
- Move 40-fips.conf to /etc/dracut.conf.d/

* Mon Feb 01 2021 Nicolas Ontiveros <niontive@microsoft.com> - 049-3
- Add dracut-fips package.
- Disable kernel crypto testing in dracut-fips.

*   Wed Apr 08 2020 Nicolas Ontiveros <niontive@microsoft.com> 049-2
-   Remove toybox from requires.

*   Thu Mar 26 2020 Nicolas Ontiveros <niontive@microsoft.com> 049-1
-   Update version to 49. License verified.

*   Tue Sep 03 2019 Mateusz Malisz <mamalisz@microsoft.com> 048-2
-   Initial CBL-Mariner import from Photon (license: Apache2).

*   Mon Oct 01 2018 Alexey Makhalov <amakhalov@vmware.com> 048-1
-   Version update

*   Thu Dec 28 2017 Divya Thaluru <dthaluru@vmware.com>  045-6
-   Fixed the log file directory structure

*   Mon Sep 18 2017 Alexey Makhalov <amakhalov@vmware.com> 045-5
-   Requires coreutils/util-linux/findutils or toybox,
    /bin/grep, /bin/sed

*   Fri Jun 23 2017 Xiaolin Li <xiaolinl@vmware.com> 045-4
-   Add kmod-devel to BuildRequires

*   Fri May 26 2017 Bo Gan <ganb@vmware.com> 045-3
-   Fix dependency

*   Thu Apr 27 2017 Bo Gan <ganb@vmware.com> 045-2
-   Disable xattr for cp

*   Wed Apr 12 2017 Chang Lee <changlee@vmware.com> 045-1
-   Updated to 045

*   Wed Jan 25 2017 Harish Udaiya Kumar <hudaiyakumr@vmware.com> 044-6
-   Added the patch for bash 4.4 support.

*   Wed Nov 23 2016 Anish Swaminathan <anishs@vmware.com>  044-5
-   Add systemd initrd root device target to list of modules

*   Fri Oct 07 2016 ChangLee <changlee@vmware.com> 044-4
-   Modified %check

*   Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 044-3
-   GA - Bump release of all rpms

*   Thu Apr 25 2016 Gengsheng Liu <gengshengl@vmware.com> 044-2
-   Fix incorrect systemd directory.

*   Thu Feb 25 2016 Kumar Kaushik <kaushikk@vmware.com> 044-1
-   Updating Version.
