Summary:        Dracut module to mount persistent partition and create rw paths
Name:           persistent-mount
Version:        1.0
Release:        4%{?dist}
License:        GPLv2+
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          System Environment/Base
URL:            https://dracut.wiki.kernel.org/
Source0:        persistent-mount.conf
Source1:        91persistent-mount/module-setup.sh
Source2:        91persistent-mount/persistent-mount.sh
Source3:        COPYING
Requires:       dracut
Requires:       kpartx
Requires:       acl

%description
Dracut module capable to mount partition and create overlays.
The module will mount a persistent partition and will create tmpfs overlays and
persistent bind mount paths for the files/directories based on configuration file.
See persistent-mount.sh for details.

%install
mkdir -p %{buildroot}%{_sysconfdir}/dracut.conf.d
install -D -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/dracut.conf.d/

mkdir -p %{buildroot}%{_libdir}/dracut/modules.d/91persistent-mount/
install -p -m 0755 %{SOURCE1} %{buildroot}%{_libdir}/dracut/modules.d/91persistent-mount/
install -p -m 0755  %{SOURCE2} %{buildroot}%{_libdir}/dracut/modules.d/91persistent-mount/

cp %{SOURCE3} COPYING

%files
%{_sysconfdir}/dracut.conf.d/persistent-mount.conf
%dir %{_libdir}/dracut/modules.d/91persistent-mount
%{_libdir}/dracut/modules.d/91persistent-mount/*
%license COPYING

%changelog
* Mon Jan 28 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0-4
- Preserve dir permissions during overlayfs mount.

* Tue Nov 12 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0-3
- Drop initramfs from runtime requirements.

* Thu Oct 10 2024 Adithya Baglody <adithya.nagaraj.baglody@intel.com> - 1.0-2
- FDE support.

* Mon Aug 27 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0-1
- Original version for Edge Microvisor Toolkit.
