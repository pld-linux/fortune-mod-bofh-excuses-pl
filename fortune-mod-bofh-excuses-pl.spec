Summary:	Collection of Bofh Excuses Fortunes in polish language
Summary(pl.UTF-8):	Zestaw fortunek z wymówkami administratorów (BOFH-ów) po polsku
Name:		fortune-mod-bofh-excuses-pl
Version:	1.0
Release:	2
License:	BSD
Group:		Applications/Games
Requires:	fortune-mod
Source0:	%{name}-%{version}.tgz
# Source0-md5:	effccf2cfaa7846f5c1e4bedae892a00
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	fortune-mod >= 1.0-13
BuildArch:	noarch

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

This package contains famous BOFH excuses in polish language,
translated by Andrzej 'Greybrow' Korcala (http://greybrow.iq.pl/POPR/)

%description -l pl.UTF-8
Fortune-mod zawiera wciąż popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotę na odrobinę mądrości przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mogą dodać fortune do plików .login użytkowników tak,
by każdy otrzymał swoją dawkę mądrości przy logowaniu.

Ten pakiet zawiera słynne wymówki BOFH-ów po polsku przetłumaczone
przez Andrzeja 'Greybow' Korcale (http://greybrow.iq.pl/POPR/)

%prep
%setup -q -n bofh-pl
%build
strfile bofh-excuses-pl bofh-excuses-pl.dat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install bofh-excuses-pl* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
