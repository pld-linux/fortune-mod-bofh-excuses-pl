Summary:	Collection of Bofh Excuses Fortunes in polish language
Summary(pl):	Zestaw fortunek z wymówkami administratorów (BOFH-ów) po polsku
Name:		fortune-mod-bofh-excuses-pl
Version:	1.0
Release:	1
License:	BSD
Group:		Applications/Games
Requires:	fortune-mod
Source0:	%{name}-%{version}.tgz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
# requires strfile form fortune-mod package (why it's placed in /usr/sbin/ directory?)
BuildRequires:	fortune-mod

%description
Fortune-mod contains the ever-popular fortune program. Want a little
bit of random wisdom revealed to you when you log in? Fortune's your
program. Fun-loving system administrators can add fortune to users'
.login files, so that the users get their dose of wisdom each time
they log in.

This package contains famous BOFH excuses in polish language,
translated by Andrzej 'Greybrow' Korcala (http://greybrow.iq.pl/POPR/)

%description -l pl
Fortune-mod zawiera wci±¿ popularny program fortune ("cytat dnia",
"przepowiednia"). Masz ochotê na odrobinê m±dro¶ci przekazanej Ci
podczas logowania? Program fortune jest dla Ciebie. Administratorzy z
poczuciem humoru mog± dodaæ fortune do plików .login u¿ytkowników tak,
by ka¿dy otrzyma³ swoj± dawkê m±dro¶ci przy logowaniu.

Ten pakiet zawiera s³ynne wymówki BOFH-ów po polsku przet³umaczone
przez Andrzeja 'Greybow' Korcale (http://greybrow.iq.pl/POPR/)

%prep
%setup -q -n bofh-pl
%build
%{_sbindir}/strfile bofh-excuses-pl bofh-excuses-pl.dat

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/games/fortunes

install bofh-excuses-pl* $RPM_BUILD_ROOT%{_datadir}/games/fortunes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/games/fortunes/*
