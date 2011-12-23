# TODO
# - tests fail, likely need dbus server or sth
#
# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define		pdir	Desktop
%define		pnam	Notify
%include	/usr/lib/rpm/macros.perl
Summary:	Desktop::Notify - Communicate with the Desktop Notifications framework
Name:		perl-Desktop-Notify
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SA/SACAVILIA/Desktop-Notify-%{version}.tar.gz
# Source0-md5:	8847fe21dcd8572fec8c4e5f082aa24d
URL:		http://search.cpan.org/dist/Desktop-Notify/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-Net-DBus
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a Perl interface to the Desktop Notifications
framework.

The framework allows applications to display pop-up notifications on
an X desktop. This is implemented with two components: a daemon that
displays the notifications, and a client library used by applications
to send notifications to the daemon. These components communicate
through the DBus message bus protocol.

More information is available from
<http://trac.galago-project.org/wiki/DesktopNotifications>

This module serves the same purpose as libnotify, in an
object-oriented Perl interface. It is not, however, an interface to
libnotify itself, but a separate implementation of the specification
using Net::DBus.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Desktop
%{perl_vendorlib}/Desktop/*.pm
%{perl_vendorlib}/Desktop/Notify
%{_mandir}/man3/*
