%global neo_major 24
%global neo_minor 35
%global neo_build 30872.22

%global _lto_cflags %{nil}
%global optflags %{optflags} -Wno-error=maybe-uninitialized

Name:           intel-compute-runtime
Version:        %{neo_major}.%{neo_minor}.%{neo_build}
Release:        3%{?dist}
Summary:        Compute API support for Intel graphics
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/intel/compute-runtime
Source0:        %{url}/archive/%{version}/compute-runtime-%{version}.tar.gz

# This is just for Intel GPUs
ExclusiveArch:  x86_64

BuildRequires:  cmake
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  intel-gmmlib-devel
BuildRequires:  libva-devel
BuildRequires:  libdrm-devel
BuildRequires:  intel-igc-devel
BuildRequires:  intel-level-zero-devel
BuildRequires:  ninja-build
BuildRequires:  ocl-icd-devel
BuildRequires:  opencl-headers

# This doesn't get added automatically, so specify it explicitly
Requires:       intel-igc

# Let compute-runtime be a meta package for intel-ocloc, intel-opencl and intel-level-zero
Requires:       intel-ocloc = %{version}-%{release}
Requires:       intel-opencl = %{version}-%{release}

# prelim/drm
Provides: bundled(drm-uapi-helper)

%description
The Intel Graphics Compute Runtime for oneAPI Level Zero and OpenCL Driver is an open source project
providing compute API support (Level Zero, OpenCL) for Intel graphics hardware architectures (HD Graphics, Xe).

%package -n    intel-ocloc
Summary:       Tool for managing Intel Compute GPU device binary format

%description -n intel-ocloc
ocloc is a tool for managing Intel Compute GPU device binary format (a format used by Intel Compute GPU runtime).
It can be used for generation (as part of 'compile' command) as well as
manipulation (decoding/modifying - as part of 'disasm'/'asm' commands) of such binary files.

%package -n    intel-ocloc-devel
Summary:       Tool for managing Intel Compute GPU device binary format - Devel Files
Requires:      intel-ocloc%{?_isa} = %{version}-%{release}

%description -n intel-ocloc-devel
Devel files (headers and libraries) for developing against
intel-ocloc (a tool for managing Intel Compute GPU device binary format).

%package -n    intel-opencl
Summary:       OpenCL support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}

%description -n intel-opencl
Implementation for the Intel GPUs of the OpenCL specification - a generic
compute oriented API. This code base contains the code to run OpenCL programs
on Intel GPUs which basically defines and implements the OpenCL host functions
required to initialize the device, create the command queues, the kernels and
the programs and run them on the GPU.

%package -n    intel-level-zero-gpu
Summary:       oneAPI L0 support implementation for Intel GPUs
Requires:      intel-igc-libs%{?_isa}
Requires:      intel-gmmlib%{?_isa}
Requires:      intel-level-zero%{?_isa}
Provides:      intel-level-zero-gpu%{?_isa}

%description -n intel-level-zero-gpu
Implementation for the Intel GPUs of the oneAPI L0 specification -  which provides direct-to-metal
interfaces to offload accelerator devices. Its programming interface can be tailored to any device
needs and can be adapted to support broader set of languages features such as function pointers,
virtual functions, unified memory, and I/O capabilities..

%prep
%autosetup -p1 -n compute-runtime-%{version}

# remove sse2neon completely as we're building just for x86(_64)
rm -rv third_party/sse2neon

%build
# -DNEO_DISABLE_LD_GOLD=1 for https://bugzilla.redhat.com/show_bug.cgi?id=2043178 and https://bugzilla.redhat.com/show_bug.cgi?id=2043758
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DNEO_OCL_VERSION_MAJOR=%{neo_major} \
    -DNEO_OCL_VERSION_MINOR=%{neo_minor} \
    -DNEO_VERSION_BUILD=%{neo_build} \
    -DSKIP_UNIT_TESTS=1 \
    -DNEO_DISABLE_LD_GOLD=1 \
    -DCL_TARGET_OPENCL_VERSION=300
%cmake_build

%install
%cmake_install
# Symlink to provide ocloc
pushd %{buildroot}%{_bindir}
ln -s ocloc-* ocloc
popd

%files

%files -n intel-opencl
%license LICENSE.md
%dir %{_libdir}/intel-opencl/
%{_libdir}/intel-opencl/libigdrcl.so
%{_sysconfdir}/OpenCL/vendors/intel.icd

%files -n intel-ocloc
%license LICENSE.md
%{_bindir}/ocloc
%{_bindir}/ocloc-*
%{_libdir}/libocloc.so

%files -n intel-ocloc-devel
%{_includedir}/ocloc_api.h

%files -n intel-level-zero-gpu
%license LICENSE.md
%{_libdir}/libze_intel_gpu.so.*
%{_includedir}/level_zero/zet_intel_gpu_debug.h

%doc
%changelog
* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 24.35.30872.22-3
- Update initial changelog entry having fedora version and license info.

* Mon Nov 18 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.35.30872.22-2
- Adding intel level zero plugin package

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 24.35.30872.22-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
