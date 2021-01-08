%global pypi_name lifx-photons-core

Name:           python-%{pypi_name}
Version:        0.32.5
Release:        1%{?dist}
Summary:        Photons core modules

License:        MIT
URL:            http://github.com/delfick/photons
Source0:        %{pypi_source}
Source1:        lifx-discovery.xml
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(bitarray) = 1.6.1
BuildRequires:  python3dist(delfick-project) = 0.7.8
BuildRequires:  python3dist(kdtree) = 0.16
BuildRequires:  python3dist(lru-dict) = 1.1.6
BuildRequires:  python3dist(rainbow-logging-handler) = 2.2.2
BuildRequires:  python3dist(ruamel.yaml) = 0.16.12
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
Photons is Python 3.6+ framework for interacting with LIFX products.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       lifx-photons-core
Provides:       photons-core
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       firewalld-filesystem
Requires:       python3dist(bitarray) = 1.6.1
Requires:       python3dist(delfick-project) = 0.7.8
Requires:       python3dist(kdtree) = 0.16
Requires:       python3dist(lru-dict) = 1.1.6
Requires:       python3dist(rainbow-logging-handler) = 2.2.2
Requires:       python3dist(ruamel.yaml) = 0.16.12
Requires:       python3dist(setuptools)

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_usr}/lib/firewalld/services
install -m 644 %{SOURCE1} %{buildroot}%{_usr}/lib/firewalld/services

%post -n python3-%{pypi_name}
%firewalld_reload

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{_bindir}/lifx
%{_bindir}/run_photons_core_tests
%{_usr}/lib/firewalld/services/lifx-discovery.xml
%pycached %{python3_sitelib}/photons_core.py
%pycached %{python3_sitelib}/photons_pytest.py
%{python3_sitelib}/photons_app
%{python3_sitelib}/photons_canvas
%{python3_sitelib}/photons_control
%{python3_sitelib}/photons_messages
%{python3_sitelib}/photons_products
%{python3_sitelib}/photons_protocol
%{python3_sitelib}/photons_transport
%{python3_sitelib}/lifx_photons_core-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller <me@dje.li> - 0.32.5-1
- Initial packaging of lifx-photons-core from PyPi.
