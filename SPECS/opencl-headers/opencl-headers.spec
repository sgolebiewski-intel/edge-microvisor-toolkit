Name:           opencl-headers
Version:        2024.05.08
Release:        2%{?dist}
Summary:        OpenCL (Open Computing Language) header files
License:        Apache-2.0
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/KhronosGroup/OpenCL-Headers/
Source0:        %{url}archive/v%{version}/opencl-headers-v%{version}.tar.gz

BuildArch:      noarch

%description
%{summary}.

%prep
%autosetup -n OpenCL-Headers-%{version}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/CL/
install -p -m 0644 CL/* -t %{buildroot}%{_includedir}/CL/
# We're not interested in Direct3D things
rm -vf %{buildroot}%{_includedir}/CL/cl_{dx9,d3d}*
# Install pkgconfig files
mkdir -p %{buildroot}%{_datadir}/pkgconfig
sed -e 's|@CMAKE_INSTALL_PREFIX@|%{_prefix}|' -e 's|@OPENCL_INCLUDEDIR_PC@|%{_includedir}|' OpenCL-Headers.pc.in > %{buildroot}%{_datadir}/pkgconfig/OpenCL-Headers.pc

%files
%dir %{_includedir}/CL
%{_includedir}/CL/cl_egl.h
%{_includedir}/CL/cl_ext.h
%{_includedir}/CL/cl_ext_intel.h
%{_includedir}/CL/cl_function_types.h
%{_includedir}/CL/cl_gl_ext.h
%{_includedir}/CL/cl_gl.h
%{_includedir}/CL/cl.h
%{_includedir}/CL/cl_half.h
%{_includedir}/CL/cl_icd.h
%{_includedir}/CL/cl_layer.h
%{_includedir}/CL/cl_platform.h
%{_includedir}/CL/cl_va_api_media_sharing_intel.h
%{_includedir}/CL/cl_version.h
%{_includedir}/CL/opencl.h
%{_datadir}/pkgconfig/OpenCL-Headers.pc

%changelog
* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2024.05.08-2
- Update initial changelog entry having fedora version and license info.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 2024.05.08-1
- Initial Edge Microvisor Toolkit import from Fedora 40 (license: MIT). License verified.
