Summary:        A Python module that tries to figure out what your local timezone is
Name:           python-tzlocal
Version:        5.2
Release:        4%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/regebro/tzlocal
# pypi/pythonhosted tarballs don't respect symlinks which are used in the test
Source0:        https://github.com/regebro/tzlocal/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-mock
Requires:       python3-pytz

%global common_description %{expand:
This Python module returns a tzinfo object with the local timezone information.
It requires pytz, and returns pytz tzinfo objects. This module attempts to fix
a glaring hole in pytz, that there is no way to get the local timezone
information, unless you know the zoneinfo name.}
%description %{common_description}

%package -n python3-tzlocal
Summary:        %{summary}
%description -n python3-tzlocal %{common_description}

%prep
%autosetup -n tzlocal-%{version}
%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tzlocal

%check
%pytest

%files -n python3-tzlocal -f %{pyproject_files}
# pyproject_files handles LICENSE.txt; verify with “rpm -qL -p …”
%doc README.rst CHANGES.txt

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 5.2-4
- Update Source URL.

* Mon Oct 21 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 5.2-3
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
