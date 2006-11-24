Summary:	anyfs-tools - a unix-like toolset for recovering and converting filesystems
Summary(pl):	anyfs-tools - uniksowy zestaw narzêdzi do odzyskiwania i konwersji systemów plików
Name:		anyfs-tools
Version:	0.84.9
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/anyfs-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	27d74d895f630b8f3f74d6f58e16c7a5
URL:		http://anyfs-tools.sourceforge.net/
BuildRequires:	bzip2-devel
BuildRequires:	e2fsprogs-devel >= 1.38
BuildRequires:	mjpegtools-devel
Requires:	xfsprogs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
anyfs-tools provides a unix-like toolset for recovering and converting
filesystems. The following utils are included in the toolset:

build_it uses Linux OS filesystem drivers to recursively read
directory entries in order to obtain information about all of the
filesystem inodes. The information is then saved to an external inode
table.

anysurrect searches block devices for specific file types, based on
their file structure. Information about each found file type is also
saved to an external inode table.

reblock changes the filesystem block size. reblock uses information
from the filesystems inode table to change each files' fragments
placing so that it will align with block boundaries but with a new
block size.

build_e2fs proceeds from external inode table information for building
ext2fs filesystems on device.

build_xfs proceeds from external inode table information for building
xfs filesystems on device.

anyconvertfs converts device filesystem with applying other
anyfs-tools utilities.

The anyfs filesystem driver for Linux allows a user to mount a device
using the external inode table information created by the build_it or
anysurrect commands. Once the filesystem is mounted with the inode
table information the user can perform file operations such as
deleting, moving files, making symbolic and hard links, special files
and changing file access permissions. All changes are applied to the
external inode table on unmounting the filesystem, leaving the data on
the block device unchanged.

%description -l pl
anyfs-tools dostarczaj± dzia³aj±cego w uniksowym stylu zestawu
narzêdzi do odzyskiwania i konwersji systemów plików. W pakiecie
zawarte s± nastêpuj±ce narzêdzia:

build_it wykorzystuje linuksowe sterowniki systemów plików do
rekurencyjnego odczytu wpisów katalogów w celu uzyskania informacji o
wszystkich i-wêz³ach systemu plików. Informacje te s± nastêpnie
zapisywane do zewnêtrznej tabeli i-wêz³ów.

anysurrect przeszukuje urz±dzenia blokowe pod k±tem okre¶lonych
rodzajów plików w oparciu o ich strukturê plików. Inforamcje o ka¿dym
znalezionym rodzaju pliku s± tak¿e zapisywane do zewnêtrznej tabeli
i-wêz³ów.

reblock zmienia rozmiar bloku systemu plików. Wykorzystuje informacje
o tabeli i-wêz³ów systemu plików, aby zmieniæ rozmieszczenie
fragmentów ka¿dego pliku w taki sposób, by by³y wyrównane do granic
bloków przy nowym ich rozmiarze.

build_e2fs na podstawie zewnêtrznej informacji o tabeli i-wêz³ów
przystêpuje do tworzenia systemu plików ext2fs na urz±dzeniu.

build_xfs na podstawie zewnêtrznej informacji o tabeli i-wêz³ów
przystêpuje do tworzenia systemu plików xfs na urz±dzeniu.

anyconvertfs konwertuje system plików stosuj±c inne narzêdzia
anyfs-tools.

Sterownik systemu plików anyfs dla Linuksa pozwala u¿ytkownikowi
podmontowaæ urz±dzenie przy u¿yciu zewnêtrznych informacji o tabeli
i-wêz³ów stworzonej przy u¿yciu polecenia build_it lub anysurrect. Po
podmontowaniu systemu plików u¿ytkownik mo¿e wykonywaæ operacje na
plikach, takie jak usuwanie, przenoszenie, tworzenie dowi±zañ
symbolicznych i zwyk³ych czy urz±dzeñ specjalnych oraz zmiana
uprawnieñ do plików. Wszystkie zmiany s± wykonywane na zewnêtrznej
tabeli i-wêz³ów przy odmontowywaniu systemu plików, bez zmiany danych
na urz±dzeniu blokowym.

%package devel
Summary:	Header files for anyfs-tools
Summary(pl):	Pliki nag³ówkowe anyfs-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anyfs-tools.

%description devel -l pl
Pliki nag³ówkowe anyfs-tools.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README THANKS
%lang(ru) %doc README.ru
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%lang(ru) %{_mandir}/ru/man3/*
%lang(ru) %{_mandir}/ru/man3/*
%lang(ru) %{_mandir}/ru/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/anyfs-tools
