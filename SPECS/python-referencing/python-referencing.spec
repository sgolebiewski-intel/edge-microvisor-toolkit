Summary:        An implementation-agnostic implementation of JSON reference resolution
Name:           python-referencing
Version:        0.35.1
Release:        2%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://pypi.python.org/pypi/referencing
Source:         https://github.com/python-jsonschema/referencing/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pip
BuildRequires:  python3-hatch-vcs
BuildRequires:  python3-hatchling
BuildRequires:  python3-pathspec
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-trove-classifiers

%global _description %{expand:
An implementation-agnostic implementation of JSON reference resolution.
In other words, a way for e.g. JSON Schema tooling to resolve the $ref
keyword across all drafts without needing to implement support themselves.}
%description %_description

%package -n     python3-referencing
Summary:        %{summary}
%description -n python3-referencing %_description

%prep
%autosetup -n referencing-%{version} -p1
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files referencing

%check
%pyproject_check_import -e referencing.tests*
%pytest referencing/tests

%files -n python3-referencing -f %{pyproject_files}
%exclude %{python3_sitelib}/referencing-%{version}.dist-info/licenses/COPYING

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 0.35.1-2
- Update Source URL.

* Wed Oct 23 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 0.35.1-1
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.
