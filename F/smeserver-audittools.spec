Summary: SME Server auditing tools
%define name smeserver-audittools
Name: %{name}
%define version 0.0.2
%define release 01
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
* Thu Mar 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.2-01
- Roll new tarball with patches to 0.0.1-10 [SME: 792]

* Thu Mar 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-10
- Add pseudonyms audit [SME: 762]

* Thu Mar 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-09
- Moved all tools into /sbin/e-smith/audittools to reduce clutter
  and make it easier to run all of them [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-08
- audit-users2domains - What email address have been used? [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-07
- Remove verbose option to rpm_status - not used [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-06
- Determine how many RPMs own a template and whether it has been
  modified since the install of the RPM [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-05
- Only display commands required for conversion from virtualdomains
  hacks to user@domain pseudonyms. These are audit tools - changing
  the system should be a separate task [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-04
- Examine custom templates:
  - Are they owned by an RPM?
  - Are they an override or an addition?
- Examine templates
  - Are they owned by an RPM?
  - TODO: Have they been modified since the install? [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-03
- First cut at custom template audit [SME: 762]

* Thu Mar 23 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-02
- Add dependency on perl(RPM2) [SME: 762]

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
  --file /sbin/e-smith/audittools/ 'attr(0554,root,root)' \
  > %{name}-%{version}-%{release}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
