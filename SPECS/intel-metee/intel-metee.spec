Summary:        Intel ME TEE Library
Name:           intel-metee
Version:        4.2.1
Release:        2%{?dist}
# Most of the source code is Apache-2.0, with the following exceptions:
# src/linux/include/linux/mei.h: (GPL-2.0 WITH Linux-syscall-note) OR BSD-3-Clause
# src/linux/libmei.h: BSD-3-Clause
# src/linux/mei.c: BSD-3-Clause
License:        Apache-2.0 AND BSD-3-Clause AND ((GPL-2.0-only WITH Linux-syscall-note) OR BSD-3-Clause)
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/metee
Source0:        https://github.com/intel/metee/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.1
BuildRequires:  gcc-c++
BuildRequires:  doxygen
# Upstream only supports x86_64
ExclusiveArch:  x86_64

%description
Cross-platform access library for Intel CSME HECI interface.

%package devel
Summary:    Development files for %{name}
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
applications that use %{name}.

%package doc
Summary:    Documentation files for %{name}
BuildArch:  noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.

%prep
%autosetup -p1 -n metee-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc CHANGELOG.md README.md SECURITY.md
%{_libdir}/libmetee.so.%{version}

%files devel
%{_includedir}/metee.h
%{_libdir}/libmetee.so

%files doc
%license COPYING
%{_docdir}/intel-metee

%changelog
* Fri Dec 27 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 4.2.1-2
- Update Source URL.

* Tue Oct 08 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 4.2.1-1
- Upgrade to version 4.2.1

* Fri Oct 04 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 3.2.4-1
- Initial Edge Microvisor Toolkit import from Fedora 42 (license: MIT). License verified.
