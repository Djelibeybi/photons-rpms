# Created by pyp2rpm-3.3.5
%global pypi_name whirlwind-web

Name:           python-%{pypi_name}
Version:        0.10.0
Release:        1%{?dist}
Summary:        Wrapper around the tornado web server library

License:        MIT
URL:            http://github.com/delfick/whirlwind
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# Bypass the strict dependencies declared upstream
%{?python_disable_dependency_generator}

%description
Whirlwind A wrapper around the tornado web server.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(aiohttp) >= 3.7
Requires:       python3dist(delfick-project) >= 0.5
Requires:       python3dist(setuptools)
Requires:       python3dist(tornado) >= 5.1.1
%description -n python3-%{pypi_name}
Whirlwind A wrapper around the tornado web server.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/run_whirlwind_pytest
%{python3_sitelib}/whirlwind
%{python3_sitelib}/whirlwind_web-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller - 0.10.0-1
- Initial packaging of whirlwind-web from PyPi.
