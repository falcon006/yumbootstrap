%define _version 0.0.3
%define _release 1
%define _packager Stanislaw Klekot <dozzie@jarowit.net>
#%define __python /usr/bin/python3
#%define python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: yumbootstrap - chroot installer for Red Hat derivatives
Name: yumbootstrap
Version: %{_version}
Release: %{_release}%{?dist}
Group: Development/Tools
License: GPL v3
Source0: yumbootstrap-%{_version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root
URL: http://dozzie.jarowit.net/trac/wiki/yumbootstrap
BuildArch: noarch
Packager: %{_packager}
Prefix: %{_prefix}
BuildRequires: python-setuptools
BuildRequires: python3-devel
Requires: yum >= 3.0

%description
yumbootstrap is a tool for installing Yum-based distributions (Red Hat,
CentOS, Fedora) in a chroot directory. Idea behind it is stolen from Debian's
debootstrap. 

%prep
%setup -q
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" .

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT"
%{__python} setup.py install --root "$RPM_BUILD_ROOT"
make install-notmodule \
  DESTDIR="$RPM_BUILD_ROOT" \
  BINDIR=%{_sbindir} SYSCONFDIR=%{_sysconfdir}
mkdir -p "$RPM_BUILD_ROOT/%{_docdir}/yumbootstrap-%{_version}"
cp KNOWN_ISSUES.md LICENSE README.md SUITES.md TODO \
   "$RPM_BUILD_ROOT/%{_docdir}/yumbootstrap-%{_version}"


# %clean
# no %clean section


%files
%defattr(-,root,root,-)
%{_sbindir}/yumbootstrap
%{_sysconfdir}/yumbootstrap
#%{_mandir}/man8
%{_docdir}/yumbootstrap-%{_version}
/usr/lib/python3.9/site-packages/*
#%{python3_sitearch}/yumbootstrap
#%{python3_sitearch}/yumbootstrap-*.egg-info


# %changelog
# no %changelog section
