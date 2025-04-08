Summary:        XPath 1.0/2.0 parsers and selectors for ElementTree and lxml
Name:           python-elementpath
Version:        4.4.0
Release:        2%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/sissaschool/elementpath
Source0:        https://github.com/sissaschool/elementpath/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-wheel
BuildRequires:  python3-pip

%global _description %{expand:
The proposal of this package is to provide XPath 1.0, 2.0 and 3.0 selectors for
Python's ElementTree XML data structures, both for the standard ElementTree
library and for the lxml.etree library.

For lxml.etree this package can be useful for providing XPath 2.0 selectors,
because lxml.etree already has it's own implementation of XPath 1.0.}

%description %_description

%package -n     python3-elementpath
Summary:        %{summary}
%{?python_provide:%python_provide python3-elementpath}

%description -n python3-elementpath  %_description

%prep
%autosetup -p1 -n elementpath-%{version}
# Remove an upstream workaround for the mypy tests
# https://github.com/sissaschool/elementpath/commit/3431f6d907bda73512edbe1d68507f675b234384
# Upstream has been notified: https://github.com/sissaschool/elementpath/issues/64#issuecomment-1696519082
sed -i '/lxml-stubs/d' tox.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%files -n python3-elementpath
%license LICENSE
%doc README.rst
%{python3_sitelib}/elementpath/
%{python3_sitelib}/elementpath-%{version}.dist-info/

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 4.4.0-2
- Update Source URL.

* Wed Oct 16 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 4.4.0-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 4.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 01 2023 Charalampos Stratakis <cstratak@redhat.com> - 4.1.5-2
- Update to 4.1.5 - enable tests

* Fri Aug 25 2023 Charalampos Stratakis <cstratak@redhat.com> - 4.1.5-1
- Update to 4.1.5
- Disable tests for bootstraping with new version of xmlschema
- Fixes: rhbz#2166299

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jun 16 2023 Python Maint <python-maint@redhat.com> - 3.0.2-5
- Rebuilt for Python 3.12

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 3.0.2-4
- Bootstrap for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Aug 16 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.0.2-2
-  Update to 3.0.2 - enable tests

* Tue Aug 16 2022 Tomáš Hrnčiar <thrnciar@redhat.com> - 3.0.2-1
- Update to 3.0.2
- Fixes: rhbz#2021606

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.2-4
- Rebuilt for Python 3.11

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 2.3.2-3
- Bootstrap for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Nov 05 2021 Joel Capitao <jcapitao@redhat.com> - 2.3.2-1
- Update to 2.3.2
- Fixes rhbz#2000317

* Tue Jul 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.3-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Mon Jul 26 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.2.3-2
- Update to 2.2.3 with tests

* Mon Jul 26 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.2.3-1
- Update to 2.2.3 without tests

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 2.1.2-3
- Rebuilt for Python 3.10

* Wed Jun 02 2021 Python Maint <python-maint@redhat.com> - 2.1.2-2
- Bootstrap for Python 3.10

* Thu Jan 28 12:03:51 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.1.2-1
- Update to 2.1.2

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 09:57:43 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.1.1-2
- Build with tests

* Thu Jan 14 08:35:26 CET 2021 Tomas Hrnciar <thrnciar@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-4
- Rebuilt for Python 3.9

* Sat May 23 2020 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-3
- Bootstrap for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 31 2019 Miro Hrončok <mhroncok@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Tue Dec 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.3.2-1
- Initial package
