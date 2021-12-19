%global cli_cmd tb

Name: toolboxcutter
Version: 0.2.0
Release: 1%{?dist}
Summary: A script to automate use of toolbox

License: MIT
URL: https://github.com/jcrd/toolboxcutter
Source0: https://github.com/jcrd/toolboxcutter/archive/v0.2.0.tar.gz

BuildArch: noarch

BuildRequires: perl

Requires: bash
Requires: dnf
Requires: toolbox

%global debug_package %{nil}

%description
toolboxcutter automates use of toolbox using per-project Dockerfiles.

%prep
%setup

%build
%make_build PREFIX=/usr

%install
%make_install PREFIX=/usr

%files
%license LICENSE
%doc README.md
/usr/bin/%{cli_cmd}
/usr/share/man/man1/%{cli_cmd}.1.gz

%changelog
* Sun Dec 19 2021 James Reed <james@twiddlingbits.net> - 0.2.0-1
- Release v0.2.0

* Tue May 11 2021 James Reed <james@twiddlingbits.net> - 0.1.1-1
- Release v0.1.1

* Sat Dec 19 2020 James Reed <jcrd@tuta.io> - 0.1.0-1
- Initial package
