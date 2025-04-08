Summary:        Debugging tools for Python
Name:           python-snoop
Version:        0.4.3
Release:        2%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://github.com/alexmojaki/snoop
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm

%global _description %{expand:
Snoop is a powerful set of Python debugging tools. It's primarily meant
to be a more featureful and refined version of PySnooper, a replacement
for debug print statements in code.
}

%description %_description

%package -n python3-snoop
Summary:        %{summary}
%{?python_provides python3-snoop}
%description -n python3-snoop %_description

%prep
%autosetup -n snoop-%{version}

%build
%py3_build

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 -m pytest -v tests/

%files -n python3-snoop
%license LICENSE.txt
%doc README.md
%{python3_sitelib}/snoop/
%{python3_sitelib}/snoop-%{version}-py%{python3_version}.egg-info/

%changelog
* Tue Dec 31 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.4.3-2
- Update Source URL.

* Thu Sep 19 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 0.4.3-1
- Original version for Edge Microvisor Toolkit. License verified.
