Summary:	Software dedicated to viewing and analyzing antennas
Name:		qantenna
Version:	0.3.0
Release:	1
License:	GPLv2+
Group:		Sciences/Physics
Url:		http://qantenna.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/qantenna/qantenna/%{version}/%{name}-%{version}.orig.tar.xz
BuildRequires:	qt5-linguist
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
Requires:	nec2++

%description
QAntenna is a FLOSS software dedicated to viewing and analyzing
antennas and their radiation patterns. It provides the user with a
3D view of the models, capable of zooming, rotating, and more to come.

%files
%doc README AUTHORS ChangeLog COPYING
%{_bindir}/qantenna

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%qmake_qt5 PREFIX=/usr qantenna.pro

%make RPM_OPT_FLAGS="%{optflags}"

%install
make INSTALL_ROOT=%{buildroot} install


