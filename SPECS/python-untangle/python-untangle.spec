Summary:        Converts XML to Python objects
Name:           python-untangle
Version:        1.2.1
Release:        6%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/stchris/untangle
#VCS:            https://github.com/stchris/untangle
Source0:        https://github.com/stchris/untangle/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Remove unnecessary shebang
# https://github.com/stchris/untangle/pull/140
Patch0:         python-untangle-1.2.1-shebang.patch
BuildRequires:  python%{python3_pkgversion}-defusedxml
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildArch:      noarch

%description
Converts XML to a Python object. * Siblings with similar names are grouped into
a list. * Children can be accessed with parent.child, attributes with
element['attribute'].

%package -n     python%{python3_pkgversion}-untangle
Summary:        %{summary}
%{?python_provide:%python_provide python3-untangle}

Requires:       python%{python3_pkgversion}-defusedxml

%description -n python%{python3_pkgversion}-untangle
Converts XML to a Python object. Siblings with similar names are grouped into
a list. Children can be accessed with parent.child, attributes with
element.

%prep
%autosetup -n untangle-%{version}

%build
# using old py3_build/py3_install to keep remain compatible with EPEL7/8 builds
%py3_build

%install
%py3_install

%check
%pytest -sv

%files -n python%{python3_pkgversion}-untangle
%license LICENSE
%doc README.md AUTHORS CHANGELOG.md
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/untangle.py
%{python3_sitelib}/untangle-%{version}-py%{python3_version}.egg-info

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.2.1-6
- Update Source URL.

* Fri Sep 13 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.2.1-5
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.2.1-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jan 18 2024 Michal Ambroz <rebus@seznam.cz> - 1.2.1-2
- #PR140 - remove unnecessary shebang

* Wed Dec 07 2022 Michal Ambroz <rebus@seznam.cz> - 1.2.1-1
- Initial package.
