%global pypi_name lifx-photons-interactor
%global short_name photons-interactor

Name:           python-%{pypi_name}
Version:        0.8.1
Release:        1%{?dist}
Summary:        A Photons powered server for interacting with LIFX lights

License:        MIT
URL:            https://photons.delfick.com
Source0:        %{pypi_source}
Source1:        %{short_name}.service
Source2:        %{short_name}.yml
Source3:        %{short_name}.xml
Source4:        %{short_name}.sysusers

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros

%{?systemd_requires}
%{?sysusers_requires_compat}

# Bypass the strict dependencies declared upstream
%{?python_disable_dependency_generator}

%global _description %{expand:
A Photons powered server for interacting with LIFX lights over the lan.
The server allows us to do continuous discovery and information gathering
so that all commands are super fast.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       lifx-photons-interactor
Provides:       photons-interactor
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       firewalld-filesystem
Requires:       python3dist(aiohttp) >= 3.7.2
Requires:       python3dist(alembic) >= 1.3.2
Requires:       python3dist(lifx-photons-core) >= 0.32.5
Requires:       python3dist(setuptools)
Requires:       python3dist(sqlalchemy) > 1.3.3
Requires:       python3dist(tornado) >= 6.1
Requires:       python3dist(whirlwind-web) >= 0.9

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

mkdir -p %{buildroot}%{_unitdir} \
         %{buildroot}%{_sysconfdir}/photons \
         %{buildroot}%{_sysusersdir} \
         %{buildroot}%{_usr}/lib/firewalld/services \
         %{buildroot}%{_var}/lib/photons

install -m 644 %SOURCE1 %{buildroot}%{_unitdir}
install -m 644 %SOURCE2 %{buildroot}%{_sysconfdir}/photons/interactor.yml
install -m 644 %SOURCE4 %{buildroot}%{_sysusersdir}/%{short_name}.conf
install -m 644 %SOURCE3 %{buildroot}%{_usr}/lib/firewalld/services

%pre -n python3-%{pypi_name}
%sysusers_create_package %{short_name} %SOURCE4

%post -n python3-%{pypi_name}
%systemd_post %{short_name}.service
%firewalld_reload

%preun -n python3-%{pypi_name}
%systemd_preun %{short_name}.service

%postun -n python3-%{pypi_name}
%systemd_postun_with_restart %{short_name}.service

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst

%dir %{_sysconfdir}/photons
%config(noreplace) %{_sysconfdir}/photons/interactor.yml

%attr(755,photons,-) %dir %{_var}/lib/photons
%attr(644,photons,-) %ghost %{_var}/lib/photons/interactor.db

# systemd and firewalld configuration files
%{_sysusersdir}/%{short_name}.conf
%{_usr}/lib/firewalld/services/photons-interactor.xml
%{_unitdir}/photons-interactor.service

%{python3_sitelib}/interactor
%{python3_sitelib}/lifx_photons_interactor-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller <me@dje.li> - 0.8.1-1
- Initial packaging of lifx-photons-interactor from PyPi.
