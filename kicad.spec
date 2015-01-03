Name:           kicad
Version:        2014.03.13
Release:        11.rev4744%{?dist}
Summary:        Electronic schematic diagrams and printed circuit board artwork
Summary(fr):    Saisie de schéma électronique et routage de circuit imprimé

Group:          Applications/Engineering
License:        GPLv2+
URL:            http://www.kicad-pcb.org
# URL2:         https://launchpad.net/kicad
# URL3:         http://orson.net.pl/pub/kicad/
# Additional librairies from Walter Lain
# URL4:         http://smisioto.no-ip.org/elettronica/kicad/kicad-en.htm

# Source files created with the following scripts ...
#   kicad-clone.sh ... clone BZR repositories of main, libraries, doc
#   kicad-update.sh ... update BZR repositories
#   kicad-export.sh ... export BZR repositories and create tarballs
#   kicad-walter-libs.sh ... download, unpack and prepare tarball with walter libs

Source:         %{name}-%{version}.tar.xz
Source1:        %{name}-doc-%{version}.tar.xz
Source2:        %{name}-libraries-%{version}.tar.xz
Source3:        %{name}-footprints-%{version}.tar.xz
Source7:        Epcos-MKT-1.0.tar.bz2
Source8:        %{name}-walter-libraries-%{version}.tar.xz

Patch0:         pcb_calculator-desktop-fix.patch
Patch1:         kicad-2014.03.13-nostrip.patch
Patch2:         kicad-2014.03.13-fp-lib.patch
Patch3:         kicad-2014.03.13-freerouting.patch
Patch4:         kicad-2014.03.13-boost-context.patch

BuildRequires:  desktop-file-utils
BuildRequires:  wxGTK-devel
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  glew-devel

Requires:       electronics-menu
Requires:       freerouting

%description
KiCad is an EDA software to design electronic schematic
diagrams and printed circuit board artwork up to 16 layers.
KiCad is a set of four softwares and a project manager:
- KiCad: project manager
- Eeschema: schematic entry
- Pcbnew: board editor
- Cvpcb: footprint selector for components used in the circuit design
- Gerbview: GERBER viewer (photoplotter documents)

%description -l fr
KiCad est un logiciel open source (GPL) pour la création de schémas
électroniques et le tracé de circuits imprimés jusqu'à 16 couches.
KiCad est un ensemble de quatres logiciels et un gestionnaire de projet :
- KiCad : gestionnaire de projet.
- Eeschema : saisie de schémas
- Pcbnew : éditeur de circuits imprimés
- Cvpcb : sélecteur d'empreintes pour les composants utilisés dans le circuit
- Gerbview : visualisateur GERBER (documents pour phototraçage)


%package        doc
Summary:        Documentation for KiCad
Summary(fr):    Documentations pour KiCad en anglais
Group:          Documentation
License:        GPLv2+
BuildArch:      noarch

%description    doc
Documentation and tutorials for KiCad in English.


%package        doc-de
Summary:        Documentation for KiCad in German
Summary(fr):    Documentations pour KiCad en allemand
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-de
Documentation and tutorials for KiCad in German


%package        doc-es
Summary:        Documentation for KiCad in Spanish
Summary(fr):    Documentations pour KiCad en espagnol
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-es
Documentation and tutorials for KiCad in Spanish


%package        doc-fr
Summary:        Documentation for KiCad in French
Summary(fr):    Documentations pour KiCad en français
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-fr
Documentation and tutorials for KiCad in French


%package        doc-hu
Summary:        Documentation for KiCad in Hungarian
Summary(fr):    Documentations pour KiCad en hongrois
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-hu
Documentation and tutorials for KiCad in Hungarian


%package        doc-it
Summary:        Documentation for KiCad in Italian
Summary(fr):    Documentations pour KiCad en italien
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-it
Documentation and tutorials for KiCad in Italian


%package        doc-ja
Summary:        Documentation for KiCad in Japanese
Summary(fr):    Documentations pour KiCad en japonais
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch
%description    doc-ja
Documentation and tutorials for KiCad in Japanese


%package        doc-pl
Summary:        Documentation for KiCad in Polish
Summary(fr):    Documentations pour KiCad en polonais
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-pl
Documentation and tutorials for KiCad in Polish


%package        doc-pt
Summary:        Documentation for KiCad in Portuguese
Summary(fr):    Documentations pour KiCad en portugais
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-pt
Documentation and tutorials for KiCad in Portuguese


%package        doc-ru
Summary:        Documentation for KiCad in Russian
Summary(fr):    Documentations pour KiCad en russe
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-ru
Documentation and tutorials for KiCad in Russian


%package        doc-zh_CN
Summary:        Documentation for KiCad in Chinese
Summary(fr):    Documentations pour KiCad en chinois
Group:          Documentation
Requires:       %{name}-doc = %{version}-%{release}
BuildArch:      noarch

%description    doc-zh_CN
Documentation and tutorials for KiCad in Chinese


%prep
%setup -q -a 1 -a 2 -a 3 -a 7 -a 8

%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p0

cd %{name}-libraries-%{version}
%patch2 -p1
cd ..

#kicad-doc.noarch: W: file-not-utf8 /usr/share/doc/kicad/AUTHORS.txt
iconv -f iso8859-1 -t utf-8 AUTHORS.txt > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS.txt


#multilibs
%ifarch x86_64 sparc64 ppc64 amd64 s390x
%{__sed} -i "s|KICAD_PLUGINS lib/kicad/plugins|KICAD_PLUGINS lib64/kicad/plugins|" CMakeLists.txt
#%{__sed} -i "s|/usr/lib/kicad|/usr/lib64/kicad|" %{SOURCE3}
%endif


%build

# Add Epcos library
cd Epcos-MKT-1.0
cp -pR library ../%{name}-libraries-%{version}/
cp -pR modules ../%{name}-libraries-%{version}/
cd ..

# Add Walter libraries
cd %{name}-walter-libraries-%{version}
cp -pR library ../%{name}-libraries-%{version}/
cp -pR modules ../%{name}-libraries-%{version}/
cd ..

#
# Symbols libraries
#
pushd %{name}-libraries-%{version}/
%cmake -DKICAD_STABLE_VERSION=OFF
%{__make} -j1 VERBOSE=1
popd


#
# Core components
#
%cmake -DKICAD_STABLE_VERSION=OFF -DKICAD_SKIP_BOOST=ON
%{__make} -j1 VERBOSE=1


%install
%{__rm} -rf %{buildroot}

%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install


# install localization
cd %{name}-doc-%{version}/internat
for dir in bg ca cs de es fr hu it ko nl pl pt ru sl sv zh_CN
do
  install -m 644 -D ${dir}/%{name}.mo %{buildroot}%{_datadir}/locale/${dir}/LC_MESSAGES/%{name}.mo
done
cd ../..


# install desktop
for desktopfile in %{buildroot}%{_datadir}/applications/*.desktop ; do
  desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  --remove-category Development              \
  --delete-original                          \
  ${desktopfile}
done

#
# Symbols libraries
#
pushd %{name}-libraries-%{version}/
%{__make} INSTALL="install -p" DESTDIR=%{buildroot} install
popd

# install template
install -d %{buildroot}%{_datadir}/%{name}/template
install -m 644 template/%{name}.pro %{buildroot}%{_datadir}/%{name}/template

# Footprints
pushd %{name}-footprints-%{version}/
cp -a */ %{buildroot}%{_datadir}/%{name}/modules
popd
ln -f %{buildroot}%{_datadir}/%{name}/template/fp-lib-table{.for-pretty,}

# Preparing for documentation pull-ups
%{__rm} -f  %{name}-doc-%{version}/doc/help/CMakeLists.txt
%{__rm} -f  %{name}-doc-%{version}/doc/help/makefile
%{__rm} -f  %{name}-doc-%{version}/doc/tutorials/CMakeLists.txt

%{__cp} -pr %{name}-doc-%{version}/doc/* %{buildroot}%{_docdir}/%{name}
%{__cp} -pr AUTHORS.txt CHANGELOG* %{buildroot}%{_docdir}/%{name}

# Drop this, it's no longer able to webstart the freerouter
# and we have it available locally anyway
rm %{buildroot}%{_bindir}/*.jnlp

%find_lang %{name}


%post
touch --no-create %{_datadir}/icons/hicolor || :
touch --no-create %{_datadir}/mime/packages &> /dev/null || :
update-desktop-database &> /dev/null || :


%postun
if [ $1 -eq 0 ]
then
  touch --no-create %{_datadir}/icons/hicolor || :
  gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
  touch --no-create %{_datadir}/mime/packages &> /dev/null || :
  update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :
fi
update-desktop-database %{_datadir}/applications > /dev/null 2>&1 || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
update-mime-database %{?fedora:-n} %{_datadir}/mime &> /dev/null || :


%files -f %{name}.lang
%{_bindir}/*
%{_libdir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/mimetypes/application-x-*.*
%{_datadir}/icons/hicolor/*/apps/*.*
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/x-%{name}-*.desktop
#%config(noreplace) %{_sysconfdir}/ld.so.conf.d/kicad.conf
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/*.txt

%files doc
%dir %{_docdir}/%{name}/
%{_docdir}/%{name}/contrib
#%{_docdir}/%{name}/help/
%{_docdir}/%{name}/help/en
%{_docdir}/%{name}/help/file_formats
#%{_docdir}/%{name}/tutorials
%{_docdir}/%{name}/tutorials/en
%{_docdir}/%{name}/scripts

%files doc-de
%{_docdir}/%{name}/help/de
%{_docdir}/%{name}/tutorials/de

%files doc-es
%{_docdir}/%{name}/help/es
%{_docdir}/%{name}/tutorials/es

%files doc-fr
%{_docdir}/%{name}/help/fr
%{_docdir}/%{name}/tutorials/fr

%files doc-hu
%{_docdir}/%{name}/tutorials/hu

%files doc-it
%{_docdir}/%{name}/help/it
%{_docdir}/%{name}/tutorials/it

%files doc-ja
%{_docdir}/%{name}/help/ja
%{_docdir}/%{name}/tutorials/ja

%files doc-pl
%{_docdir}/%{name}/help/pl
%{_docdir}/%{name}/tutorials/pl

%files doc-pt
%{_docdir}/%{name}/help/pt

%files doc-ru
%{_docdir}/%{name}/help/ru
%{_docdir}/%{name}/tutorials/ru

%files doc-zh_CN
%{_docdir}/%{name}/tutorials/zh_CN


%changelog
* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 2014.03.13-11.rev4744
- Rebuild for boost 1.57.0
- Add upstream patch to support new Boost.Context API
  (kicad-2014.03.13-boost-context.patch)

* Fri Jan 02 2015 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-10.rev4744
- Use local autorouter

* Sun Nov 30 2014 Lubomir Rintel <lkundrak@v3.sk> - 2014.03.13-9.rev4744
- Install library footprints

* Mon Aug 18 2014 Rex Dieter <rdieter@fedoraproject.org> 2014.03.13-8.rev4744
- update mime scriptlets

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-7.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2014.03.13-6.rev4744
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Petr Machata <pmachata@redhat.com> - 2014.03.13-5.rev4744
- Rebuild for boost 1.55.0

* Tue Mar 18 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-4.rev4744
- Removing ExcludeArch as boost-context has been built for arm

* Mon Mar 17 2014 Ville Skyttä <ville.skytta@iki.fi> - 2014.03.13-3.rev4744
- Don't strip binaries too early (#1076929)

* Mon Mar 17 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-2.rev4744
- Fixing the pcb_calculator desktop file (missing underscore)

* Thu Mar 13 2014 Jaromir Capik <jcapik@redhat.com> - 2014.03.13-1.rev4744
- Update to the latest available revisions
- Building with -j1 instead of _smp_mflags (probably causing build failures)
- Creating scripts for source downloading & postprocessing
- Fixing bogus dates in the changelog

* Mon Dec 23 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-2.rev4021
- Removed kicad.pdf from kicad (Fix #1001243)
- Clean up spec file as suggested by Michael Schwendt
- ldconfig no more needed in this release
- Fix kicad-doc Group
- kicad-doc no more requires kicad
 
* Sat Jun 22 2013 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2013.06.11-1.rev4021
- New upstream release
- Added symbols and modules (with 3d view) from Walter Lain
 
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-3.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2012.01.19-2.rev3256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jan 29 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2012.01.19-1.rev3256
- New upstream release
- Add doxygen as build requirement
- Add bulgarian language
- Add it and pl tutorials
- Update versioning patch
- Add patch to fix python syntax in bom-in-python (Gerd v. Egidy <gerd@egidy.de>)
- Add a new patch to fix a new link time error
- Fix a PS plotting scale bug
- Move junction button close to no connexion button
- Fix thermal relief gap calculation for circular pads in pcbnew
- Add undo/redo support for Pcbnew auto place, auto move, and auto route features.
- Make CvPcb correctly preview the selected component footprint if one has already been assigned.
- Fix a bug in pcb calculation
- Width tuning (width correction) for PS plotting of tracks, pads and vias

* Wed Jan 25 2012 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-4.rev3047
- Fix gcc-4.7 issue by Scott Tsai <scottt.tw@gmail.com> 

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2011.07.12-3.rev3047
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jul 15 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-2.rev3047
- Fix patch command 

* Tue Jul 12 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.07.12-1.rev3047
- New upstream version
- Update versioning patch
- Add Polish documentation
- Add Epcos MKT capacitors library
- Fix localisation installation path

* Mon Apr  4 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-3.rev2765
- Fix 3D viewer crash (BZ #693008)

* Wed Mar 23 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-2.rev2765
- Add missing library

* Tue Mar 22 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2011.01.28-1.rev2765
- New upstream version
- Update versioning patch, all others patches no more needed
- Patch to fix a link time error (with help from Kevin Kofler and Nikola Pajkovsky)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2010.05.27-10.rev2363
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Dan Horák <dan@danny.cz> - 2010.05.27-9.rev2363
- Add s390x as 64-bit arch

* Sat Jan 29 2011 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-8.rev2363
- Fix 3D view crash with some graphics cards (BZ #664143).

* Wed Jul 14 2010 Dan Horák <dan@danny.cz> - 2010.05.27-7.rev2363
- rebuilt against wxGTK-2.8.11-2

* Tue Jun 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-6
- Fix some module edition issues (https://bugs.launchpad.net/kicad/+bug/593546,
  https://bugs.launchpad.net/kicad/+bug/593547)

* Fri Jun 11 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-5
- Fix a crash in searching string (https://bugs.launchpad.net/kicad/+bug/592566)

* Tue Jun  8 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-4
- Fix a focus issue (https://bugs.launchpad.net/kicad/+bug/587970)
- Fix an unwanted mouse cursor move when using the t hotkey in pcbnew
- Fix an issue on arcs draw in 3D viewer (https://bugs.launchpad.net/kicad/+bug/588882)

* Mon May 31 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-3
- Fix an undo-redo issue (https://bugs.launchpad.net/kicad/+bug/586032)

* Sun May 30 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-2
- Don't forget icons

* Sat May 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.27-1
- New packager version
- Update kicad version number patch
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587175
- Patch to fix https://bugs.launchpad.net/kicad/+bug/587176

* Fri May 21 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-3
- Fix the kicad version number
- Fix a problem when trying to modify a footprint value in eeschema
  https://bugs.launchpad.net/kicad/+bug/583939

* Tue May 18 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-2
- No backup of patched files to delete
- Add noreplace flag to config macro

* Mon May 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.09-1
- New upstream version
- All previous patches no more needed
- Backward to cmake 2.6 requirement

* Sun May  9 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.05.05-1
- New upstream version
- All previous patches no more needed
- Fix url: KiCad move from SourceForge.net to LaunchPad.net
- Remove vendor tag from desktop-file-install
- Add x-kicad-pcbnew mimetype
- Add new icons for mimetype

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-9.rev2515
- Fix a minor bug that occurs when changing module orientation or side

* Mon May  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-8.rev2515
- Auto update 3D viewer: fix https://bugs.launchpad.net/kicad/+bug/571089
- Create png from screen (libedit): fix https://bugs.launchpad.net/kicad/+bug/573833

* Sun May  2 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-7.rev2515
- Rename COTATION class (french word) in DIMENSION and fix
  https://bugs.launchpad.net/kicad/+bug/568356 and https://bugs.launchpad.net/kicad/+bug/568357
- Some code cleaning ans enhancements + fix a bug about last netlist file used (LP #567902)

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-6.rev2515
- Make cleanup feature undoable, fix https://bugs.launchpad.net/kicad/+bug/564619
- Fix issues in SVG export, fix https://bugs.launchpad.net/kicad/+bug/565388
- Minor pcbnew enhancements
- Fix minor gerber problems, fix https://bugs.launchpad.net/kicad/+bug/567881

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-5.rev2515
- DRC have to use the local parameters clearance if specified,
  and NETCLASS value only if no local value specified. 

* Sat May  1 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-4.rev2514
- Fix https://bugs.launchpad.net/bugs/568896 and https://bugs.launchpad.net/bugs/569312

* Thu Apr 29 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-3.rev2514
- Fix a crash that happens sometimes when opening the design rule dialog

* Mon Apr 26 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-2.rev2514
- Fix https://bugs.launchpad.net/bugs/570074

* Mon Apr 12 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.04.06-1.rev2514
- New upstream version
- Patches no more needed

* Mon Apr  5 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-5.rev2463
- Add patch to fix SF #2981759

* Sat Apr  3 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-4.rev2463
- Apply upstream patch to fix inch/mm ratio
- Provide a source download URL

* Wed Mar 17 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-3.rev2463
- Patch with svn revision 2463 which fix 2 bugs
- Harmonize identation in %%changelog

* Tue Mar 16 2010 Tom "spot" Callaway <tcallawa@redhat.com> 2010.03.14-2.rev2462
- Link fixes. Really, these libraries should be linked properly so they don't need
  the executable linking calls to be explicitly correct, but cmake gives me a headache.
- Fix demo installation

* Mon Mar 15 2010 Alain Portal <alain.portal[AT]univ-montp2[DOT]fr> 2010.03.14-1.rev2462
- New upstream version

* Mon Aug 24 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-4.rev1863
- Multilib path correction, BZ 518916.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009.07.07-3.rev1863
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 08 2009 Jon Ciesla <limb@jcomserv.net> - 2009.07.07-2.rev1863
- Dropped eeschema desktop file.
- Moved English kicad.pdf to main rpm.
- Added ls.so.conf file and ldconfig to post, postun to fix libs issue.
- Dropped category Development from desktop file.

* Tue Jul 7 2009 Chitlesh Goorah <chitlesh [AT] fedoraproject DOT org> - 2009.07.07-1.rev1863
- svn rev 1863
- documentation splitted into multiple packages
- libraries are now taken directly from SVN rather than from older releases
- build changed to cmake based

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2007.07.09-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Michael Schwendt <mschwendt@fedoraproject.org> - 2007.07.09-4
- First patch is Patch0 - should fix build in Rawhide.
- Include %%_libdir/kicad directory.
- Drop explicit Requires wxGTK in favour of automatic SONAME dependencies.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2007.07.09-3
- Autorebuild for GCC 4.3

* Mon Oct 15 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-2
- Update desktop file

* Thu Oct 04 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.07.09-1
- New upstream version
- Merge previous patches
- Remove X-Fedora, Electronics and Engineering categories
- Update desktop file

* Mon Aug 27 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-4
- License tag clarification

* Thu Aug 23 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-3
- Rebuild

* Wed Feb 14 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-2
- Fix desktop entry. Fix #228598

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2007.01.15-1
- New upstream version

* Thu Feb  8 2007 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-4
- Add patch to build with RPM_OPT_FLAGS and remove -s from LDFLAGS
  Contribution of Ville Skyttä <ville[DOT]skytta[AT]iki[DOT]fi>
  Fix #227757
- Fix typo in french summary

* Thu Dec 28 2006 Jason L Tibbitts III <tibbs@math.uh.edu> 2006.08.28-3
- Rebuild with wxGTK 2.8.

* Thu Oct 05 2006 Christian Iseli <Christian.Iseli@licr.org> 2006.08.28-2
- rebuilt for unwind info generation, broken in gcc-4.1.1-21

* Fri Sep 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.08.28-1
- New upstream version
- Use macro style instead of variable style
- Install missing modules. Fix #206602

* Fri Sep  1 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-6
- FE6 rebuild

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-5
- Removing backup files is no more needed.

* Mon Jul 10 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-4
- Remove BR libGLU-devel that is no more needed (bug #197501 is closed)
- Fix files permissions.

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-3
- s/mesa-libGLU-devel/libGLU-devel/

* Mon Jul  3 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-2
- BR mesa-libGLU-devel

* Wed Jun 28 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.06.26-1
- New upstream version

* Tue Jun 13 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006.04.24-5
- Change name
- Use %%{_docdir} instead of %%{_datadir}/doc
- Use %%find_lang
- Update desktop database
- Convert MSDOS EOL to Unix EOL
- Remove BR utrac

* Mon Jun 12 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-4
- Patch to suppress extra qualification compile time error on FC5
- BR utrac to convert MSDOS files before applying patch
  This will be remove for the next upstream version.

* Tue May 23 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-3
- Install help in /usr/share/doc/kicad/ as the path is hardcoded in gestfich.cpp
- Add desktop file

* Mon May 22 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-2
- Add a second tarball that contains many things that are not included in
  the upstream source tarball such components and footprints librairies,
  help, localisation, etc.

* Sun May 21 2006 Alain Portal <aportal[AT]univ-montp2[DOT]fr> 2006-04-24-0-1
- Initial Fedora RPM
