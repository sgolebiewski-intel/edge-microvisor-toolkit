Summary:        In-process task scheduler with Cron-like capabilities
Name:           python-apscheduler
Version:        3.10.4
Release:        13%{?dist}
License:        MIT
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
URL:            https://pypi.org/project/APScheduler/
Source0:        https://github.com/agronholm/apscheduler/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
%global srcname apscheduler
%global _description %{expand:
Advanced Python Scheduler (APScheduler) is a Python library that lets you
schedule your Python code to be executed later, either just once or
periodically. You can add new jobs or remove old ones on the fly as you
please. If you store your jobs in a database, they will also survive
scheduler restarts and maintain their state. When the scheduler is
restarted, it will then run all the jobs it should have run while it was
offline.}
%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools_scm
Requires:       python3-pytz
Requires:       python3-tzlocal
%description -n python3-%{srcname} %_description

%prep
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%autosetup -n %{srcname}-%{version} -p1
# Remove that test as it require services (redis, zookeeper, ...)
# up and running. Upstream provides a docker compose to spawn
# services before running these tests.
rm tests/test_jobstores.py
sed -i 's/pytest-tornado5/pytest-tornado/' setup.py
# Remove coverage
sed -i 's/addopts = -rsx --cov/addopts = -rsx/' setup.cfg
sed -i '/pytest-cov/d' setup.py

%generate_buildrequires
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_buildrequires -x testing -x tornado

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files apscheduler

%check
# Default timezone to UTC otherwise unit tests fail.
export TZ=UTC
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
* Mon Dec 30 2024 Naveen Saini <naveen.kumar.saini@intel.com> - 3.10.4-13
- Update Source URL.

* Mon Oct 21 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 3.10.4-12
- Add pytz and tzlocal as runtime dependencies.

* Fri Sep 13 2024 Mun Chun Yep <mun.chun.yep@intel.com> - 3.10.4-11
- Initial Edge Microvisor Toolkit import from Fedora 41 (license: MIT). License verified.

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 3.8.0-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Sep 23 2021 Fedora Release Monitoring <release-monitoring@fedoraproject.org> - 3.8.0-1
- Update to 3.8.0 (#1917870)

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.7.0-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 20 2021 Fabien Boucher <fboucher@redhat.com> - 3.7.0-1
- Upstream 3.7.0 (RHBZ#1917870)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Fabien Boucher <fboucher@redhat.com> - 3.6.3-3
- Update project url

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.6.3-2
- Rebuilt for Python 3.9

* Wed Mar 11 2020 Fabien Boucher <fboucher@redhat.com> - 3.6.3-1
- Inport from SF packaging and bump to 3.6.3 (#1813957)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-4
- Rebuilt for Python 3.8

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 16 2018 Miro Hrončok <mhroncok@redhat.com> - 3.5.3-2
- Subpackage python2-APScheduler has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 20 2018 Haïkel Guémar <hguemar@fedoraproject.org> - 3.5.3-1
- Upstream 3.5.3 (RHBZ#1605579)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-9
- Rebuilt for Python 3.7

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.5-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.5-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.5-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Dec 19 2015 Paul Belanger <pabelanger@redhat.com> - 3.0.5-1
- Initial packaging (#1218410)
