Summary:	GNU cpio archiving program
Name:		cpio
Version:	2.11
Release:	2
License:	GPL v3+
Group:		Applications/Archiving
Source0:	ftp://ftp.gnu.org/gnu/cpio/%{name}-%{version}.tar.bz2
# Source0-md5:	20fc912915c629e809f80b96b2e75d7d
Patch0:		%{name}-ifdef.patch
URL:		http://www.gnu.org/software/cpio/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU cpio copies files into or out of a cpio or tar archive. Archives
are files which contain a collection of other files plus information
about them, such as their file name, owner, timestamps, and access
permissions. The archive can be another file on the disk, a magnetic
tape, or a pipe. GNU cpio supports the following archive formats:
binary, old ASCII, new ASCII, crc, HPUX binary, HPUX old ASCII, old
tar and POSIX.1 tar. By default, cpio creates binary format archives,
so that they are compatible with older cpio programs. When it is
extracting files from archives, cpio automatically recognizes which
kind of archive it is reading and can read archives created on
machines with a different byte-order.

%prep
%setup -q
%patch0 -p1

sed -i "/gets is a security hole/d" gnu/stdio.in.h

%build
%if 0
%{__gettextize}
%{__aclocal} -I m4 -I am
%{__autoconf}
%{__autoheader}
%{__automake}
%endif
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /usr/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/cpio
%{_infodir}/cpio.info*
%{_mandir}/man1/cpio.1*

