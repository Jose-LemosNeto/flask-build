%if 0%{?fedora} || 0%{?rhel} >=7
%global with_python3 1
%endif


%{!?_licensedir: %global license %%doc}

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global modname flask-migrate

Name:               python-flask-migrate
Version:            2.1.1
Release:            1%{?dist}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic

License:            MIT
URL:                http://pypi.python.org/pypi/flask-migrate
Source0:            https://pypi.python.org/packages/d4/42/9e1bab5b15495e7acd25cb6b164a050b90da20af7e801aa2a7b1f74efdfa/Flask-Migrate-%{version}.tar.gz
BuildArch:          noarch

%description
SQLAlchemy database migrations for Flask applications using Alembic.

%package -n python2-%{modname}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic
%{?python_provide:%python_provide python2-%{modname}}

BuildRequires:      python2-devel

# TODO - rename these to python2-* once those renames are done.
BuildRequires:      python2-flask
BuildRequires:      python2-alembic
BuildRequires:      python2-flask-script

Requires:           python2-flask
Requires:           python2-alembic
Requires:           python2-flask-script

%if 0%{?rhel} && 0%{?rhel} <= 7
BuildRequires:      python-setuptools
BuildRequires:      python-flask-sqlalchemy
Requires:           python-flask-sqlalchemy
%else
BuildRequires:      python2-setuptools
BuildRequires:      python2-flask-sqlalchemy
Requires:           python2-flask-sqlalchemy
%endif

%description -n python2-%{modname}
SQLAlchemy database migrations for Flask applications using Alembic.

%if 0%{?with_python3}
%package -n python%{python3_pkgversion}-%{modname}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic
%{?python_provide:%python_provide python%{python3_pkgversion}-%{modname}}

BuildRequires:      python%{python3_pkgversion}-devel
BuildRequires:      python%{python3_pkgversion}-setuptools
BuildRequires:      python%{python3_pkgversion}-flask
BuildRequires:      python%{python3_pkgversion}-flask-sqlalchemy
BuildRequires:      python%{python3_pkgversion}-alembic
BuildRequires:      python%{python3_pkgversion}-flask-script
Requires:           python%{python3_pkgversion}-flask
Requires:           python%{python3_pkgversion}-flask-sqlalchemy
Requires:           python%{python3_pkgversion}-alembic
Requires:           python%{python3_pkgversion}-flask-script

%description -n python%{python3_pkgversion}-%{modname}
SQLAlchemy database migrations for Flask applications using Alembic.
%endif

%prep
%autosetup -n Flask-Migrate-%{version}

# For rpmlint
chmod 0644 flask_migrate/templates/flask-multidb/*
chmod 0644 flask_migrate/templates/flask/*

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install
%if 0%{?with_python3}
%py3_install
%endif

# Tests are expecting flaskcli which we don't have packaged.
#%check
#%{__python2} setup.py test
#%if 0%{?with_python3}
#%{__python3} setup.py test
#%endif

%files -n python2-%{modname}
%doc README.md
%license LICENSE
%{python2_sitelib}/flask_migrate/
%{python2_sitelib}/Flask_Migrate-%{version}*

%if 0%{?with_python3}
%files -n python%{python3_pkgversion}-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/flask_migrate/
%{python3_sitelib}/Flask_Migrate-%{version}*
%endif

%changelog
* Sun Apr 15 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.1.1-1
- new version

* Wed Feb 21 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.0.0-8
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 16 2018 Itamar Reis Peixoto <itamar@ispbrasil.com.br> - 2.0.0-7
- make spec file compatible with epel7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jan 18 2017 Ralph Bean <rbean@redhat.com> - 2.0.0-3
- Conditionalize deps for EL7.

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0.0-2
- Rebuild for Python 3.6

* Wed Aug 10 2016 Ralph Bean <rbean@redhat.com> - 2.0.0-1
- Initial package for Fedora!  \ó/
