# Created by pyp2rpm-3.3.5
%global pypi_name kdtree

Name:           python-%{pypi_name}
Version:        0.16
Release:        1%{?dist}
Summary:        A Python implemntation of a kd-tree

License:        ISC license
URL:            https://github.com/stefankoegl/kdtree
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This package provides a simple implementation of a kd-tree in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
This package provides a simple implementation of a kd-tree in Python.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%doc readme.md
%pycached %{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller <me@dje.li> - 0.16-1
- Initial packaging of kdtree from PyPi.
