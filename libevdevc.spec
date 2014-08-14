%define lib_major 0
%define lib_name %mklibname evdevc %{lib_major}
%define lib_hollow %mklibname hollow %{lib_major}
%define develname %mklibname -d evdevc
%define	debugcflags %nil
%define	_fortify_cflags %nil
# This package is a fork from ChromiumOS

Name:		libevdevc
Version:	1.1
Release:	3
Summary:	Kernel Evdevc Device Wrapper Library from ChromiumOS
Group:		System/Libraries
License:	MIT
URL:		http://www.freedesktop.org/wiki/Software/libevdev
Source0:	http://www.freedesktop.org/software/%{name}/%{name}-%{version}.tar.bz2

%description
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n %{lib_name}
Summary:	Kernel Evdev Device Wrapper Library
Group:		System/Libraries

%description -n %{lib_name}
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n %{lib_hollow}
Summary:	Kernel Evdev Device Wrapper Library
Group:		System/Libraries

%description -n %{lib_hollow}
%{name} is a library to wrap kernel evdev devices and provide a proper API
to interact with those devices.

%package -n %develname
Summary:	Kernel Evdev Device Wrapper Library Development Package
Provides:	%{name}-devel = %{version}-%{release}
Provides:	evdevc-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}

%description -n %develname
Kernel Evdev Device Wrapper Library Development Package.

%prep
%setup -q

%build
%setup_compile_flags
sed -i 's!LIBDIR ?= /usr/lib!LIBDIR = %{_libdir}!g' Makefile
%make

%install
%makeinstall_std

%files -n %{lib_name}
%{_libdir}/libevdevc.so.%{lib_major}*

%files -n %{lib_hollow}
%{_libdir}/libevdevc_hollow.so.%{lib_major}

%files -n %{develname}
%{_includedir}/libevdevc/
%{_libdir}/libevdevc.so
%{_libdir}/libevdevc_hollow.so
