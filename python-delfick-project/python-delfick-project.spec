# Created by pyp2rpm-3.3.5
%global pypi_name delfick-project

Name:           python-%{pypi_name}
Version:        0.7.8
Release:        1%{?dist}
Summary:        Common code I use in all my projects

License:        MIT
URL:            https://github.com/delfick/delfick_project
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/delfick_project-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Project helpers This is a collection of code that I use in nearly all my
projects:
* Mainline helper
* Custom python exception class
* Logging helpers
* Option merging
* Validation and Normalisation of data
* Module addon system

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(rainbow-logging-handler) = 2.2.2
%description -n python3-%{pypi_name}
Project helpers This is a collection of code that I use in nearly all my
projects:
* Mainline helper
* Custom python exception class
* Logging helpers
* Option merging
* Validation and Normalisation of data
* Module addon system

%prep
%autosetup -n delfick_project-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/delfick_project
%{python3_sitelib}/delfick_project-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller <me@dje.li> - 0.7.8-1
- Initial packaging of delfick-project from PyPi.
