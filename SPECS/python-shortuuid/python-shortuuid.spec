Summary:        A generator library for concise, unambiguous and URL-safe UUIDs
Name:           python-%{srcname}
Version:        1.0.13
Release:        2%{?dist}
License:        BSD-3-Clause
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/skorokithakis/shortuuid
Source0:        https://github.com/skorokithakis/shortuuid/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%global srcname shortuuid
%global _description %{expand:
shortuuid is a simple python library that generates concise, unambiguous,
URL-safe UUIDs.
Often, one needs to use non-sequential IDs in places where users will see them,
but the IDs must be as concise and easy to use as possible. shortuuid solves
this problem by generating uuids using Python's built-in uuid module and then
translating them to base57 using lowercase and uppercase letters and digits, and
removing similar-looking characters such as l, 1, I, O and 0.}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-fastjsonschema
BuildRequires:  python%{python3_pkgversion}-lark
BuildRequires:  python%{python3_pkgversion}-pip
BuildRequires:  python%{python3_pkgversion}-poetry-core
BuildRequires:  python%{python3_pkgversion}-setuptools
# Test dependencies:
BuildRequires:  python3dist(pytest)
BuildArch:      noarch

%description %{_description}

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname} %{_description}

%prep
%autosetup -p1 -n %{srcname}-%{version}


%generate_buildrequires
%pyproject_buildrequires -r


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}

# this file is wrongly copied
rm %{buildroot}%{python3_sitelib}/COPYING


%check
%pytest -V


%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%license COPYING
%doc README.md
%{_bindir}/shortuuid

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.0.13-3
- Update Source URL.

* Thu Dec 19 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0.13-2
- Add vendor and distribution tag.

* Wed Aug 28 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.0.13-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Dec 10 2021 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.8-1
- Update to 1.0.8
- Adjust spec for latest packaging guidelines
- Opt in to rpmautospec

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.0.1-5
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.1-2
- Rebuilt for Python 3.9

* Sat Mar 07 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Fri Mar 06 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-11
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct 12 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.5.0-7
- Python2 binary package has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.5.0-5
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.5.0-3
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar  1 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.0-1
- Update to 0.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.1-1
- initial packaging
