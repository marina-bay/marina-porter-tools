Name:	    marina-porter-tools
Summary:    Extra debugging tools and configs for porting
Version:    1
Release:    1
Group:      Configs
License:    GPLv2

%description
Extra debugging tools and configs for porting

%prep

%build

%install
mkdir -p %{buildroot}/
cp -r sparse/* %{buildroot}/

%clean

%files
%defattr(-,root,root,-)
%config /etc/systemd/journald.conf.d/journald-porting.conf
