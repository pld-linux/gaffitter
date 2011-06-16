Summary:	gaffitter - Genetic Algorithm File Fitter
Name:		gaffitter
Version:	0.6.0
Release:	1
License:	GPL
Group:		Tools
Source0:	http://downloads.sourceforge.net/gaffitter/%{name}-%{version}.tar.bz2
# Source0-md5:	a4a0fa0b3eeeaf49624d2e1b78de3cff
URL:		http://gaffitter.sourceforge.net//
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Genetic Algorithm File Fitter, or just GAFFitter, is a command-line
software written in C++ that arranges--via a genetic algorithm--an
input list of items or files/directories into volumes of a certain
capacity (target), such as CD or DVD, in a way that the total wastage
is minimized.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
    DESTDIR=$RPM_BUILD_ROOT \
    prefix=/usr

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/gaffitter
