Summary:	A tool for SQL server injection and takeover
Name:		sqlninja
Version:	0.2.5
Release:	1
License:	GPL v2
Group:		Applications/Databases
URL:		http://sqlninja.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sqlninja/%{name}-%{version}.tgz
# Source0-md5:	95acfd9c5bc2305f239596c613d4ffc7
Patch0:		%{name}-pathmodifier.patch
Requires:	perl-IO-Socket-SSL
Requires:	perl-Net-DNS-Nameserver
Requires:	perl-Net-Pcap
Requires:	perl-Net-RawIP
Requires:	perl-NetPacket
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sqlninja is a tool targeted to exploit SQL Injection vulnerabilities
on a web application that uses Microsoft SQL Server as its back-end.
Its main goal is to provide remote access to vulnerable DB server.

%prep
%setup -q
%patch0

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_datadir}/%{name}/apps}
cp -a %{name}.conf $RPM_BUILD_ROOT%{_sysconfdir}
install -p %{name} $RPM_BUILD_ROOT%{_sbindir}
# FIXME: Including binaries
install -p apps/*.exe $RPM_BUILD_ROOT%{_datadir}/%{name}/apps

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc LICENSE ChangeLog README sqlninja-howto.html
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_sbindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/apps/*.exe
