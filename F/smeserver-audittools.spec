Summary: SME Server auditing tools
%define name smeserver-audittools
Name: %{name}
%define version 0.0.1
%define release 02
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Packager: Gordon Rowell <gordonr@gormand.com.au>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: perl(RPM2)
BuildRequires: e-smith-devtools

%description
Tools for consistency audits of SME Servers. Useful for determining local
modifications prior to upgrades.

%changelog
* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-02
- Add dependency on perl(RPM2)

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-01
- Initial version [SME: 762]

%prep
%setup

%build

%pre

%post

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
  > %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
