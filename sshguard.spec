%define prel beta2

Summary:	Protect hosts from brute force attacks against ssh
Name:		sshguard
Version:	1.0
Release:	%mkrel 0.%{prel}.2
License:	GPL
Group:		Networking/Remote access
Url:		http://sshguard.sourceforge.net
Source0:	http://downloads.sourceforge.net/sshguard/%{name}-%{version}%{prel}.tar.bz2
Requires:	iptables
Requires:	sshd
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Sshguard protects networked hosts from brute force attacks 
against ssh servers. It detects such attacks and blocks the 
attacker's address with a firewall rule.

%prep
%setup -qn %{name}-%{version}%{prel}

%build
%configure2_5x \
	--with-firewall=iptables

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_sbindir}/%{name}
%{_mandir}/man8/%{name}*
