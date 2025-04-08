%global lld_srcdir llvm-project-llvmorg-%{version}

Summary:        LLD is a linker from the LLVM project that is a drop-in replacement for system linkers and runs much faster than them
Name:           lld14
Version:        14.0.5
Release:        2%{?dist}
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://lld.llvm.org/
Source0:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{version}.tar.gz
BuildRequires:  build-essential
BuildRequires:  cmake
BuildRequires:  file
BuildRequires:  llvm14-devel
BuildRequires:  ninja-build
BuildRequires:  python3
Requires:       %{name}-libs = %{version}-%{release}

%package devel
Summary:        Libraries and header files for LLD
Requires:       %{name} = %{version}-%{release}

%package libs
Summary:        LLD shared libraries

%description
The LLVM project linker.

%description devel
This package contains library and header files needed to develop new native
programs that use the LLD infrastructure.

%description libs
Shared libraries for LLD.

%prep
%setup -q -n %{lld_srcdir}

%build
mkdir -p build
cd build
%cmake ..                                                         \
       -G Ninja                                                   \
       -DCMAKE_BUILD_TYPE=Release                                 \
       -DCMAKE_SKIP_RPATH:BOOL=on                                 \
       -DCMAKE_C_FLAGS=-I../../libunwind-%{version}.src/include   \
       -DCMAKE_CXX_FLAGS=-I../../libunwind-%{version}.src/include \
       -DLLVM_LINK_LLVM_DYLIB:BOOL=on                             \
       -DLLVM_DYLIB_COMPONENTS="all"                              \
       -Wno-dev ../lld

%ninja_build

%install
cd build
%ninja_install

%files
%{_bindir}/*

%files devel
%{_includedir}/lld/
%{_libdir}/cmake/lld/*.cmake
%{_libdir}/*.so

%files libs
%{_libdir}/*.so.*

%changelog
* Tue Dec 24 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 14.0.5-2
- Updated initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.5-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
