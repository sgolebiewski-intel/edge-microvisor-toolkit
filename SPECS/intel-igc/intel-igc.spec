%global llvm_compat 14

Name:           intel-igc
Version:        1.0.17537.20
Release:        3%{?dist}
Summary:        Intel Graphics Compiler for OpenCL
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/intel-graphics-compiler
Source0:        %{url}/archive/igc-%{version}/igc-%{version}.tar.gz

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  make
#BuildRequires:  git
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  llvm%{?llvm_compat}-devel
BuildRequires:  lld%{?llvm_compat}-devel
BuildRequires:  clang%{?llvm_compat}
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  python3
BuildRequires:  python3-mako
BuildRequires:  python3-PyYAML
BuildRequires:  zlib-devel
BuildRequires:  intel-opencl-clang-devel
BuildRequires:  spirv-llvm-translator-devel
BuildRequires:  spirv-llvm-translator-tools
BuildRequires:  vc-intrinsics-devel
BuildRequires:  spirv-headers-devel
BuildRequires:  spirv-tools-devel

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description
The Intel Graphics Compiler for OpenCL is an LLVM based compiler for OpenCL targeting Intel Gen graphics hardware architecture.

%package       devel
Summary:       Intel Graphics Compiler Frontend - Devel Files
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description   devel
Devel files for Intel Graphics Compiler for OpenCL.

%package       libs
Summary:       Intel Graphics Compiler Frontend - Library Files
Requires:      %{name} = %{version}-%{release}

%description   libs
Library files for Intel Graphics Compiler for OpenCL.

%prep
%autosetup -n intel-graphics-compiler-igc-%{version} -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DIGC_OPTION__LINK_KHRONOS_SPIRV_TRANSLATOR=ON \
    -DIGC_BUILD__VC_ENABLED=ON \
    -DIGC_OPTION__SPIRV_TRANSLATOR_MODE=Prebuilds \
    -DIGC_OPTION__CLANG_MODE=Prebuilds \
    -DIGC_OPTION__LLD_MODE=Prebuilds \
    -DIGC_OPTION__LLVM_MODE=Prebuilds \
    -DLLVM_ROOT=%{_libdir}/cmake/llvm \
    -DIGC_OPTION__SPIRV_TOOLS_MODE=Prebuilds \
    -DIGC_OPTION__USE_PREINSTALLED_SPIRV_HEADERS=ON \
    -DIGC_OPTION__VC_INTRINSICS_MODE=Prebuilds \
    -DCMAKE_C_FLAGS="" \
    -DCMAKE_CXX_FLAGS="" \
    -DCMAKE_INSTALL_PREFIX=/usr/ \
    -DCMAKE_INSTALL_LIBDIR=/usr/lib \
    -DINSTALL_GENX_IR=ON \
    -Wno-dev \
    -G Ninja
%cmake_build

%install
%cmake_install
%files
%{_bindir}/iga{32,64}
%{_bindir}/GenX_IR

%files libs
%license LICENSE.md
%license %{_libdir}/igc/NOTICES.txt
%dir %{_libdir}/igc/
%{_libdir}/libiga{32,64}.so.1{,.*}
%{_libdir}/libigc.so.1{,.*}
%{_libdir}/libigdfcl.so.1{,.*}

%files devel
%{_libdir}/libiga{32,64}.so
%{_libdir}/libigc.so
%{_libdir}/libigdfcl.so
%{_includedir}/igc
%{_includedir}/iga
%{_includedir}/visa
%{_libdir}/pkgconfig/igc-opencl.pc

%changelog
* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0.17537.20-3
- Updated initial changelog entry having fedora version and license info.

* Fri Nov 15 2024 Chee Yang Lee <chee.yang.lee@intel.com> - 1.0.17537.20-2
- BuildRequires python3-pyyaml -> python3-PyYAML

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 1.0.17537.20-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
