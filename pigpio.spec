Name:           pigpio
Version:        78
Release:        1%{?dist}
Summary:        library for the Raspberry which allows control of the General Purpose Input Outputs (GPIO)

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
Summary:        Development files for Raspberry General Purpose Input Outputs (GPIO) library
Requires:       %{name} = %{version}-%{release}

%description devel
pigpio is a C library for the Raspberry which allows control of
the General Purpose Input Outputs (GPIO).

Contains development files for C language clients of the library.

%prep
%autosetup


%build
# do not install manuals into /usr/man
sed -e 's|DESTINATION man/|DESTINATION ${SHARE_INSTALL_PREFIX}/man/|' \
    -i CMakeLists.txt
%cmake
%cmake_build


%install
%cmake_install
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


%changelog
* Sun Jan 31 2021 Petr Menšík <pemensik@redhat.com>
- initial build
