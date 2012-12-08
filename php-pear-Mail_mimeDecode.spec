%define		_class		Mail
%define		_subclass	mimeDecode
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.5.5
Release:	%mkrel 2
Summary:	Provides a class to decode mime messages
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Provides a class to deal with the decoding and interpreting of mime messages.
This package used to be part of the Mail_Mime package, but has been split off.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.5-2mdv2011.0
+ Revision: 667623
- mass rebuild

* Sun Dec 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.5-1mdv2011.0
+ Revision: 622932
- update to new version 1.5.5

* Tue Sep 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.4-1mdv2011.0
+ Revision: 578195
- update to new version 1.5.4

* Thu Sep 09 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.3-1mdv2011.0
+ Revision: 576924
- update to new version 1.5.3

* Tue Dec 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.1-1mdv2010.1
+ Revision: 478815
- update to new version 1.5.1

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-2mdv2010.1
+ Revision: 470148
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-1mdv2010.0
+ Revision: 450224
- import php-pear-Mail_mimeDecode


* Fri Sep 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.0-1mdv2010.0
- split out from php-pear package
