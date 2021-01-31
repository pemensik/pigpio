# Python version includes for some reason 1.%%version
%global pyver_prefix 1.

Name:           pigpio
Version:        78
Release:        1%{?dist}
Summary:        Raspberry Pi General Purpose Input Outputs (GPIO) library

License:        Unlicense
URL:            http://abyz.me.uk/rpi/pigpio/
Source0:        https://github.com/joan2937/pigpio/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/joan2937/pigpio/pull/428
Patch1:         pigpio-lib-suffix.patch
BuildRequires:  cmake gcc make
BuildRequires:  sed
BuildRequires:  python3-devel
#Requires:       

%description
pigpio is a C library for the Raspberry which allows control of
the General Purpose Input Outputs (GPIO).

%package devel
Summary:        Raspberry Pi General Purpose Input Outputs (GPIO) development files
Requires:       %{name} = %{version}-%{release}

%description devel
pigpio is a C library for the Raspberry which allows control of
the General Purpose Input Outputs (GPIO).

Contains development files for C language clients of the library.

%package -n python3-%{name}
Summary:        Raspberry Pi GPIO module
Requires:       %{name} = %{version}-%{release}
# Borrowed from python-pigpio package
%{?python_provide:%python_provide python3-%{name}}

%description -n python3-%{name}

Raspberry Pi Python module to access the pigpio daemon.


%prep
%autosetup


%build
# do not install manuals into /usr/man
sed -e 's|DESTINATION man/|DESTINATION ${SHARE_INSTALL_PREFIX}/man/|' \
    -e 's|QUIET||' \
    -i CMakeLists.txt
%cmake
%cmake_build
%py3_build

%install
%cmake_install
%py3_install
# Not sure how they would be useful. Do not package them yet.
rm -rf  %{buildroot}%{_usr}/lib/cmake/pigpio

%files
%license UNLICENCE
%doc README.md SUPPORT.md
%{_bindir}/pigpiod
%{_bindir}/pig2vcd
%{_bindir}/pigs
# TODO: should use soversion outside devel
%{_libdir}/libpigpio*.so
%{_mandir}/man1/pig*.1*
%{_mandir}/man3/pig*.3*

%files devel
%{_includedir}/pigpio*.h

%files -n python3-%{name}
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{name}.py
%{python3_sitelib}/%{name}-%{?pyver_prefix}%{version}-py%{python3_version}.egg-info

%changelog
* Sun Jan 31 2021 Petr Menšík <pemensik@redhat.com>
- initial build
