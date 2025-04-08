Summary:        Tool used in initramfs to seal/unseal FDE key to the TPM
Name:           tpm2-initramfs-tool
Version:        0.2.2
Release:        2%{?dist}
License:        GPLv2
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/timchen119/tpm2-initramfs-tool
Source0:        https://github.com/timchen119/tpm2-initramfs-tool/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf-archive
BuildRequires:  tpm2-tss-devel
Requires:       tpm2-tss

%global _description %{expand:
This tool using the tpm2-tss software stack. Its purpose is to generate/seal/unseal
the Full Disk Encryption (FDE) key into the TPM persistent object using TPM2 ESAPI.
}

%description %_description

%prep
%setup -q

%build
./bootstrap
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license LICENSE
%doc README.md
%{_bindir}/tpm2-initramfs-tool
%{_libdir}/pkgconfig/tpm2-initramfs-tool.pc

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.2.2-2
- Update Source URL.

* Fri Sep 20 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 0.2.2-1
- Original version for Edge Microvisor Toolkit. License verified.
