# $Id: smeserver-audittools.spec,v 1.12 2009/11/07 18:54:32 snetram Exp $

Summary: SME Server auditing tools
%define name smeserver-audittools
Name: %{name}
%define version 1.2.0
%define release 7
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System Environment/Base
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-audittools-1.2.0-fix-yum-invocation.patch
Patch1: smeserver-audittools-1.2.0-fix-dotted-usernames-and-groups.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: perl(RPM2)
BuildRequires: e-smith-devtools

%description
Tools for consistency audits of SME Servers. Useful for determining local
modifications prior to upgrades.

%changelog
* Sat Nov 7 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-7.sme
- Fix regular expression to actually replace the colon with a dot [SME: 5572]

* Sat Nov 7 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-6.sme
- Undo changes made in 1.2.0-5 [SME: 5572]
- Properly fix output for usernames and groups containing a dot [SME: 5572]

* Fri Nov 6 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-5.sme
- Remove comment lines from output of aliases [SME: 5572]

* Thu Nov 5 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-4.sme
- Remove the leading path for yum in newrpms [SME: 5562]

* Sat Oct 24 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-3.sme
- Revert changes made in [SME: 5417]

* Sat Aug 1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.2.0-2.sme
- Sort the output of the repositories audittool alphabetically [SME: 5417]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 1.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Thu Aug 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 0.0.2-7
- New tool repositories, lists status of configured repositories [SME: 4438]

* Wed Jan 09 2008 Stephen Noble <support@dungog.net> 0.0.2-6
- New tool events, lists modified events [SME: 3419]

* Sat Jun 16 2007 Stephen Noble <support@dungog.net> 0.0.2-5
- New tool newrpms, lists installed rpms not in standard repos [SME: 1206]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Wed Apr 12 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.2-03
- Change status output for templates audit. In particular 
  OK -> OWNED_BY_RPM. This means that custom templates will appear
  as "OWNED_BY_RPM, OVERRIDE" rather than "OK, OVERRIDE". template
  fragments should not be placed in templates-custom via RPMs [SME: 792]

* Thu Mar 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.2-02
- Fix output from pseudonyms audit [SME: 792]
- Display commands on stdout and warnings on stderr [SME: 792]
- Complain about pseudonyms with @, but no domain [SME: 792]
- Complain if virtualdomains pseudonym doesn't match accounts db [SME: 792]

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
%patch0 -p1
%patch1 -p1

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
