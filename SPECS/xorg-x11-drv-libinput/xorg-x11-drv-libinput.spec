%global tarball xf86-input-libinput
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/input

Summary:    Xorg X11 libinput input driver
Name:       xorg-x11-drv-libinput
Version:    1.5.0
Release:    3%{?dist}
URL:        https://www.x.org
Source0:    %{url}/archive/individual/driver/%{tarball}-%{version}.tar.xz
# SPDX
License:    MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: xorg-x11-server-devel >= 1.14.0
BuildRequires: libudev-devel libevdev-devel libinput-devel >= 0.6.0-3
BuildRequires: xorg-x11-util-macros

Requires: xkeyboard-config
Requires: libinput >= 0.21.0

Provides: xorg-x11-drv-synaptics = 1.9.0-3
Obsoletes: xorg-x11-drv-synaptics < 1.9.0-3

%description
A generic input driver for the X.Org X11 X server based on libinput,
supporting all devices.

%prep
%autosetup -p 1 -n %{tarball}-%{version}

%build
autoreconf --force -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%doc COPYING
%{driverdir}/libinput_drv.so
%{_datadir}/X11/xorg.conf.d/40-libinput.conf
%{_mandir}/man4/libinput.4*

%package devel
Summary:        Xorg X11 libinput input driver development package.
Requires:       pkgconfig
%description devel
Xorg X11 libinput input driver development files.

%files devel
%doc COPYING
%{_libdir}/pkgconfig/xorg-libinput.pc
%dir %{_includedir}/xorg/
%{_includedir}/xorg/libinput-properties.h

%changelog
* Thu Feb 27 2025 Lee Chee Yang <chee.yang.lee@intel.com> - 1.5.0-3
- Add Vendor and Distribution

* Fri Feb 14 2025 Naveen Saini <naveen.kumar.saini@intel.com> - 1.5.0-2
- Fix source url.

* Fri Oct 18 2024 Junxiao Chang <junxiao.chang@intel.com> - 1.5.0-1
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT). License verified.
