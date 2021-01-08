# Created by pyp2rpm-3.3.5
%global pypi_name lru-dict

Name:           python-%{pypi_name}
Version:        1.1.6
Release:        1%{?dist}
Summary:        An Dict like LRU container

License:        MIT
URL:            https://github.com/amitdev/lru-dict
Source0:        %{pypi_source}

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. This is a fast and efficient C implementation.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A fixed size dict like container which evicts Least Recently Used (LRU) items
once size limit is exceeded. There are many python implementations available
which does similar things. This is a fast and efficient C implementation.

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
%doc README.rst
%{python3_sitearch}/lru.cpython-*
%{python3_sitearch}/lru_dict-%{version}-py%{python3_version}.egg-info

%changelog
* Wed Jan 06 2021 Avi Miller - 1.1.6-1
- Initial packaging of lru-dict from PyPi.
