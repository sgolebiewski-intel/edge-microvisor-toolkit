Summary:        Python URI normalizator
Name:           python-%{srcname}
Version:        1.4.3
Release:        7%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/niksite/url-normalize
Source0:        https://github.com/niksite/url-normalize/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/niksite/url-normalize/pull/28
Patch0:         python-url-normalize-poetry-core.patch
%global srcname url-normalize
%global _description %{expand:
URI Normalization function
 * Take care of IDN domains.
 * Always provide the URI scheme in lowercase characters.
 * Always provide the host, if any, in lowercase characters.
 * Only perform percent-encoding where it is essential.
 * Always use uppercase A-through-F characters when percent-encoding.
 * Prevent dot-segments appearing in non-relative URI paths.
 * For schemes that define a default authority, use an empty authority if the
   default is desired.
 * For schemes that define an empty path to be equivalent to a path of "/",
   use "/".
 * For schemes that define a port, use an empty port if the default is desired
 * All portions of the URI must be utf-8 encoded NFC from Unicode strings
Inspired by Sam Ruby's urlnorm.py:
    http://intertwingly.net/blog/2004/08/04/Urlnorm
This fork author: Nikolay Panov (<pythonista@npanov.com>)
}
BuildRequires:  python3-devel
BuildRequires:  python3-fastjsonschema
BuildRequires:  python3-lark
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
# needed for check
BuildRequires:  python3dist(pytest)
BuildArch:      noarch

%description %{_description}

%generate_buildrequires
%pyproject_buildrequires

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
%autosetup -p 1 -n %{srcname}-%{version}

# supplied tox.ini causes check to fail, will use pytest instead
rm tox.ini

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files url_normalize

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 1.4.3-7
- Update Source URL.

* Thu Dec 19 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.4.3-6
- Add vendor and distribution tag.

* Tue Sep 10 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 1.4.3-5
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 1.4.3-4
- Rebuilt for Python 3.13

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Sep 29 2023 Andrew Bauer <zonexpertconsulting@outlook.com> - 1.4.3-1
- initial specfile
- 1.4.3 release

