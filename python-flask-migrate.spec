%if 0%{?fedora}
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
Version:            2.0.0
Release:            5%{?dist}
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
BuildRequires:      python-flask
BuildRequires:      python-alembic
BuildRequires:      python-flask-script

Requires:           python-flask
Requires:           python-alembic
Requires:           python-flask-script

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
%package -n python3-%{modname}
Summary:            SQLAlchemy database migrations for Flask applications using Alembic
%{?python_provide:%python_provide python3-%{modname}}

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools
BuildRequires:      python3-flask
BuildRequires:      python3-flask-sqlalchemy
BuildRequires:      python3-alembic
BuildRequires:      python3-flask-script
Requires:           python3-flask
Requires:           python3-flask-sqlalchemy
Requires:           python3-alembic
Requires:           python3-flask-script

%description -n python3-%{modname}
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
%files -n python3-%{modname}
%doc README.md
%license LICENSE
%{python3_sitelib}/flask_migrate/
%{python3_sitelib}/Flask_Migrate-%{version}*
%endif

%changelog
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
