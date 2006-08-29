Summary:	anyfs-tools provides a unix-like toolset for recovering and converting filesystems
Summary(pl):	anyfs
Name:		anyfs-tools
Version:	0.84.6
Release:	0.1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/anyfs-tools/%{name}-%{version}.tar.bz2
# Source0-md5:	ba763fe3b1736dfeb82e39e27ebc2797
URL:		-
#BuildRequires:	-
Requires:	xfstools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
anyfs-tools provides a unix-like toolset for recovering and converting
filesystems. The following utils are included in the toolset:

build_it uses LINUX OS filesystem drivers to recursively read
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

%package devel
Summary:	Header files for anyfs-tools library
Summary(pl):	Pliki nag³ówkowe biblioteki anyfs-tools
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for anyfs-toolslibrary.

%description devel -l pl
Pliki nag³ówkowe biblioteki anyfs-tools.

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
%doc README THANKS README.ru
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{_mandir}/ru/man3/*
%{_mandir}/ru/man3/*
%{_mandir}/ru/man5/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/anyfs-tools/*
