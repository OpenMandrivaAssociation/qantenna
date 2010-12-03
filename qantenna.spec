%define name	qantenna
%define version	0.2.2
%define rel	1

Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
Summary:	QAntenna is softwareto viewing and analizing antennas
Group:		Sciences/Physics 
License:	GPLv2
URL:		http://qantenna.sourceforge.net/
Source:		http://sourceforge.net/projects/qantenna/files/qantenna/0.2.2/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	libgc-devel
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-devel
Requires:	nec2++
Requires:	libmesagl
Requires:	libatlas


%description
QAntenna is a FLOSS software dedicated to viewing and analizing 
antennas and their radiation patterns. It provides the user with a 
3D view of the models, capable of zooming, rotating, and more to come. 

%prep
%setup -q

%build
%qmake_qt4  PREFIX=/usr qantenna.pro

%make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

rm -rf %{buildroot}
make INSTALL_ROOT=$RPM_BUILD_ROOT install




%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README  AUTHORS ChangeLog COPYING INSTALL
%{_bindir}/qantenna
%{_datadir}/qantenna/qantenna_da.qm
%{_datadir}/qantenna/qantenna_de.qm
%{_datadir}/qantenna/qantenna_es.qm
%{_datadir}/qantenna/qantenna_fr.qm
%{_datadir}/qantenna/qantenna_it.qm
%{_datadir}/qantenna/qantenna_nl.qm
%{_datadir}/qantenna/qantenna_pl.qm
%{_datadir}/qantenna/qantenna_ru.qm
%{_datadir}/qantenna/qantenna_sv.qm



