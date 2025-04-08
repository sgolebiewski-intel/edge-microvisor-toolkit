Summary:        JSON Schema meta-schemas and vocabularies, exposed as a Registry
Name:           python-jsonschema-specifications
Version:        2023.11.2
Release:        7%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/python-jsonschema/jsonschema-specifications
Source0:        https://github.com/python-jsonschema/jsonschema-specifications/releases/download/v%{version}/jsonschema_specifications-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-hatchling
BuildRequires:  python3-pathspec
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-trove-classifiers

%global with_tests 1
%global common_description %{expand:
JSON support files from the JSON Schema Specifications (metaschemas,
vocabularies, etc.), packaged for runtime access from Python as a
referencing-based Schema Registry.}
%description %{common_description}

%package -n     python3-jsonschema-specifications
Summary:        %{summary}
%description -n python3-jsonschema-specifications %{common_description}

%if 0%{?with_tests}
%package  -n    python3-jsonschema-specifications-tests
Summary:        Tests for the JSON Schema specifications
BuildRequires:  python3dist(pytest)
Requires:       python3dist(pytest)
Requires:       python3-jsonschema-specifications = %{version}-%{release}
%description -n python3-jsonschema-specifications-tests
Tests for the JSON Schema specifications
%endif

%prep
%autosetup -n jsonschema_specifications-%{version}
sed -i "/^file:.*/d" docs/requirements.in
sed -i "/^pygments-github-lexers/d" docs/requirements.in
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files jsonschema_specifications

%if 0%{?with_tests}
%check
%pytest
%endif

%files -n python3-jsonschema-specifications -f %{pyproject_files}
%license COPYING
%doc README.rst
%exclude %{python3_sitelib}/jsonschema_specifications/tests
%exclude %{python3_sitelib}/jsonschema_specifications-%{version}.dist-info/licenses/COPYING

%if 0%{?with_tests}
%files -n python3-jsonschema-specifications-tests
%license COPYING
%{python3_sitelib}/jsonschema_specifications/tests
%endif

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 2023.11.2-7
- Update Source URL.

* Tue Oct 22 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 2023.11.2-6
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.11.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 09 2024 Python Maint <python-maint@redhat.com> - 2023.11.2-5
- Rebuilt for Python 3.13

* Sat Jun 08 2024 Python Maint <python-maint@redhat.com> - 2023.11.2-4
- Bootstrap for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.11.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2023.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Nov 30 2023 Joel Capitao <jcapitao@redhat.com> - 2023.11.2-1
- Update to 2023.11.2 (rhbz#2252278)

* Mon Nov 20 2023 Joel Capitao <jcapitao@redhat.com> - 2023.11.1-1
- Update to 2023.11.1 (rhbz#2249692)

* Mon Aug 07 2023 Joel Capitao <jcapitao@redhat.com> - 2023.7.1-1
- Initial package.

