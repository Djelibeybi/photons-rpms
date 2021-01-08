Name: python-nose-cov
Version: 1.6
Release: 21%{?dist}
Summary: nose plugin for coverage reporting, including subprocesses and multiprocessing
Source0: https://pypi.python.org/packages/source/n/nose-cov/nose-cov-%{version}.tar.gz
License: MIT
BuildArch: noarch
Url: http://bitbucket.org/memedough/nose-cov/overview

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
This plugin produces coverage reports and supports coverage of subprocesses.

%package -n python3-nose-cov
Summary: nose plugin for coverage reporting, including subprocesses and multiprocessing
Requires:  python3-nose
Requires:  python3-cov-core
%{?python_provide:%python_provide python3-nose-cov}
%description -n python3-nose-cov
This plugin produces coverage reports and supports coverage of subprocesses.

%prep
%setup -q -n nose-cov-%{version}
rm -rf nose_cov.egg-info


%build
%py3_build


%install
%py3_install


%files -n python3-nose-cov
%doc README.txt
%doc LICENSE.txt
%{python3_sitelib}/nose_cov*.egg-info
%{python3_sitelib}/nose_cov.py*
%{python3_sitelib}/__pycache__/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Miro Hrončok <mhroncok@redhat.com> - 1.6-20
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6-18
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 1.6-17
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.6-13
- Rebuilt for Python 3.7

* Thu Mar 22 2018 John Dulaney <jdulaney@fedoraproject.org> - 1.6-13
- Drop python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.6-11
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.6-8
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.6-5
- Update spec file to new standards

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jul 10 2015 John Dulaney <jdulaney@fedoraproject.org> - 1.6-3
- Python 3

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Sep 29 2014 John Dulaney <jdulaney@fedoraproject.org> - 1.6-1
- Initial packaging
- Spec based on python-nose
