%global cli_cmd tb

Name: {{{ git_cwd_name name="toolboxcutter" }}}
Version: {{{ git_cwd_version lead="$(git tag | sed -n 's/^v//p' | sort --version-sort -r | head -n1)" }}}
Release: 1%{?dist}
Summary: A script to automate use of toolbox

License: MIT
URL: https://github.com/jcrd/toolboxcutter
VCS: {{{ git_cwd_vcs }}}
Source0: {{{ git_cwd_pack }}}

BuildArch: noarch

BuildRequires: perl

Requires: bash
Requires: dnf
Requires: toolbox

%global debug_package %{nil}

%description
toolboxcutter automates use of toolbox using per-project Dockerfiles.

%prep
{{{ git_cwd_setup_macro }}}

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
{{{ git_cwd_changelog }}}
