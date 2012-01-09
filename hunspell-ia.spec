Name: hunspell-ia
Summary: Interlingua hunspell dictionaries
%define upstreamid 20050226
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Group: Applications/Text
Source: http://download.savannah.gnu.org/releases/interlingua/ia_myspell.zip
URL: http://wiki.services.openoffice.org/wiki/Dictionaries#Interlingua_.28x-register.29
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Interlingua hunspell dictionaries.

%prep
%setup -q -c

%build
tr -d '\r' < README_ia.txt > README_ia.txt.new
touch -r README_ia.txt README_ia.txt.new
mv -f README_ia.txt.new README_ia.txt

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p ia.* $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_ia.txt
%{_datadir}/myspell/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20050226-3.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050226-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20050226-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 07 2008 Caolan McNamara <caolanm@redhat.com> - 0.20050226-1
- initial version
