# Created by pyp2rpm-3.3.5
%global pypi_name rainbow_logging_handler

Name:           python-%{pypi_name}
Version:        2.2.2
Release:        1%{?dist}
Summary:        Ultimate Python colorized logger with user-custom color

License:        LICENSE.txt
URL:            https://github.com/laysakura/rainbow_logging_handler
Source0:        %{pypi_source %{pypi_name} %{version} zip}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(coverage)
BuildRequires:  python3dist(logutils)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(nose-cov)
BuildRequires:  python3dist(setuptools)

%description
rainbow_logging_handler Ultimate Python colorized logger... contents::
:local:Usage Generic usage example This script runs like above screenshot...
code-block:: python import sys

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(colorama)
Requires:       python3dist(logutils)
%description -n python3-%{pypi_name}
rainbow_logging_handler Ultimate Python colorized logger... contents::
:local:Usage Generic usage example This script runs like above screenshot...
code-block:: python import sys


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
%license LICENSE.txt
%doc README.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller - 2.2.2-1
- Initial packaging of rainbow_logging_handler from PyPi.
