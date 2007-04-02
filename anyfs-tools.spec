Summary:	anyfs-tools - a unix-like toolset for recovering and converting filesystems
Summary(pl.UTF-8):	anyfs-tools - uniksowy zestaw narzędzi do odzyskiwania i konwersji systemów plików
Name:		anyfs-tools
Version:	0.84.11
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://dl.sourceforge.net/anyfs-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	c5d13e636b0097386f5aebf4c445d627
URL:		http://anyfs-tools.sourceforge.net/
BuildRequires:	e2fsprogs-devel >= 1.38
BuildRequires:	libfuse-devel
BuildRequires:	mjpegtools-devel
BuildRequires:	mpeg2dec-devel
BuildRequires:	xfsprogs-devel
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

%description -l pl.UTF-8
anyfs-tools dostarczają działającego w uniksowym stylu zestawu
narzędzi do odzyskiwania i konwersji systemów plików. W pakiecie
zawarte są następujące narzędzia:

build_it wykorzystuje linuksowe sterowniki systemów plików do
rekurencyjnego odczytu wpisów katalogów w celu uzyskania informacji o
wszystkich i-węzłach systemu plików. Informacje te są następnie
zapisywane do zewnętrznej tabeli i-węzłów.

anysurrect przeszukuje urządzenia blokowe pod kątem określonych
rodzajów plików w oparciu o ich strukturę plików. Inforamcje o każdym
znalezionym rodzaju pliku są także zapisywane do zewnętrznej tabeli
i-węzłów.

reblock zmienia rozmiar bloku systemu plików. Wykorzystuje informacje
o tabeli i-węzłów systemu plików, aby zmienić rozmieszczenie
fragmentów każdego pliku w taki sposób, by były wyrównane do granic
bloków przy nowym ich rozmiarze.

build_e2fs na podstawie zewnętrznej informacji o tabeli i-węzłów
przystępuje do tworzenia systemu plików ext2fs na urządzeniu.

build_xfs na podstawie zewnętrznej informacji o tabeli i-węzłów
przystępuje do tworzenia systemu plików xfs na urządzeniu.

anyconvertfs konwertuje system plików stosując inne narzędzia
anyfs-tools.

Sterownik systemu plików anyfs dla Linuksa pozwala użytkownikowi
podmontować urządzenie przy użyciu zewnętrznych informacji o tabeli
i-węzłów stworzonej przy użyciu polecenia build_it lub anysurrect. Po
podmontowaniu systemu plików użytkownik może wykonywać operacje na
plikach, takie jak usuwanie, przenoszenie, tworzenie dowiązań
symbolicznych i zwykłych czy urządzeń specjalnych oraz zmiana
uprawnień do plików. Wszystkie zmiany są wykonywane na zewnętrznej
tabeli i-węzłów przy odmontowywaniu systemu plików, bez zmiany danych
na urządzeniu blokowym.

%package devel
Summary:	Header files for anyfs-tools
Summary(pl.UTF-8):	Pliki nagłówkowe anyfs-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anyfs-tools.

%description devel -l pl.UTF-8
Pliki nagłówkowe anyfs-tools.

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
