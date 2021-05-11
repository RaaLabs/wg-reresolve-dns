# The name should reflect the name part of the tar.gz archive
Name:           wg-reresolve-dns
# The version should reflect the version part of the tar.gz arcive
Version:        0.1.0
Release:        0
Summary:        Package for reresolving dns if peer domain changes ip address

License:        GPLv2
URL:            https://github.com/RaaLabs/wg-reresolve-dns

# The name of the tar.gz archive as present in the SOURCE folder
Source0:        %{name}-%{version}.tar.gz

Requires:       bash

# options x86_64 or noarch
BuildArch:      x86_64

%description
Package for reresolving dns if peer domain changes ip address

%prep
%setup -q


%build

%install
# Prepare the binary and run script
install -d -m 0755 %{buildroot}/usr/local/wireguard-tools
install -m 0755 wg-reresolve-dns.sh %{buildroot}/usr/local/wireguard-tools/wg-reresolve-dns.sh

# Prepare the systemd files
mkdir -p %{buildroot}/usr/lib/systemd/system/
install -m 0755 wg-reresolve-dns.service %{buildroot}/usr/lib/systemd/system/wg-reresolve-dns.service
install -m 0755 wg-reresolve-dns.timer %{buildroot}/usr/lib/systemd/system/wg-reresolve-dns.timer
mkdir -p %{buildroot}/usr/lib/systemd/system/timers.target.wants
ln -s /usr/lib/systemd/system/wg-reresolve-dns.timer %{buildroot}/usr/lib/systemd/system/timers.target.wants/wg-reresolve-dns.timer

# Prepare a link to the service within clr-service-restart so it will be automatically restarted when updated
mkdir -p %{buildroot}/usr/share/clr-service-restart
ln -sf /usr/lib/systemd/system/wg-reresolve-dns.timer %{buildroot}/usr/share/clr-service-restart/wg-reresolve-dns.timer

%files
# %license LICENSE
/usr/local/wireguard-tools/wg-reresolve-dns.sh
/usr/lib/systemd/system/wg-reresolve-dns.service
/usr/lib/systemd/system/wg-reresolve-dns.timer
/usr/lib/systemd/system/timers.target.wants/wg-reresolve-dns.timer
/usr/share/clr-service-restart/wg-reresolve-dns.timer