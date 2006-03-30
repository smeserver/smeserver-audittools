Summary: SME Server auditing tools
%define name smeserver-audittools
Name: %{name}
%define version 0.0.1
%define release 10
Version: %{version}
Release: %{release}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-audittools-0.0.1-CustomTemplates.patch
Patch1: smeserver-audittools-0.0.1-TemplateOwners.patch
Patch2: smeserver-audittools-0.0.1-DisplayCommands.patch
Patch3: smeserver-audittools-0.0.1-CheckModified.patch
Patch4: smeserver-audittools-0.0.1-RemoveVerbose.patch
Patch5: smeserver-audittools-0.0.1-Users2Domains.patch
Patch6: P/smeserver-audittools-0.0.1-subdirectory.patch
Patch7: P/smeserver-audittools-0.0.1-pseudonyms.patch
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
* Thu Mar 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-10
- Add psedonyms audit [SME: 762]

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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

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
