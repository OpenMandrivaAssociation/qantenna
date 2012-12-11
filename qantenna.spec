%define name	qantenna
%define version	0.2.3
%define rel	1

Name:		%{name}
Version:	%{version}
%if %{mdvver} >= 201100
Release:	%{rel}
%else
Release:	%mkrel %{rel}
%endif
Summary:	Software dedicated to viewing and analyzing antennas
Group:		Sciences/Physics 
License:	GPLv2
URL:		http://qantenna.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/qantenna/qantenna/%{version}/%{name}-%{version}.tar.bz2
Patch0:		qantenna-0.2.3-mdv-link.patch
BuildRequires:	pkgconfig(bdw-gc)
BuildRequires:	qt4-devel
BuildRequires:	mesaglu-devel
Requires:	nec2++
Requires:	libatlas


%description
QAntenna is a FLOSS software dedicated to viewing and analizing 
antennas and their radiation patterns. It provides the user with a 
3D view of the models, capable of zooming, rotating, and more to come. 

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4  PREFIX=/usr qantenna.pro

%make RPM_OPT_FLAGS="%{optflags}"

%install
make INSTALL_ROOT=%{buildroot} install
%if %{mdvver} >= 201200
%find_lang %{name} --with-qt
%endif

%if %{mdvver} <= 201100
%files
%lang(da) /usr/share/qantenna/qantenna_da.qm
%lang(de) /usr/share/qantenna/qantenna_de.qm
%lang(es) /usr/share/qantenna/qantenna_es.qm
%lang(fr) /usr/share/qantenna/qantenna_fr.qm
%lang(it) /usr/share/qantenna/qantenna_it.qm
%lang(nl) /usr/share/qantenna/qantenna_nl.qm
%lang(pl) /usr/share/qantenna/qantenna_pl.qm
%lang(ru) /usr/share/qantenna/qantenna_ru.qm
%lang(sv) /usr/share/qantenna/qantenna_sv.qm
%else
%files -f %{name}.lang
%endif
%doc README AUTHORS ChangeLog COPYING
%{_bindir}/qantenna


%changelog
* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.3-1mdv2011.0
+ Revision: 770399
+ rebuild (emptylog)

* Wed Feb 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 0.2.3-1
+ Revision: 770365
- update to 0.2.3

* Fri Dec 03 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.2.2-1mdv2011.0
+ Revision: 605788
- import qantenna

