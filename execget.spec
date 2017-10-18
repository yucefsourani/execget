Name:           execget
Version:        0.1
Release:        1%{?dist}
Summary:        Simple Tool To Get Exec Command From Desktop Entry
BuildArch:	noarch
License:        GPLv3
URL:            https://arfedora.blogspot.com
Source0:        https://github.com/yucefsourani/execget/archive/%{version}.tar.gz
Requires:       python3-gobject
Requires:       pygobject3   

%description
Simple Tool To Get Exec Command From Desktop Entry.

%prep
%autosetup



%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps

install -pDm0755 ./execget %{buildroot}%{_bindir}
cp ./org.github.yucefsourani.execget.desktop %{buildroot}%{_datadir}/applications
cp ./org.github.yucefsourani.execget.png %{buildroot}%{_datadir}/pixmaps


%files
%license LICENSE
%doc README.md
%{_bindir}/execget
%{_datadir}/applications/org.github.yucefsourani.execget.desktop
%{_datadir}/pixmaps/org.github.yucefsourani.execget.png


%changelog
* Wed Oct 18 2017 yucefsourani <youssef.m.sourani@gmail.com> 0.1-1
- Initial For Fedora 26
