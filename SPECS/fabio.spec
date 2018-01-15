## package settings
%define fabio_user     fabio
%define fabio_group    %{fabio_user}
%define fabio_confdir  %{_sysconfdir}/%{name}
%define fabio_gover    1.9.2
%ifarch %ix86
%define fabio_build linux_386
%endif
%ifarch x86_64 amd64
%define fabio_build linux_amd64
%endif
%define debug_package  %{nil}

Name:           fabio
Version:        1.5.6
Release:        0%{?dist}
Summary:        Consul Load-Balancing made simple.

Group:          System Environment/Daemons
License:        MIT License
URL:            https://fabiolb.net

Source0:        https://github.com/fabiolb/%{name}/releases/download/v%{version}/%{name}-%{version}-go%{fabio_gover}-%{fabio_build}
Source1:        https://github.com/fabiolb/%{name}/blob/v%{version}/%{name}.properties
Source2:        %{name}.service
Source3:        %{name}.sysconfig

BuildRequires:  systemd-units

Requires(pre):      shadow-utils
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd

%description
Fabio is an HTTP and TCP reverse proxy that configures itself with data from Consul.

%package    config
Summary:    Configuration files for %{name}
Group:      System Environment/Daemons
Requires:   fabio

%description config
Example configuration for %{name}.

%prep
cp -f %{SOURCE0} %{name}

%build

%install

## sytem files
%{__install} -p -D -m 0640 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service
%{__install} -p -D -m 0640 %{SOURCE3} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

## sample config
%{__install} -d -m 0750 %{buildroot}%{fabio_confdir}
%{__install} -p -D -m 0640 %{SOURCE1} %{buildroot}%{fabio_confdir}/%{name}.properties

## main binary
%{__install} -p -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}

%pre
## add required user and group if needed
getent group %{fabio_group} >/dev/null || \
	groupadd -r %{fabio_group}
getent passwd %{fabui_user} >/dev/null || \
	useradd -r -g %{fabio_user} -d /nonexistent \
	-s /sbin/nologin -c %{name} %{fabio_user}
exit 0

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%defattr(-,root,root,-)
%{_unitdir}/%{name}.service
%{_bindir}/%{name}

%files config
%defattr(0644,root,root,0755)
%config(noreplace) %{fabio_confdir}/%{name}.properties
%config(noreplace) %{_sysconfdir}/sysconfig/%{name}

%changelog