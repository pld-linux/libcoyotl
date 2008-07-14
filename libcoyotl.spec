Summary:	The Coyotl library defies easy classification -- much like it's namesake
Name:		libcoyotl
Version:	3.1.0
Release:	1
License:	GPL
Group:		Libraries
URL:		http://www.coyotegulch.com/products/libcoyotl/index.html
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Coyotl library defies easy classification -- much like it's
namesake. It collects several C++ tools that have proven useful in
many of my programs, but which aren't "big enough" to warrant an
individual library.

%package devel
Summary:	libcoyotl headers and documentation
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libcoyotl libraries headers and documentation

%package static
Summary:	libcoyotl static libraries
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
libcoyotl static libraries

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/lib*.la
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%dir %{_docdir}/%{name}/api/
%{_docdir}/%{name}/api/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a