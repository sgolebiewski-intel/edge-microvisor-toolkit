Name:           ocl-icd
Version:        2.3.2
Release:        2%{?dist}
Summary:        OpenCL Library (Installable Client Library) Bindings
License:        BSD-2-Clause
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/OCL-dev/%{name}/
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  opencl-headers
BuildRequires:  ruby rubygems
BuildRequires:  asciidoc
BuildRequires:  xmlto

%description
%{summary}.

%package devel
Summary:        OpenCL Library Development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opencl-headers

%description devel
This package contains the development files for the OpenCL ICD bindings.

%prep
%autosetup
%build
autoreconf -vfi
%configure
%make_build
%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.la
rm -vrf %{buildroot}%{_defaultdocdir}

%check
make check

%ldconfig_scriptlets
%files
%license COPYING
%doc NEWS README
%{_libdir}/libOpenCL.so.*
%{_mandir}/man7/libOpenCL*.7.*

%files devel
%doc ocl_icd_loader_gen.map ocl_icd_bindings.c
%{_includedir}/ocl_icd.h
%{_bindir}/cllayerinfo
%{_libdir}/libOpenCL.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/OpenCL.pc

%changelog
* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2.3.2-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 2.3.2-1
- Initial Edge Microvisor Toolkit import from Fedora 38 (license: MIT). License verified.
