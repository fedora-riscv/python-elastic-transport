%global pypi_name elastic-transport

%global _description %{expand:
Transport classes and utilities shared among Python Elastic client libraries

This library was lifted from elasticsearch-py and then transformed to be used
across all Elastic services rather than only Elasticsearch.}

Name:		python-%{pypi_name}
Version:	8.1.2
Release:	2%{?dist}
Summary:	Transport classes and utilities shared among Python Elastic

License:	ASL 2.0
URL:		https://github.com/elastic/elastic-transport-python
Source0:	%{pypi_source}

BuildArch:	noarch

%description
%{summary}

%package -n python3-%{pypi_name}
Summary:	%{summary}
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	%{py3_dist setuptools}

%description -n python3-%{pypi_name} %_description

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf elastic_transport.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc CHANGELOG.md
%doc README.md
%license LICENSE
%{python3_sitelib}/elastic_transport
%{python3_sitelib}/elastic_transport-%{version}-py%{python3_version}.egg-info

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 8.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat May 21 2022 Ali Erdinc Koroglu <aekoroglu@fedorapackage.org> - 8.1.2-1
- Initial package
