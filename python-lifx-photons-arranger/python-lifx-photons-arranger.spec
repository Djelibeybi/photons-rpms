%global pypi_name lifx-photons-arranger

Name:           python-%{pypi_name}
Version:        0.5.9
Release:        1%{?dist}
Summary:        A web interface for changing the user co-ordinates of LIFX tiles

License:        MIT
URL:            http://github.com/delfick/photons/apps/arranger
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%global _description %{expand:
This is a web UI for arranging the positions of a number of LIFX Tiles relative
to each other.}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

Provides:       lifx-photons-arranger
Provides:       photons-arranger
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(lifx-photons-core) >= 0.32.5
Requires:       python3dist(setuptools)
Requires:       python3dist(tornado) >= 5.1.1
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

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/arranger
%{python3_sitelib}/lifx_photons_arranger-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller <me@dje.li> - 0.5.9-1
- Initial packaging of lifx-photons-arranger from PyPi.
