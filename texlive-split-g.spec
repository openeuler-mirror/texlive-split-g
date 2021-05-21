%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-g
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source1439:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/din1505.tar.xz
Source1440:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/din1505.doc.tar.xz
Source1441:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dk-bib.tar.xz
Source1442:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dk-bib.doc.tar.xz
Source1444:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doipubmed.tar.xz
Source1445:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doipubmed.doc.tar.xz
Source1767:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dice.tar.xz
Source1768:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dice.doc.tar.xz
Source1769:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dictsym.tar.xz
Source1770:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dictsym.doc.tar.xz
Source1771:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dingbat.tar.xz
Source1772:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dingbat.doc.tar.xz
Source1774:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doublestroke.tar.xz
Source1775:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doublestroke.doc.tar.xz
Source1776:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dozenal.tar.xz
Source1777:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dozenal.doc.tar.xz
Source1779:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drm.tar.xz
Source1780:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drm.doc.tar.xz
Source1782:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/droid.tar.xz
Source1783:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/droid.doc.tar.xz
Source1785:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duerer.tar.xz
Source1786:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duerer.doc.tar.xz
Source1787:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duerer-latex.tar.xz
Source1788:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duerer-latex.doc.tar.xz
Source1789:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dutchcal.tar.xz
Source1790:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dutchcal.doc.tar.xz
Source2178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipsconfig.tar.xz
Source2266:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dinat.tar.xz
Source2267:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dinat.doc.tar.xz
Source2268:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dirtree.tar.xz
Source2269:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dirtree.doc.tar.xz
Source2271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docbytex.tar.xz
Source2272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docbytex.doc.tar.xz
Source2273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dowith.tar.xz
Source2274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dowith.doc.tar.xz
Source2374:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dramatist.tar.xz
Source2375:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dramatist.doc.tar.xz
Source2377:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvgloss.tar.xz
Source2378:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvgloss.doc.tar.xz
Source2508:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dnp.tar.xz
Source2542:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/disser.tar.xz
Source2543:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/disser.doc.tar.xz
Source2613:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dickimaw.doc.tar.xz
Source2614:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxtut.doc.tar.xz
Source2708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/droit-fr.tar.xz
Source2709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/droit-fr.doc.tar.xz
Source2744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dhua.tar.xz
Source2745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dhua.doc.tar.xz
Source3122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagmac2.tar.xz
Source3123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagmac2.doc.tar.xz
Source3124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doc-pictex.doc.tar.xz
Source3125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dottex.tar.xz
Source3126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dottex.doc.tar.xz
Source3128:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dot2texi.tar.xz
Source3129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dot2texi.doc.tar.xz
Source3130:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dratex.tar.xz
Source3131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dratex.doc.tar.xz
Source3132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drs.tar.xz
Source3133:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drs.doc.tar.xz
Source3134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duotenzor.tar.xz
Source3135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/duotenzor.doc.tar.xz
Source3690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagbox.tar.xz
Source3691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagbox.doc.tar.xz
Source3693:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagnose.tar.xz
Source3694:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diagnose.doc.tar.xz
Source3695:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dialogl.tar.xz
Source3696:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dialogl.doc.tar.xz
Source3698:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dichokey.tar.xz
Source3699:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dichokey.doc.tar.xz
Source3700:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dinbrief.tar.xz
Source3701:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dinbrief.doc.tar.xz
Source3703:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/directory.tar.xz
Source3704:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/directory.doc.tar.xz
Source3705:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dirtytalk.tar.xz
Source3706:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dirtytalk.doc.tar.xz
Source3708:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dlfltxb.tar.xz
Source3709:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dlfltxb.doc.tar.xz
Source3710:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dnaseq.tar.xz
Source3711:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dnaseq.doc.tar.xz
Source3713:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doclicense.tar.xz
Source3714:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doclicense.doc.tar.xz
Source3716:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docmfp.tar.xz
Source3717:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docmfp.doc.tar.xz
Source3719:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docmute.tar.xz
Source3720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docmute.doc.tar.xz
Source3722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doctools.tar.xz
Source3723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doctools.doc.tar.xz
Source3725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/documentation.tar.xz
Source3726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/documentation.doc.tar.xz
Source3728:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doi.tar.xz
Source3729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/doi.doc.tar.xz
Source3730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dotarrow.tar.xz
Source3731:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dotarrow.doc.tar.xz
Source3733:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dotseqn.tar.xz
Source3734:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dotseqn.doc.tar.xz
Source3736:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/download.tar.xz
Source3737:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/download.doc.tar.xz
Source3739:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dox.tar.xz
Source3740:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dox.doc.tar.xz
Source3742:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dpfloat.tar.xz
Source3743:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dpfloat.doc.tar.xz
Source3744:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dprogress.tar.xz
Source3745:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dprogress.doc.tar.xz
Source3747:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drac.tar.xz
Source3748:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drac.doc.tar.xz
Source3750:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftcopy.tar.xz
Source3751:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftcopy.doc.tar.xz
Source3753:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftwatermark.tar.xz
Source3754:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftwatermark.doc.tar.xz
Source3756:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtk.tar.xz
Source3757:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtk.doc.tar.xz
Source3758:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxgallery.doc.tar.xz
Source3760:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvdcoll.tar.xz
Source3761:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvdcoll.doc.tar.xz
Source3762:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynblocks.tar.xz
Source3763:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynblocks.doc.tar.xz
Source5946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drv.tar.xz
Source5947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drv.doc.tar.xz
Source5948:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviincl.tar.xz
Source5949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviincl.doc.tar.xz
Source6119:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dsptricks.tar.xz
Source6120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dsptricks.doc.tar.xz
Source6348:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dithesis.tar.xz
Source6349:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dithesis.doc.tar.xz
Source6647:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/digiconfigs.tar.xz
Source6648:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/digiconfigs.doc.tar.xz
Source6649:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drawstack.tar.xz
Source6650:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drawstack.doc.tar.xz
Source6651:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dyntree.tar.xz
Source6652:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dyntree.doc.tar.xz
Source7309:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drawmatrix.tar.xz
Source7310:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/drawmatrix.doc.tar.xz
Source7315:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynamicnumber.tar.xz
Source7316:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynamicnumber.doc.tar.xz
Source7720:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/docsurvey.doc.tar.xz
Source7721:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftfigure.tar.xz
Source7722:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/draftfigure.doc.tar.xz
Source7723:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxdescribe.tar.xz
Source7724:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxdescribe.doc.tar.xz
Source7725:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ducksay.tar.xz
Source7726:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ducksay.doc.tar.xz
Source7729:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynkin-diagrams.tar.xz
Source7730:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dynkin-diagrams.doc.tar.xz
Source8122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diffcoeff.tar.xz
Source8123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diffcoeff.doc.tar.xz
Source8124:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dijkstra.tar.xz
Source8125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dijkstra.doc.tar.xz
Source8126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dsserif.tar.xz
Source8127:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dsserif.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-din1505
Provides:       tex-din1505 = %{tl_version}
License:        Bibtex
Summary:        Bibliography styles for German texts
Version:        svn19441.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-din1505
A set of bibliography styles that conformt to DIN 1505, and
match the original BibTeX standard set (plain, unsrt, alpha and
abbrv), together with a style natdin to work with natbib.

%package -n texlive-din1505-doc
Summary:        Documentation for din1505
Version:        svn19441.0

Provides:       tex-din1505-doc
AutoReqProv:    No

%description -n texlive-din1505-doc
Documentation for din1505

%package -n texlive-dk-bib
Provides:       tex-dk-bib = %{tl_version}
License:        GPLv2+
Summary:        Danish variants of standard BibTeX styles
Version:        svn15878.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(url.sty)
Provides:       tex(dk-apali.sty) = %{tl_version}, tex(dk-bib.sty) = %{tl_version}

%description -n texlive-dk-bib
Dk-bib is a translation of the four standard BibTeX style files
(abbrv, alpha, plain and unsrt) and the apalike style file into
Danish. The files have been extended with URL, ISBN, ISSN,
annote and printing fields which can be enabled through a LaTeX
style file. Dk-bib also comes with a couple of Danish sorting
order files for BibTeX8.

%package -n texlive-dk-bib-doc
Summary:        Documentation for dk-bib
Version:        svn15878.0.6

Provides:       tex-dk-bib-doc
AutoReqProv:    No

%description -n texlive-dk-bib-doc
Documentation for dk-bib

%package -n texlive-doipubmed
Provides:       tex-doipubmed = %{tl_version}
License:        LPPL
Summary:        Special commands for use in bibliographies
Version:        svn15878.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty)
Provides:       tex(doipubmed.sty) = %{tl_version}

%description -n texlive-doipubmed
The package provides the commands \doi, \pubmed and \citeurl.
These commands are primarily designed for use in
bibliographies. A LaTeX2HTML style file is also provided.

%package -n texlive-doipubmed-doc
Summary:        Documentation for doipubmed
Version:        svn15878.1.01

Provides:       tex-doipubmed-doc
AutoReqProv:    No

%description -n texlive-doipubmed-doc
Documentation for doipubmed

%package -n texlive-dice
Provides:       tex-dice = %{tl_version}
License:        LPPL
Summary:        A font for die faces
Version:        svn28501.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dice3d.tfm) = %{tl_version}

%description -n texlive-dice
A Metafont font that can produce die faces in 2D or with
various 3D effects.

%package -n texlive-dice-doc
Summary:        Documentation for dice
Version:        svn28501.0

Provides:       tex-dice-doc
AutoReqProv:    No

%description -n texlive-dice-doc
Documentation for dice

%package -n texlive-dictsym
Provides:       tex-dictsym = %{tl_version}
License:        LPPL
Summary:        DictSym font and macro package
Version:        svn20031.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(pifont.sty), tex(keyval.sty)
Provides:       tex(dictsym.map) = %{tl_version}, tex(dictsym.tfm) = %{tl_version}
Provides:       tex(dictsym.pfb) = %{tl_version}, tex(dictsym.sty) = %{tl_version}

%description -n texlive-dictsym
This directory contains the DictSym Type1 font designed by
Georg Verweyen and all files required to use it with LaTeX on
the Unix or PC platforms. The font provides a number of symbols
commonly used in dictionaries. The accompanying macro package
makes the symbols accessible as LaTeX commands.

%package -n texlive-dictsym-doc
Summary:        Documentation for dictsym
Version:        svn20031.0

Provides:       tex-dictsym-doc
AutoReqProv:    No

%description -n texlive-dictsym-doc
Documentation for dictsym

%package -n texlive-dingbat
Provides:       tex-dingbat = %{tl_version}
License:        LPPL
Summary:        Two dingbat symbol fonts
Version:        svn27918.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ark10.tfm) = %{tl_version}, tex(dingbat.tfm) = %{tl_version}
Provides:       tex(dingbat.sty) = %{tl_version}, tex(uark.fd) = %{tl_version}
Provides:       tex(udingbat.fd) = %{tl_version}

%description -n texlive-dingbat
The fonts (ark10 and dingbat) are specified in Metafont;
support macros are provided for use in LaTeX. An Adobe Type 1
version of the fonts is available in the niceframe fonts
bundle.

%package -n texlive-dingbat-doc
Summary:        Documentation for dingbat
Version:        svn27918.1.0

Provides:       tex-dingbat-doc
AutoReqProv:    No

%description -n texlive-dingbat-doc
Documentation for dingbat

%package -n texlive-doublestroke
Provides:       tex-doublestroke = %{tl_version}
License:        Doublestroke
Summary:        Typeset mathematical double stroke symbols
Version:        svn15878.1.111

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(dstroke.map) = %{tl_version}, tex(dsrom10.tfm) = %{tl_version}
Provides:       tex(dsrom12.tfm) = %{tl_version}, tex(dsrom8.tfm) = %{tl_version}
Provides:       tex(dsss10.tfm) = %{tl_version}, tex(dsss12.tfm) = %{tl_version}
Provides:       tex(dsss8.tfm) = %{tl_version}, tex(dsrom10.pfb) = %{tl_version}
Provides:       tex(dsrom12.pfb) = %{tl_version}, tex(dsrom8.pfb) = %{tl_version}
Provides:       tex(dsss10.pfb) = %{tl_version}, tex(dsss12.pfb) = %{tl_version}
Provides:       tex(dsss8.pfb) = %{tl_version}, tex(Udsrom.fd) = %{tl_version}
Provides:       tex(Udsss.fd) = %{tl_version}, tex(dsfont.sty) = %{tl_version}

%description -n texlive-doublestroke
A font based on Computer Modern Roman useful for typesetting
the mathematical symbols for the natural numbers (N), whole
numbers (Z), rational numbers (Q), real numbers (R) and complex
numbers (C); coverage includes all Roman capital letters, '1',
'h' and 'k'. The font is available both as Metafont source and
in Adobe Type 1 format, and LaTeX macros for its use are
provided. The fonts appear in the blackboard bold sampler.

%package -n texlive-doublestroke-doc
Summary:        Documentation for doublestroke
Version:        svn15878.1.111

Provides:       tex-doublestroke-doc
AutoReqProv:    No

%description -n texlive-doublestroke-doc
Documentation for doublestroke

%package -n texlive-dozenal
Provides:       tex-dozenal = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset documents using base twelve numbering (also called "dozenal")
Version:        svn47680
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(fixltx2e.sty), tex(xstring.sty), tex(ifpdf.sty), tex(mfirstuc.sty)
Provides:       tex(dozenal.map) = %{tl_version}, tex(dozchars10.tfm) = %{tl_version}
Provides:       tex(dozchars12.tfm) = %{tl_version}, tex(dozchars17.tfm) = %{tl_version}
Provides:       tex(dozchars6.tfm) = %{tl_version}, tex(dozchars7.tfm) = %{tl_version}
Provides:       tex(dozchars8.tfm) = %{tl_version}, tex(dozchars9.tfm) = %{tl_version}
Provides:       tex(dozchb10.tfm) = %{tl_version}, tex(dozchbx10.tfm) = %{tl_version}
Provides:       tex(dozchbx12.tfm) = %{tl_version}, tex(dozchbx5.tfm) = %{tl_version}
Provides:       tex(dozchbx6.tfm) = %{tl_version}, tex(dozchbx7.tfm) = %{tl_version}
Provides:       tex(dozchbx8.tfm) = %{tl_version}, tex(dozchbx9.tfm) = %{tl_version}
Provides:       tex(dozchbxi10.tfm) = %{tl_version}, tex(dozchbxsl10.tfm) = %{tl_version}
Provides:       tex(dozchit10.tfm) = %{tl_version}, tex(dozchit12.tfm) = %{tl_version}
Provides:       tex(dozchit7.tfm) = %{tl_version}, tex(dozchit8.tfm) = %{tl_version}
Provides:       tex(dozchit9.tfm) = %{tl_version}, tex(dozchsl10.tfm) = %{tl_version}
Provides:       tex(dozchsl12.tfm) = %{tl_version}, tex(dozchsl8.tfm) = %{tl_version}
Provides:       tex(dozchsl9.tfm) = %{tl_version}, tex(dozchars10.pfb) = %{tl_version}
Provides:       tex(dozchars12.pfb) = %{tl_version}, tex(dozchars17.pfb) = %{tl_version}
Provides:       tex(dozchars6.pfb) = %{tl_version}, tex(dozchars7.pfb) = %{tl_version}
Provides:       tex(dozchars8.pfb) = %{tl_version}, tex(dozchars9.pfb) = %{tl_version}
Provides:       tex(dozchb10.pfb) = %{tl_version}, tex(dozchbx10.pfb) = %{tl_version}
Provides:       tex(dozchbx12.pfb) = %{tl_version}, tex(dozchbx5.pfb) = %{tl_version}
Provides:       tex(dozchbx6.pfb) = %{tl_version}, tex(dozchbx7.pfb) = %{tl_version}
Provides:       tex(dozchbx8.pfb) = %{tl_version}, tex(dozchbx9.pfb) = %{tl_version}
Provides:       tex(dozchbxi10.pfb) = %{tl_version}, tex(dozchbxsl10.pfb) = %{tl_version}
Provides:       tex(dozchit10.pfb) = %{tl_version}, tex(dozchit12.pfb) = %{tl_version}
Provides:       tex(dozchit7.pfb) = %{tl_version}, tex(dozchit8.pfb) = %{tl_version}
Provides:       tex(dozchit9.pfb) = %{tl_version}, tex(dozchsl10.pfb) = %{tl_version}
Provides:       tex(dozchsl12.pfb) = %{tl_version}, tex(dozchsl8.pfb) = %{tl_version}
Provides:       tex(dozchsl9.pfb) = %{tl_version}, tex(dozenal.sty) = %{tl_version}

%description -n texlive-dozenal
The package supports typesetting documents whose counters are
represented in base twelve, also called "dozenal". It includes
a macro by David Kastrup for converting positive whole numbers
to dozenal from decimal (base ten) representation. The package
also includes a few other macros and redefines all the standard
counters to produce dozenal output. Fonts, in Roman, italic,
slanted, and boldface versions, provide ten and eleven (the
Pitman characters preferred by the Dozenal Society of Great
Britain). The fonts were designed to blend well with the
Computer Modern fonts, and are available both as Metafont
source and in Adobe Type 1 format.

%package -n texlive-dozenal-doc
Summary:        Documentation for dozenal
Version:        svn47680
Provides:       tex-dozenal-doc
AutoReqProv:    No

%description -n texlive-dozenal-doc
Documentation for dozenal

%package -n texlive-drm
Provides:       tex-drm = %{tl_version}
License:        LPPL 1.3
Summary:        A complete family of fonts written in Metafont
Version:        svn38157.4.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fontenc.sty), tex(modroman.sty), tex(amsmath.sty), tex(gmp.sty)
Requires:       tex(ifpdf.sty)
Provides:       tex(drm.map) = %{tl_version}, tex(drm10.otf) = %{tl_version}
Provides:       tex(drm11.otf) = %{tl_version}, tex(drm12.otf) = %{tl_version}
Provides:       tex(drm14.otf) = %{tl_version}, tex(drm17.otf) = %{tl_version}
Provides:       tex(drm24.otf) = %{tl_version}, tex(drm6.otf) = %{tl_version}
Provides:       tex(drm7.otf) = %{tl_version}, tex(drm8.otf) = %{tl_version}
Provides:       tex(drm9.otf) = %{tl_version}, tex(drmb10.otf) = %{tl_version}
Provides:       tex(drmb11.otf) = %{tl_version}, tex(drmb12.otf) = %{tl_version}
Provides:       tex(drmb14.otf) = %{tl_version}, tex(drmb17.otf) = %{tl_version}
Provides:       tex(drmb24.otf) = %{tl_version}, tex(drmb6.otf) = %{tl_version}
Provides:       tex(drmb7.otf) = %{tl_version}, tex(drmb8.otf) = %{tl_version}
Provides:       tex(drmb9.otf) = %{tl_version}, tex(drmbx10.otf) = %{tl_version}
Provides:       tex(drmbx11.otf) = %{tl_version}, tex(drmbx12.otf) = %{tl_version}
Provides:       tex(drmbx14.otf) = %{tl_version}, tex(drmbx17.otf) = %{tl_version}
Provides:       tex(drmbx24.otf) = %{tl_version}, tex(drmbx6.otf) = %{tl_version}
Provides:       tex(drmbx7.otf) = %{tl_version}, tex(drmbx8.otf) = %{tl_version}
Provides:       tex(drmbx9.otf) = %{tl_version}, tex(drmdoz10.otf) = %{tl_version}
Provides:       tex(drmdoz11.otf) = %{tl_version}, tex(drmdoz12.otf) = %{tl_version}
Provides:       tex(drmdoz14.otf) = %{tl_version}, tex(drmdoz17.otf) = %{tl_version}
Provides:       tex(drmdoz24.otf) = %{tl_version}, tex(drmdoz6.otf) = %{tl_version}
Provides:       tex(drmdoz7.otf) = %{tl_version}, tex(drmdoz8.otf) = %{tl_version}
Provides:       tex(drmdoz9.otf) = %{tl_version}, tex(drmdozb10.otf) = %{tl_version}
Provides:       tex(drmdozb11.otf) = %{tl_version}, tex(drmdozb12.otf) = %{tl_version}
Provides:       tex(drmdozb14.otf) = %{tl_version}, tex(drmdozb17.otf) = %{tl_version}
Provides:       tex(drmdozb24.otf) = %{tl_version}, tex(drmdozb6.otf) = %{tl_version}
Provides:       tex(drmdozb7.otf) = %{tl_version}, tex(drmdozb8.otf) = %{tl_version}
Provides:       tex(drmdozb9.otf) = %{tl_version}, tex(drmdozbx10.otf) = %{tl_version}
Provides:       tex(drmdozbx11.otf) = %{tl_version}, tex(drmdozbx12.otf) = %{tl_version}
Provides:       tex(drmdozbx14.otf) = %{tl_version}, tex(drmdozbx17.otf) = %{tl_version}
Provides:       tex(drmdozbx24.otf) = %{tl_version}, tex(drmdozbx6.otf) = %{tl_version}
Provides:       tex(drmdozbx7.otf) = %{tl_version}, tex(drmdozbx8.otf) = %{tl_version}
Provides:       tex(drmdozbx9.otf) = %{tl_version}, tex(drmdozit10.otf) = %{tl_version}
Provides:       tex(drmdozit11.otf) = %{tl_version}, tex(drmdozit12.otf) = %{tl_version}
Provides:       tex(drmdozit14.otf) = %{tl_version}, tex(drmdozit17.otf) = %{tl_version}
Provides:       tex(drmdozit24.otf) = %{tl_version}, tex(drmdozit6.otf) = %{tl_version}
Provides:       tex(drmdozit7.otf) = %{tl_version}, tex(drmdozit8.otf) = %{tl_version}
Provides:       tex(drmdozit9.otf) = %{tl_version}, tex(drmdozitbx10.otf) = %{tl_version}
Provides:       tex(drmdozitbx11.otf) = %{tl_version}, tex(drmdozitbx12.otf) = %{tl_version}
Provides:       tex(drmdozitbx14.otf) = %{tl_version}, tex(drmdozitbx17.otf) = %{tl_version}
Provides:       tex(drmdozitbx24.otf) = %{tl_version}, tex(drmdozitbx6.otf) = %{tl_version}
Provides:       tex(drmdozitbx7.otf) = %{tl_version}, tex(drmdozitbx8.otf) = %{tl_version}
Provides:       tex(drmdozitbx9.otf) = %{tl_version}, tex(drmdozitsc10.otf) = %{tl_version}
Provides:       tex(drmdozitsc11.otf) = %{tl_version}, tex(drmdozitsc12.otf) = %{tl_version}
Provides:       tex(drmdozitsc14.otf) = %{tl_version}, tex(drmdozitsc17.otf) = %{tl_version}
Provides:       tex(drmdozitsc24.otf) = %{tl_version}, tex(drmdozitsc6.otf) = %{tl_version}
Provides:       tex(drmdozitsc7.otf) = %{tl_version}, tex(drmdozitsc8.otf) = %{tl_version}
Provides:       tex(drmdozitsc9.otf) = %{tl_version}, tex(drmdozittc10.otf) = %{tl_version}
Provides:       tex(drmdozittc11.otf) = %{tl_version}, tex(drmdozittc12.otf) = %{tl_version}
Provides:       tex(drmdozittc14.otf) = %{tl_version}, tex(drmdozittc17.otf) = %{tl_version}
Provides:       tex(drmdozittc24.otf) = %{tl_version}, tex(drmdozittc6.otf) = %{tl_version}
Provides:       tex(drmdozittc7.otf) = %{tl_version}, tex(drmdozittc8.otf) = %{tl_version}
Provides:       tex(drmdozittc9.otf) = %{tl_version}, tex(drmdozl10.otf) = %{tl_version}
Provides:       tex(drmdozl11.otf) = %{tl_version}, tex(drmdozl12.otf) = %{tl_version}
Provides:       tex(drmdozl14.otf) = %{tl_version}, tex(drmdozl17.otf) = %{tl_version}
Provides:       tex(drmdozl24.otf) = %{tl_version}, tex(drmdozl6.otf) = %{tl_version}
Provides:       tex(drmdozl7.otf) = %{tl_version}, tex(drmdozl8.otf) = %{tl_version}
Provides:       tex(drmdozl9.otf) = %{tl_version}, tex(drmdozsc10.otf) = %{tl_version}
Provides:       tex(drmdozsc11.otf) = %{tl_version}, tex(drmdozsc12.otf) = %{tl_version}
Provides:       tex(drmdozsc14.otf) = %{tl_version}, tex(drmdozsc17.otf) = %{tl_version}
Provides:       tex(drmdozsc24.otf) = %{tl_version}, tex(drmdozsc6.otf) = %{tl_version}
Provides:       tex(drmdozsc7.otf) = %{tl_version}, tex(drmdozsc8.otf) = %{tl_version}
Provides:       tex(drmdozsc9.otf) = %{tl_version}, tex(drmdozscbx10.otf) = %{tl_version}
Provides:       tex(drmdozscbx11.otf) = %{tl_version}, tex(drmdozscbx12.otf) = %{tl_version}
Provides:       tex(drmdozscbx14.otf) = %{tl_version}, tex(drmdozscbx17.otf) = %{tl_version}
Provides:       tex(drmdozscbx24.otf) = %{tl_version}, tex(drmdozscbx6.otf) = %{tl_version}
Provides:       tex(drmdozscbx7.otf) = %{tl_version}, tex(drmdozscbx8.otf) = %{tl_version}
Provides:       tex(drmdozscbx9.otf) = %{tl_version}, tex(drmdozsl10.otf) = %{tl_version}
Provides:       tex(drmdozsl11.otf) = %{tl_version}, tex(drmdozsl12.otf) = %{tl_version}
Provides:       tex(drmdozsl14.otf) = %{tl_version}, tex(drmdozsl17.otf) = %{tl_version}
Provides:       tex(drmdozsl24.otf) = %{tl_version}, tex(drmdozsl6.otf) = %{tl_version}
Provides:       tex(drmdozsl7.otf) = %{tl_version}, tex(drmdozsl8.otf) = %{tl_version}
Provides:       tex(drmdozsl9.otf) = %{tl_version}, tex(drmdoztc10.otf) = %{tl_version}
Provides:       tex(drmdoztc11.otf) = %{tl_version}, tex(drmdoztc12.otf) = %{tl_version}
Provides:       tex(drmdoztc14.otf) = %{tl_version}, tex(drmdoztc17.otf) = %{tl_version}
Provides:       tex(drmdoztc24.otf) = %{tl_version}, tex(drmdoztc6.otf) = %{tl_version}
Provides:       tex(drmdoztc7.otf) = %{tl_version}, tex(drmdoztc8.otf) = %{tl_version}
Provides:       tex(drmdoztc9.otf) = %{tl_version}, tex(drmdoztcbx10.otf) = %{tl_version}
Provides:       tex(drmdoztcbx11.otf) = %{tl_version}, tex(drmdoztcbx12.otf) = %{tl_version}
Provides:       tex(drmdoztcbx14.otf) = %{tl_version}, tex(drmdoztcbx17.otf) = %{tl_version}
Provides:       tex(drmdoztcbx24.otf) = %{tl_version}, tex(drmdoztcbx6.otf) = %{tl_version}
Provides:       tex(drmdoztcbx7.otf) = %{tl_version}, tex(drmdoztcbx8.otf) = %{tl_version}
Provides:       tex(drmdoztcbx9.otf) = %{tl_version}, tex(drmdozui10.otf) = %{tl_version}
Provides:       tex(drmdozui11.otf) = %{tl_version}, tex(drmdozui12.otf) = %{tl_version}
Provides:       tex(drmdozui14.otf) = %{tl_version}, tex(drmdozui17.otf) = %{tl_version}
Provides:       tex(drmdozui24.otf) = %{tl_version}, tex(drmdozui6.otf) = %{tl_version}
Provides:       tex(drmdozui7.otf) = %{tl_version}, tex(drmdozui8.otf) = %{tl_version}
Provides:       tex(drmdozui9.otf) = %{tl_version}, tex(drmdozuibx10.otf) = %{tl_version}
Provides:       tex(drmdozuibx11.otf) = %{tl_version}, tex(drmdozuibx12.otf) = %{tl_version}
Provides:       tex(drmdozuibx14.otf) = %{tl_version}, tex(drmdozuibx17.otf) = %{tl_version}
Provides:       tex(drmdozuibx24.otf) = %{tl_version}, tex(drmdozuibx6.otf) = %{tl_version}
Provides:       tex(drmdozuibx7.otf) = %{tl_version}, tex(drmdozuibx8.otf) = %{tl_version}
Provides:       tex(drmdozuibx9.otf) = %{tl_version}, tex(drmfigs10.otf) = %{tl_version}
Provides:       tex(drmfigs11.otf) = %{tl_version}, tex(drmfigs12.otf) = %{tl_version}
Provides:       tex(drmfigs14.otf) = %{tl_version}, tex(drmfigs17.otf) = %{tl_version}
Provides:       tex(drmfigs24.otf) = %{tl_version}, tex(drmfigs6.otf) = %{tl_version}
Provides:       tex(drmfigs7.otf) = %{tl_version}, tex(drmfigs8.otf) = %{tl_version}
Provides:       tex(drmfigs9.otf) = %{tl_version}, tex(drmgrk10.otf) = %{tl_version}
Provides:       tex(drminf10.otf) = %{tl_version}, tex(drminf11.otf) = %{tl_version}
Provides:       tex(drminf12.otf) = %{tl_version}, tex(drminf14.otf) = %{tl_version}
Provides:       tex(drminf17.otf) = %{tl_version}, tex(drminf24.otf) = %{tl_version}
Provides:       tex(drminf6.otf) = %{tl_version}, tex(drminf7.otf) = %{tl_version}
Provides:       tex(drminf8.otf) = %{tl_version}, tex(drminf9.otf) = %{tl_version}
Provides:       tex(drmit10.otf) = %{tl_version}, tex(drmit11.otf) = %{tl_version}
Provides:       tex(drmit12.otf) = %{tl_version}, tex(drmit14.otf) = %{tl_version}
Provides:       tex(drmit17.otf) = %{tl_version}, tex(drmit24.otf) = %{tl_version}
Provides:       tex(drmit6.otf) = %{tl_version}, tex(drmit7.otf) = %{tl_version}
Provides:       tex(drmit8.otf) = %{tl_version}, tex(drmit9.otf) = %{tl_version}
Provides:       tex(drmitbx10.otf) = %{tl_version}, tex(drmitbx11.otf) = %{tl_version}
Provides:       tex(drmitbx12.otf) = %{tl_version}, tex(drmitbx14.otf) = %{tl_version}
Provides:       tex(drmitbx17.otf) = %{tl_version}, tex(drmitbx24.otf) = %{tl_version}
Provides:       tex(drmitbx6.otf) = %{tl_version}, tex(drmitbx7.otf) = %{tl_version}
Provides:       tex(drmitbx8.otf) = %{tl_version}, tex(drmitbx9.otf) = %{tl_version}
Provides:       tex(drmitsc10.otf) = %{tl_version}, tex(drmitsc11.otf) = %{tl_version}
Provides:       tex(drmitsc12.otf) = %{tl_version}, tex(drmitsc14.otf) = %{tl_version}
Provides:       tex(drmitsc17.otf) = %{tl_version}, tex(drmitsc24.otf) = %{tl_version}
Provides:       tex(drmitsc6.otf) = %{tl_version}, tex(drmitsc7.otf) = %{tl_version}
Provides:       tex(drmitsc8.otf) = %{tl_version}, tex(drmitsc9.otf) = %{tl_version}
Provides:       tex(drmittc10.otf) = %{tl_version}, tex(drmittc11.otf) = %{tl_version}
Provides:       tex(drmittc12.otf) = %{tl_version}, tex(drmittc14.otf) = %{tl_version}
Provides:       tex(drmittc17.otf) = %{tl_version}, tex(drmittc24.otf) = %{tl_version}
Provides:       tex(drmittc6.otf) = %{tl_version}, tex(drmittc7.otf) = %{tl_version}
Provides:       tex(drmittc8.otf) = %{tl_version}, tex(drmittc9.otf) = %{tl_version}
Provides:       tex(drml10.otf) = %{tl_version}, tex(drml11.otf) = %{tl_version}
Provides:       tex(drml12.otf) = %{tl_version}, tex(drml14.otf) = %{tl_version}
Provides:       tex(drml17.otf) = %{tl_version}, tex(drml24.otf) = %{tl_version}
Provides:       tex(drml6.otf) = %{tl_version}, tex(drml7.otf) = %{tl_version}
Provides:       tex(drml8.otf) = %{tl_version}, tex(drml9.otf) = %{tl_version}
Provides:       tex(drmmi10.otf) = %{tl_version}, tex(drmsc10.otf) = %{tl_version}
Provides:       tex(drmsc11.otf) = %{tl_version}, tex(drmsc12.otf) = %{tl_version}
Provides:       tex(drmsc14.otf) = %{tl_version}, tex(drmsc17.otf) = %{tl_version}
Provides:       tex(drmsc24.otf) = %{tl_version}, tex(drmsc6.otf) = %{tl_version}
Provides:       tex(drmsc7.otf) = %{tl_version}, tex(drmsc8.otf) = %{tl_version}
Provides:       tex(drmsc9.otf) = %{tl_version}, tex(drmscbx10.otf) = %{tl_version}
Provides:       tex(drmscbx11.otf) = %{tl_version}, tex(drmscbx12.otf) = %{tl_version}
Provides:       tex(drmscbx14.otf) = %{tl_version}, tex(drmscbx17.otf) = %{tl_version}
Provides:       tex(drmscbx24.otf) = %{tl_version}, tex(drmscbx6.otf) = %{tl_version}
Provides:       tex(drmscbx7.otf) = %{tl_version}, tex(drmscbx8.otf) = %{tl_version}
Provides:       tex(drmscbx9.otf) = %{tl_version}, tex(drmsl10.otf) = %{tl_version}
Provides:       tex(drmsl11.otf) = %{tl_version}, tex(drmsl12.otf) = %{tl_version}
Provides:       tex(drmsl14.otf) = %{tl_version}, tex(drmsl17.otf) = %{tl_version}
Provides:       tex(drmsl24.otf) = %{tl_version}, tex(drmsl6.otf) = %{tl_version}
Provides:       tex(drmsl7.otf) = %{tl_version}, tex(drmsl8.otf) = %{tl_version}
Provides:       tex(drmsl9.otf) = %{tl_version}, tex(drmsy10.otf) = %{tl_version}
Provides:       tex(drmsym10.otf) = %{tl_version}, tex(drmsym11.otf) = %{tl_version}
Provides:       tex(drmsym12.otf) = %{tl_version}, tex(drmsym14.otf) = %{tl_version}
Provides:       tex(drmsym17.otf) = %{tl_version}, tex(drmsym24.otf) = %{tl_version}
Provides:       tex(drmsym7.otf) = %{tl_version}, tex(drmsym8.otf) = %{tl_version}
Provides:       tex(drmsym9.otf) = %{tl_version}, tex(drmtc10.otf) = %{tl_version}
Provides:       tex(drmtc11.otf) = %{tl_version}, tex(drmtc12.otf) = %{tl_version}
Provides:       tex(drmtc14.otf) = %{tl_version}, tex(drmtc17.otf) = %{tl_version}
Provides:       tex(drmtc24.otf) = %{tl_version}, tex(drmtc6.otf) = %{tl_version}
Provides:       tex(drmtc7.otf) = %{tl_version}, tex(drmtc8.otf) = %{tl_version}
Provides:       tex(drmtc9.otf) = %{tl_version}, tex(drmtcbx10.otf) = %{tl_version}
Provides:       tex(drmtcbx11.otf) = %{tl_version}, tex(drmtcbx12.otf) = %{tl_version}
Provides:       tex(drmtcbx14.otf) = %{tl_version}, tex(drmtcbx17.otf) = %{tl_version}
Provides:       tex(drmtcbx24.otf) = %{tl_version}, tex(drmtcbx6.otf) = %{tl_version}
Provides:       tex(drmtcbx7.otf) = %{tl_version}, tex(drmtcbx8.otf) = %{tl_version}
Provides:       tex(drmtcbx9.otf) = %{tl_version}, tex(drmui10.otf) = %{tl_version}
Provides:       tex(drmui11.otf) = %{tl_version}, tex(drmui12.otf) = %{tl_version}
Provides:       tex(drmui14.otf) = %{tl_version}, tex(drmui17.otf) = %{tl_version}
Provides:       tex(drmui24.otf) = %{tl_version}, tex(drmui6.otf) = %{tl_version}
Provides:       tex(drmui7.otf) = %{tl_version}, tex(drmui8.otf) = %{tl_version}
Provides:       tex(drmui9.otf) = %{tl_version}, tex(drmuibx10.otf) = %{tl_version}
Provides:       tex(drmuibx11.otf) = %{tl_version}, tex(drmuibx12.otf) = %{tl_version}
Provides:       tex(drmuibx14.otf) = %{tl_version}, tex(drmuibx17.otf) = %{tl_version}
Provides:       tex(drmuibx24.otf) = %{tl_version}, tex(drmuibx6.otf) = %{tl_version}
Provides:       tex(drmuibx7.otf) = %{tl_version}, tex(drmuibx8.otf) = %{tl_version}
Provides:       tex(drmuibx9.otf) = %{tl_version}, tex(drm10.tfm) = %{tl_version}
Provides:       tex(drm100.tfm) = %{tl_version}, tex(drm11.tfm) = %{tl_version}
Provides:       tex(drm12.tfm) = %{tl_version}, tex(drm14.tfm) = %{tl_version}
Provides:       tex(drm17.tfm) = %{tl_version}, tex(drm24.tfm) = %{tl_version}
Provides:       tex(drm6.tfm) = %{tl_version}, tex(drm7.tfm) = %{tl_version}
Provides:       tex(drm8.tfm) = %{tl_version}, tex(drm9.tfm) = %{tl_version}
Provides:       tex(drmb10.tfm) = %{tl_version}, tex(drmb11.tfm) = %{tl_version}
Provides:       tex(drmb12.tfm) = %{tl_version}, tex(drmb14.tfm) = %{tl_version}
Provides:       tex(drmb17.tfm) = %{tl_version}, tex(drmb24.tfm) = %{tl_version}
Provides:       tex(drmb6.tfm) = %{tl_version}, tex(drmb7.tfm) = %{tl_version}
Provides:       tex(drmb8.tfm) = %{tl_version}, tex(drmb9.tfm) = %{tl_version}
Provides:       tex(drmbs10.tfm) = %{tl_version}, tex(drmbx10.tfm) = %{tl_version}
Provides:       tex(drmbx11.tfm) = %{tl_version}, tex(drmbx12.tfm) = %{tl_version}
Provides:       tex(drmbx14.tfm) = %{tl_version}, tex(drmbx17.tfm) = %{tl_version}
Provides:       tex(drmbx24.tfm) = %{tl_version}, tex(drmbx6.tfm) = %{tl_version}
Provides:       tex(drmbx7.tfm) = %{tl_version}, tex(drmbx8.tfm) = %{tl_version}
Provides:       tex(drmbx9.tfm) = %{tl_version}, tex(drmdoz10.tfm) = %{tl_version}
Provides:       tex(drmdoz11.tfm) = %{tl_version}, tex(drmdoz12.tfm) = %{tl_version}
Provides:       tex(drmdoz14.tfm) = %{tl_version}, tex(drmdoz17.tfm) = %{tl_version}
Provides:       tex(drmdoz24.tfm) = %{tl_version}, tex(drmdoz6.tfm) = %{tl_version}
Provides:       tex(drmdoz7.tfm) = %{tl_version}, tex(drmdoz8.tfm) = %{tl_version}
Provides:       tex(drmdoz9.tfm) = %{tl_version}, tex(drmdozb10.tfm) = %{tl_version}
Provides:       tex(drmdozb11.tfm) = %{tl_version}, tex(drmdozb12.tfm) = %{tl_version}
Provides:       tex(drmdozb14.tfm) = %{tl_version}, tex(drmdozb17.tfm) = %{tl_version}
Provides:       tex(drmdozb24.tfm) = %{tl_version}, tex(drmdozb6.tfm) = %{tl_version}
Provides:       tex(drmdozb7.tfm) = %{tl_version}, tex(drmdozb8.tfm) = %{tl_version}
Provides:       tex(drmdozb9.tfm) = %{tl_version}, tex(drmdozbx10.tfm) = %{tl_version}
Provides:       tex(drmdozbx11.tfm) = %{tl_version}, tex(drmdozbx12.tfm) = %{tl_version}
Provides:       tex(drmdozbx14.tfm) = %{tl_version}, tex(drmdozbx17.tfm) = %{tl_version}
Provides:       tex(drmdozbx24.tfm) = %{tl_version}, tex(drmdozbx6.tfm) = %{tl_version}
Provides:       tex(drmdozbx7.tfm) = %{tl_version}, tex(drmdozbx8.tfm) = %{tl_version}
Provides:       tex(drmdozbx9.tfm) = %{tl_version}, tex(drmdozit10.tfm) = %{tl_version}
Provides:       tex(drmdozit11.tfm) = %{tl_version}, tex(drmdozit12.tfm) = %{tl_version}
Provides:       tex(drmdozit14.tfm) = %{tl_version}, tex(drmdozit17.tfm) = %{tl_version}
Provides:       tex(drmdozit24.tfm) = %{tl_version}, tex(drmdozit6.tfm) = %{tl_version}
Provides:       tex(drmdozit7.tfm) = %{tl_version}, tex(drmdozit8.tfm) = %{tl_version}
Provides:       tex(drmdozit9.tfm) = %{tl_version}, tex(drmdozitbx10.tfm) = %{tl_version}
Provides:       tex(drmdozitbx11.tfm) = %{tl_version}, tex(drmdozitbx12.tfm) = %{tl_version}
Provides:       tex(drmdozitbx14.tfm) = %{tl_version}, tex(drmdozitbx17.tfm) = %{tl_version}
Provides:       tex(drmdozitbx24.tfm) = %{tl_version}, tex(drmdozitbx6.tfm) = %{tl_version}
Provides:       tex(drmdozitbx7.tfm) = %{tl_version}, tex(drmdozitbx8.tfm) = %{tl_version}
Provides:       tex(drmdozitbx9.tfm) = %{tl_version}, tex(drmdozitsc10.tfm) = %{tl_version}
Provides:       tex(drmdozitsc11.tfm) = %{tl_version}, tex(drmdozitsc12.tfm) = %{tl_version}
Provides:       tex(drmdozitsc14.tfm) = %{tl_version}, tex(drmdozitsc17.tfm) = %{tl_version}
Provides:       tex(drmdozitsc24.tfm) = %{tl_version}, tex(drmdozitsc6.tfm) = %{tl_version}
Provides:       tex(drmdozitsc7.tfm) = %{tl_version}, tex(drmdozitsc8.tfm) = %{tl_version}
Provides:       tex(drmdozitsc9.tfm) = %{tl_version}, tex(drmdozittc10.tfm) = %{tl_version}
Provides:       tex(drmdozittc11.tfm) = %{tl_version}, tex(drmdozittc12.tfm) = %{tl_version}
Provides:       tex(drmdozittc14.tfm) = %{tl_version}, tex(drmdozittc17.tfm) = %{tl_version}
Provides:       tex(drmdozittc24.tfm) = %{tl_version}, tex(drmdozittc6.tfm) = %{tl_version}
Provides:       tex(drmdozittc7.tfm) = %{tl_version}, tex(drmdozittc8.tfm) = %{tl_version}
Provides:       tex(drmdozittc9.tfm) = %{tl_version}, tex(drmdozl10.tfm) = %{tl_version}
Provides:       tex(drmdozl11.tfm) = %{tl_version}, tex(drmdozl12.tfm) = %{tl_version}
Provides:       tex(drmdozl14.tfm) = %{tl_version}, tex(drmdozl17.tfm) = %{tl_version}
Provides:       tex(drmdozl24.tfm) = %{tl_version}, tex(drmdozl6.tfm) = %{tl_version}
Provides:       tex(drmdozl7.tfm) = %{tl_version}, tex(drmdozl8.tfm) = %{tl_version}
Provides:       tex(drmdozl9.tfm) = %{tl_version}, tex(drmdozsc10.tfm) = %{tl_version}
Provides:       tex(drmdozsc11.tfm) = %{tl_version}, tex(drmdozsc12.tfm) = %{tl_version}
Provides:       tex(drmdozsc14.tfm) = %{tl_version}, tex(drmdozsc17.tfm) = %{tl_version}
Provides:       tex(drmdozsc24.tfm) = %{tl_version}, tex(drmdozsc6.tfm) = %{tl_version}
Provides:       tex(drmdozsc7.tfm) = %{tl_version}, tex(drmdozsc8.tfm) = %{tl_version}
Provides:       tex(drmdozsc9.tfm) = %{tl_version}, tex(drmdozscbx10.tfm) = %{tl_version}
Provides:       tex(drmdozscbx11.tfm) = %{tl_version}, tex(drmdozscbx12.tfm) = %{tl_version}
Provides:       tex(drmdozscbx14.tfm) = %{tl_version}, tex(drmdozscbx17.tfm) = %{tl_version}
Provides:       tex(drmdozscbx24.tfm) = %{tl_version}, tex(drmdozscbx6.tfm) = %{tl_version}
Provides:       tex(drmdozscbx7.tfm) = %{tl_version}, tex(drmdozscbx8.tfm) = %{tl_version}
Provides:       tex(drmdozscbx9.tfm) = %{tl_version}, tex(drmdozsl10.tfm) = %{tl_version}
Provides:       tex(drmdozsl11.tfm) = %{tl_version}, tex(drmdozsl12.tfm) = %{tl_version}
Provides:       tex(drmdozsl14.tfm) = %{tl_version}, tex(drmdozsl17.tfm) = %{tl_version}
Provides:       tex(drmdozsl24.tfm) = %{tl_version}, tex(drmdozsl6.tfm) = %{tl_version}
Provides:       tex(drmdozsl7.tfm) = %{tl_version}, tex(drmdozsl8.tfm) = %{tl_version}
Provides:       tex(drmdozsl9.tfm) = %{tl_version}, tex(drmdoztc10.tfm) = %{tl_version}
Provides:       tex(drmdoztc11.tfm) = %{tl_version}, tex(drmdoztc12.tfm) = %{tl_version}
Provides:       tex(drmdoztc14.tfm) = %{tl_version}, tex(drmdoztc17.tfm) = %{tl_version}
Provides:       tex(drmdoztc24.tfm) = %{tl_version}, tex(drmdoztc6.tfm) = %{tl_version}
Provides:       tex(drmdoztc7.tfm) = %{tl_version}, tex(drmdoztc8.tfm) = %{tl_version}
Provides:       tex(drmdoztc9.tfm) = %{tl_version}, tex(drmdoztcbx10.tfm) = %{tl_version}
Provides:       tex(drmdoztcbx11.tfm) = %{tl_version}, tex(drmdoztcbx12.tfm) = %{tl_version}
Provides:       tex(drmdoztcbx14.tfm) = %{tl_version}, tex(drmdoztcbx17.tfm) = %{tl_version}
Provides:       tex(drmdoztcbx24.tfm) = %{tl_version}, tex(drmdoztcbx6.tfm) = %{tl_version}
Provides:       tex(drmdoztcbx7.tfm) = %{tl_version}, tex(drmdoztcbx8.tfm) = %{tl_version}
Provides:       tex(drmdoztcbx9.tfm) = %{tl_version}, tex(drmdozui10.tfm) = %{tl_version}
Provides:       tex(drmdozui11.tfm) = %{tl_version}, tex(drmdozui12.tfm) = %{tl_version}
Provides:       tex(drmdozui14.tfm) = %{tl_version}, tex(drmdozui17.tfm) = %{tl_version}
Provides:       tex(drmdozui24.tfm) = %{tl_version}, tex(drmdozui6.tfm) = %{tl_version}
Provides:       tex(drmdozui7.tfm) = %{tl_version}, tex(drmdozui8.tfm) = %{tl_version}
Provides:       tex(drmdozui9.tfm) = %{tl_version}, tex(drmdozuibx10.tfm) = %{tl_version}
Provides:       tex(drmdozuibx11.tfm) = %{tl_version}, tex(drmdozuibx12.tfm) = %{tl_version}
Provides:       tex(drmdozuibx14.tfm) = %{tl_version}, tex(drmdozuibx17.tfm) = %{tl_version}
Provides:       tex(drmdozuibx24.tfm) = %{tl_version}, tex(drmdozuibx6.tfm) = %{tl_version}
Provides:       tex(drmdozuibx7.tfm) = %{tl_version}, tex(drmdozuibx8.tfm) = %{tl_version}
Provides:       tex(drmdozuibx9.tfm) = %{tl_version}, tex(drmfigs10.tfm) = %{tl_version}
Provides:       tex(drmfigs11.tfm) = %{tl_version}, tex(drmfigs12.tfm) = %{tl_version}
Provides:       tex(drmfigs14.tfm) = %{tl_version}, tex(drmfigs17.tfm) = %{tl_version}
Provides:       tex(drmfigs24.tfm) = %{tl_version}, tex(drmfigs6.tfm) = %{tl_version}
Provides:       tex(drmfigs7.tfm) = %{tl_version}, tex(drmfigs8.tfm) = %{tl_version}
Provides:       tex(drmfigs9.tfm) = %{tl_version}, tex(drmgrk10.tfm) = %{tl_version}
Provides:       tex(drminf10.tfm) = %{tl_version}, tex(drminf11.tfm) = %{tl_version}
Provides:       tex(drminf12.tfm) = %{tl_version}, tex(drminf14.tfm) = %{tl_version}
Provides:       tex(drminf17.tfm) = %{tl_version}, tex(drminf24.tfm) = %{tl_version}
Provides:       tex(drminf6.tfm) = %{tl_version}, tex(drminf7.tfm) = %{tl_version}
Provides:       tex(drminf8.tfm) = %{tl_version}, tex(drminf9.tfm) = %{tl_version}
Provides:       tex(drmit10.tfm) = %{tl_version}, tex(drmit11.tfm) = %{tl_version}
Provides:       tex(drmit12.tfm) = %{tl_version}, tex(drmit14.tfm) = %{tl_version}
Provides:       tex(drmit17.tfm) = %{tl_version}, tex(drmit24.tfm) = %{tl_version}
Provides:       tex(drmit6.tfm) = %{tl_version}, tex(drmit7.tfm) = %{tl_version}
Provides:       tex(drmit8.tfm) = %{tl_version}, tex(drmit9.tfm) = %{tl_version}
Provides:       tex(drmitbx10.tfm) = %{tl_version}, tex(drmitbx11.tfm) = %{tl_version}
Provides:       tex(drmitbx12.tfm) = %{tl_version}, tex(drmitbx14.tfm) = %{tl_version}
Provides:       tex(drmitbx17.tfm) = %{tl_version}, tex(drmitbx24.tfm) = %{tl_version}
Provides:       tex(drmitbx6.tfm) = %{tl_version}, tex(drmitbx7.tfm) = %{tl_version}
Provides:       tex(drmitbx8.tfm) = %{tl_version}, tex(drmitbx9.tfm) = %{tl_version}
Provides:       tex(drmitsc10.tfm) = %{tl_version}, tex(drmitsc11.tfm) = %{tl_version}
Provides:       tex(drmitsc12.tfm) = %{tl_version}, tex(drmitsc14.tfm) = %{tl_version}
Provides:       tex(drmitsc17.tfm) = %{tl_version}, tex(drmitsc24.tfm) = %{tl_version}
Provides:       tex(drmitsc6.tfm) = %{tl_version}, tex(drmitsc7.tfm) = %{tl_version}
Provides:       tex(drmitsc8.tfm) = %{tl_version}, tex(drmitsc9.tfm) = %{tl_version}
Provides:       tex(drmittc10.tfm) = %{tl_version}, tex(drmittc11.tfm) = %{tl_version}
Provides:       tex(drmittc12.tfm) = %{tl_version}, tex(drmittc14.tfm) = %{tl_version}
Provides:       tex(drmittc17.tfm) = %{tl_version}, tex(drmittc24.tfm) = %{tl_version}
Provides:       tex(drmittc6.tfm) = %{tl_version}, tex(drmittc7.tfm) = %{tl_version}
Provides:       tex(drmittc8.tfm) = %{tl_version}, tex(drmittc9.tfm) = %{tl_version}
Provides:       tex(drml10.tfm) = %{tl_version}, tex(drml11.tfm) = %{tl_version}
Provides:       tex(drml12.tfm) = %{tl_version}, tex(drml14.tfm) = %{tl_version}
Provides:       tex(drml17.tfm) = %{tl_version}, tex(drml24.tfm) = %{tl_version}
Provides:       tex(drml6.tfm) = %{tl_version}, tex(drml7.tfm) = %{tl_version}
Provides:       tex(drml8.tfm) = %{tl_version}, tex(drml9.tfm) = %{tl_version}
Provides:       tex(drmmi10.tfm) = %{tl_version}, tex(drmomx10.tfm) = %{tl_version}
Provides:       tex(drmorns.tfm) = %{tl_version}, tex(drmsc10.tfm) = %{tl_version}
Provides:       tex(drmsc11.tfm) = %{tl_version}, tex(drmsc12.tfm) = %{tl_version}
Provides:       tex(drmsc14.tfm) = %{tl_version}, tex(drmsc17.tfm) = %{tl_version}
Provides:       tex(drmsc24.tfm) = %{tl_version}, tex(drmsc6.tfm) = %{tl_version}
Provides:       tex(drmsc7.tfm) = %{tl_version}, tex(drmsc8.tfm) = %{tl_version}
Provides:       tex(drmsc9.tfm) = %{tl_version}, tex(drmscbx10.tfm) = %{tl_version}
Provides:       tex(drmscbx11.tfm) = %{tl_version}, tex(drmscbx12.tfm) = %{tl_version}
Provides:       tex(drmscbx14.tfm) = %{tl_version}, tex(drmscbx17.tfm) = %{tl_version}
Provides:       tex(drmscbx24.tfm) = %{tl_version}, tex(drmscbx6.tfm) = %{tl_version}
Provides:       tex(drmscbx7.tfm) = %{tl_version}, tex(drmscbx8.tfm) = %{tl_version}
Provides:       tex(drmscbx9.tfm) = %{tl_version}, tex(drmsl10.tfm) = %{tl_version}
Provides:       tex(drmsl11.tfm) = %{tl_version}, tex(drmsl12.tfm) = %{tl_version}
Provides:       tex(drmsl14.tfm) = %{tl_version}, tex(drmsl17.tfm) = %{tl_version}
Provides:       tex(drmsl24.tfm) = %{tl_version}, tex(drmsl6.tfm) = %{tl_version}
Provides:       tex(drmsl7.tfm) = %{tl_version}, tex(drmsl8.tfm) = %{tl_version}
Provides:       tex(drmsl9.tfm) = %{tl_version}, tex(drmsy10.tfm) = %{tl_version}
Provides:       tex(drmsym10.tfm) = %{tl_version}, tex(drmsym11.tfm) = %{tl_version}
Provides:       tex(drmsym12.tfm) = %{tl_version}, tex(drmsym14.tfm) = %{tl_version}
Provides:       tex(drmsym17.tfm) = %{tl_version}, tex(drmsym24.tfm) = %{tl_version}
Provides:       tex(drmsym7.tfm) = %{tl_version}, tex(drmsym8.tfm) = %{tl_version}
Provides:       tex(drmsym9.tfm) = %{tl_version}, tex(drmtc10.tfm) = %{tl_version}
Provides:       tex(drmtc11.tfm) = %{tl_version}, tex(drmtc12.tfm) = %{tl_version}
Provides:       tex(drmtc14.tfm) = %{tl_version}, tex(drmtc17.tfm) = %{tl_version}
Provides:       tex(drmtc24.tfm) = %{tl_version}, tex(drmtc6.tfm) = %{tl_version}
Provides:       tex(drmtc7.tfm) = %{tl_version}, tex(drmtc8.tfm) = %{tl_version}
Provides:       tex(drmtc9.tfm) = %{tl_version}, tex(drmtcbx10.tfm) = %{tl_version}
Provides:       tex(drmtcbx11.tfm) = %{tl_version}, tex(drmtcbx12.tfm) = %{tl_version}
Provides:       tex(drmtcbx14.tfm) = %{tl_version}, tex(drmtcbx17.tfm) = %{tl_version}
Provides:       tex(drmtcbx24.tfm) = %{tl_version}, tex(drmtcbx6.tfm) = %{tl_version}
Provides:       tex(drmtcbx7.tfm) = %{tl_version}, tex(drmtcbx8.tfm) = %{tl_version}
Provides:       tex(drmtcbx9.tfm) = %{tl_version}, tex(drmui10.tfm) = %{tl_version}
Provides:       tex(drmui11.tfm) = %{tl_version}, tex(drmui12.tfm) = %{tl_version}
Provides:       tex(drmui14.tfm) = %{tl_version}, tex(drmui17.tfm) = %{tl_version}
Provides:       tex(drmui24.tfm) = %{tl_version}, tex(drmui6.tfm) = %{tl_version}
Provides:       tex(drmui7.tfm) = %{tl_version}, tex(drmui8.tfm) = %{tl_version}
Provides:       tex(drmui9.tfm) = %{tl_version}, tex(drmuibx10.tfm) = %{tl_version}
Provides:       tex(drmuibx11.tfm) = %{tl_version}, tex(drmuibx12.tfm) = %{tl_version}
Provides:       tex(drmuibx14.tfm) = %{tl_version}, tex(drmuibx17.tfm) = %{tl_version}
Provides:       tex(drmuibx24.tfm) = %{tl_version}, tex(drmuibx6.tfm) = %{tl_version}
Provides:       tex(drmuibx7.tfm) = %{tl_version}, tex(drmuibx8.tfm) = %{tl_version}
Provides:       tex(drmuibx9.tfm) = %{tl_version}, tex(drm10.pfb) = %{tl_version}
Provides:       tex(drm11.pfb) = %{tl_version}, tex(drm12.pfb) = %{tl_version}
Provides:       tex(drm14.pfb) = %{tl_version}, tex(drm17.pfb) = %{tl_version}
Provides:       tex(drm24.pfb) = %{tl_version}, tex(drm6.pfb) = %{tl_version}
Provides:       tex(drm7.pfb) = %{tl_version}, tex(drm8.pfb) = %{tl_version}
Provides:       tex(drm9.pfb) = %{tl_version}, tex(drmb10.pfb) = %{tl_version}
Provides:       tex(drmb11.pfb) = %{tl_version}, tex(drmb12.pfb) = %{tl_version}
Provides:       tex(drmb14.pfb) = %{tl_version}, tex(drmb17.pfb) = %{tl_version}
Provides:       tex(drmb24.pfb) = %{tl_version}, tex(drmb6.pfb) = %{tl_version}
Provides:       tex(drmb7.pfb) = %{tl_version}, tex(drmb8.pfb) = %{tl_version}
Provides:       tex(drmb9.pfb) = %{tl_version}, tex(drmbx10.pfb) = %{tl_version}
Provides:       tex(drmbx11.pfb) = %{tl_version}, tex(drmbx12.pfb) = %{tl_version}
Provides:       tex(drmbx14.pfb) = %{tl_version}, tex(drmbx17.pfb) = %{tl_version}
Provides:       tex(drmbx24.pfb) = %{tl_version}, tex(drmbx6.pfb) = %{tl_version}
Provides:       tex(drmbx7.pfb) = %{tl_version}, tex(drmbx8.pfb) = %{tl_version}
Provides:       tex(drmbx9.pfb) = %{tl_version}, tex(drmdoz10.pfb) = %{tl_version}
Provides:       tex(drmdoz11.pfb) = %{tl_version}, tex(drmdoz12.pfb) = %{tl_version}
Provides:       tex(drmdoz14.pfb) = %{tl_version}, tex(drmdoz17.pfb) = %{tl_version}
Provides:       tex(drmdoz24.pfb) = %{tl_version}, tex(drmdoz6.pfb) = %{tl_version}
Provides:       tex(drmdoz7.pfb) = %{tl_version}, tex(drmdoz8.pfb) = %{tl_version}
Provides:       tex(drmdoz9.pfb) = %{tl_version}, tex(drmdozb10.pfb) = %{tl_version}
Provides:       tex(drmdozb11.pfb) = %{tl_version}, tex(drmdozb12.pfb) = %{tl_version}
Provides:       tex(drmdozb14.pfb) = %{tl_version}, tex(drmdozb17.pfb) = %{tl_version}
Provides:       tex(drmdozb24.pfb) = %{tl_version}, tex(drmdozb6.pfb) = %{tl_version}
Provides:       tex(drmdozb7.pfb) = %{tl_version}, tex(drmdozb8.pfb) = %{tl_version}
Provides:       tex(drmdozb9.pfb) = %{tl_version}, tex(drmdozbx10.pfb) = %{tl_version}
Provides:       tex(drmdozbx11.pfb) = %{tl_version}, tex(drmdozbx12.pfb) = %{tl_version}
Provides:       tex(drmdozbx14.pfb) = %{tl_version}, tex(drmdozbx17.pfb) = %{tl_version}
Provides:       tex(drmdozbx24.pfb) = %{tl_version}, tex(drmdozbx6.pfb) = %{tl_version}
Provides:       tex(drmdozbx7.pfb) = %{tl_version}, tex(drmdozbx8.pfb) = %{tl_version}
Provides:       tex(drmdozbx9.pfb) = %{tl_version}, tex(drmdozit10.pfb) = %{tl_version}
Provides:       tex(drmdozit11.pfb) = %{tl_version}, tex(drmdozit12.pfb) = %{tl_version}
Provides:       tex(drmdozit14.pfb) = %{tl_version}, tex(drmdozit17.pfb) = %{tl_version}
Provides:       tex(drmdozit24.pfb) = %{tl_version}, tex(drmdozit6.pfb) = %{tl_version}
Provides:       tex(drmdozit7.pfb) = %{tl_version}, tex(drmdozit8.pfb) = %{tl_version}
Provides:       tex(drmdozit9.pfb) = %{tl_version}, tex(drmdozitbx10.pfb) = %{tl_version}
Provides:       tex(drmdozitbx11.pfb) = %{tl_version}, tex(drmdozitbx12.pfb) = %{tl_version}
Provides:       tex(drmdozitbx14.pfb) = %{tl_version}, tex(drmdozitbx17.pfb) = %{tl_version}
Provides:       tex(drmdozitbx24.pfb) = %{tl_version}, tex(drmdozitbx6.pfb) = %{tl_version}
Provides:       tex(drmdozitbx7.pfb) = %{tl_version}, tex(drmdozitbx8.pfb) = %{tl_version}
Provides:       tex(drmdozitbx9.pfb) = %{tl_version}, tex(drmdozitsc10.pfb) = %{tl_version}
Provides:       tex(drmdozitsc11.pfb) = %{tl_version}, tex(drmdozitsc12.pfb) = %{tl_version}
Provides:       tex(drmdozitsc14.pfb) = %{tl_version}, tex(drmdozitsc17.pfb) = %{tl_version}
Provides:       tex(drmdozitsc24.pfb) = %{tl_version}, tex(drmdozitsc6.pfb) = %{tl_version}
Provides:       tex(drmdozitsc7.pfb) = %{tl_version}, tex(drmdozitsc8.pfb) = %{tl_version}
Provides:       tex(drmdozitsc9.pfb) = %{tl_version}, tex(drmdozittc10.pfb) = %{tl_version}
Provides:       tex(drmdozittc11.pfb) = %{tl_version}, tex(drmdozittc12.pfb) = %{tl_version}
Provides:       tex(drmdozittc14.pfb) = %{tl_version}, tex(drmdozittc17.pfb) = %{tl_version}
Provides:       tex(drmdozittc24.pfb) = %{tl_version}, tex(drmdozittc6.pfb) = %{tl_version}
Provides:       tex(drmdozittc7.pfb) = %{tl_version}, tex(drmdozittc8.pfb) = %{tl_version}
Provides:       tex(drmdozittc9.pfb) = %{tl_version}, tex(drmdozl10.pfb) = %{tl_version}
Provides:       tex(drmdozl11.pfb) = %{tl_version}, tex(drmdozl12.pfb) = %{tl_version}
Provides:       tex(drmdozl14.pfb) = %{tl_version}, tex(drmdozl17.pfb) = %{tl_version}
Provides:       tex(drmdozl24.pfb) = %{tl_version}, tex(drmdozl6.pfb) = %{tl_version}
Provides:       tex(drmdozl7.pfb) = %{tl_version}, tex(drmdozl8.pfb) = %{tl_version}
Provides:       tex(drmdozl9.pfb) = %{tl_version}, tex(drmdozsc10.pfb) = %{tl_version}
Provides:       tex(drmdozsc11.pfb) = %{tl_version}, tex(drmdozsc12.pfb) = %{tl_version}
Provides:       tex(drmdozsc14.pfb) = %{tl_version}, tex(drmdozsc17.pfb) = %{tl_version}
Provides:       tex(drmdozsc24.pfb) = %{tl_version}, tex(drmdozsc6.pfb) = %{tl_version}
Provides:       tex(drmdozsc7.pfb) = %{tl_version}, tex(drmdozsc8.pfb) = %{tl_version}
Provides:       tex(drmdozsc9.pfb) = %{tl_version}, tex(drmdozscbx10.pfb) = %{tl_version}
Provides:       tex(drmdozscbx11.pfb) = %{tl_version}, tex(drmdozscbx12.pfb) = %{tl_version}
Provides:       tex(drmdozscbx14.pfb) = %{tl_version}, tex(drmdozscbx17.pfb) = %{tl_version}
Provides:       tex(drmdozscbx24.pfb) = %{tl_version}, tex(drmdozscbx6.pfb) = %{tl_version}
Provides:       tex(drmdozscbx7.pfb) = %{tl_version}, tex(drmdozscbx8.pfb) = %{tl_version}
Provides:       tex(drmdozscbx9.pfb) = %{tl_version}, tex(drmdozsl10.pfb) = %{tl_version}
Provides:       tex(drmdozsl11.pfb) = %{tl_version}, tex(drmdozsl12.pfb) = %{tl_version}
Provides:       tex(drmdozsl14.pfb) = %{tl_version}, tex(drmdozsl17.pfb) = %{tl_version}
Provides:       tex(drmdozsl24.pfb) = %{tl_version}, tex(drmdozsl6.pfb) = %{tl_version}
Provides:       tex(drmdozsl7.pfb) = %{tl_version}, tex(drmdozsl8.pfb) = %{tl_version}
Provides:       tex(drmdozsl9.pfb) = %{tl_version}, tex(drmdoztc10.pfb) = %{tl_version}
Provides:       tex(drmdoztc11.pfb) = %{tl_version}, tex(drmdoztc12.pfb) = %{tl_version}
Provides:       tex(drmdoztc14.pfb) = %{tl_version}, tex(drmdoztc17.pfb) = %{tl_version}
Provides:       tex(drmdoztc24.pfb) = %{tl_version}, tex(drmdoztc6.pfb) = %{tl_version}
Provides:       tex(drmdoztc7.pfb) = %{tl_version}, tex(drmdoztc8.pfb) = %{tl_version}
Provides:       tex(drmdoztc9.pfb) = %{tl_version}, tex(drmdoztcbx10.pfb) = %{tl_version}
Provides:       tex(drmdoztcbx11.pfb) = %{tl_version}, tex(drmdoztcbx12.pfb) = %{tl_version}
Provides:       tex(drmdoztcbx14.pfb) = %{tl_version}, tex(drmdoztcbx17.pfb) = %{tl_version}
Provides:       tex(drmdoztcbx24.pfb) = %{tl_version}, tex(drmdoztcbx6.pfb) = %{tl_version}
Provides:       tex(drmdoztcbx7.pfb) = %{tl_version}, tex(drmdoztcbx8.pfb) = %{tl_version}
Provides:       tex(drmdoztcbx9.pfb) = %{tl_version}, tex(drmdozui10.pfb) = %{tl_version}
Provides:       tex(drmdozui11.pfb) = %{tl_version}, tex(drmdozui12.pfb) = %{tl_version}
Provides:       tex(drmdozui14.pfb) = %{tl_version}, tex(drmdozui17.pfb) = %{tl_version}
Provides:       tex(drmdozui24.pfb) = %{tl_version}, tex(drmdozui6.pfb) = %{tl_version}
Provides:       tex(drmdozui7.pfb) = %{tl_version}, tex(drmdozui8.pfb) = %{tl_version}
Provides:       tex(drmdozui9.pfb) = %{tl_version}, tex(drmdozuibx10.pfb) = %{tl_version}
Provides:       tex(drmdozuibx11.pfb) = %{tl_version}, tex(drmdozuibx12.pfb) = %{tl_version}
Provides:       tex(drmdozuibx14.pfb) = %{tl_version}, tex(drmdozuibx17.pfb) = %{tl_version}
Provides:       tex(drmdozuibx24.pfb) = %{tl_version}, tex(drmdozuibx6.pfb) = %{tl_version}
Provides:       tex(drmdozuibx7.pfb) = %{tl_version}, tex(drmdozuibx8.pfb) = %{tl_version}
Provides:       tex(drmdozuibx9.pfb) = %{tl_version}, tex(drmfigs10.pfb) = %{tl_version}
Provides:       tex(drmfigs11.pfb) = %{tl_version}, tex(drmfigs12.pfb) = %{tl_version}
Provides:       tex(drmfigs14.pfb) = %{tl_version}, tex(drmfigs17.pfb) = %{tl_version}
Provides:       tex(drmfigs24.pfb) = %{tl_version}, tex(drmfigs6.pfb) = %{tl_version}
Provides:       tex(drmfigs7.pfb) = %{tl_version}, tex(drmfigs8.pfb) = %{tl_version}
Provides:       tex(drmfigs9.pfb) = %{tl_version}, tex(drmgrk10.pfb) = %{tl_version}
Provides:       tex(drminf10.pfb) = %{tl_version}, tex(drminf11.pfb) = %{tl_version}
Provides:       tex(drminf12.pfb) = %{tl_version}, tex(drminf14.pfb) = %{tl_version}
Provides:       tex(drminf17.pfb) = %{tl_version}, tex(drminf24.pfb) = %{tl_version}
Provides:       tex(drminf6.pfb) = %{tl_version}, tex(drminf7.pfb) = %{tl_version}
Provides:       tex(drminf8.pfb) = %{tl_version}, tex(drminf9.pfb) = %{tl_version}
Provides:       tex(drmit10.pfb) = %{tl_version}, tex(drmit11.pfb) = %{tl_version}
Provides:       tex(drmit12.pfb) = %{tl_version}, tex(drmit14.pfb) = %{tl_version}
Provides:       tex(drmit17.pfb) = %{tl_version}, tex(drmit24.pfb) = %{tl_version}
Provides:       tex(drmit6.pfb) = %{tl_version}, tex(drmit7.pfb) = %{tl_version}
Provides:       tex(drmit8.pfb) = %{tl_version}, tex(drmit9.pfb) = %{tl_version}
Provides:       tex(drmitbx10.pfb) = %{tl_version}, tex(drmitbx11.pfb) = %{tl_version}
Provides:       tex(drmitbx12.pfb) = %{tl_version}, tex(drmitbx14.pfb) = %{tl_version}
Provides:       tex(drmitbx17.pfb) = %{tl_version}, tex(drmitbx24.pfb) = %{tl_version}
Provides:       tex(drmitbx6.pfb) = %{tl_version}, tex(drmitbx7.pfb) = %{tl_version}
Provides:       tex(drmitbx8.pfb) = %{tl_version}, tex(drmitbx9.pfb) = %{tl_version}
Provides:       tex(drmitsc10.pfb) = %{tl_version}, tex(drmitsc11.pfb) = %{tl_version}
Provides:       tex(drmitsc12.pfb) = %{tl_version}, tex(drmitsc14.pfb) = %{tl_version}
Provides:       tex(drmitsc17.pfb) = %{tl_version}, tex(drmitsc24.pfb) = %{tl_version}
Provides:       tex(drmitsc6.pfb) = %{tl_version}, tex(drmitsc7.pfb) = %{tl_version}
Provides:       tex(drmitsc8.pfb) = %{tl_version}, tex(drmitsc9.pfb) = %{tl_version}
Provides:       tex(drmittc10.pfb) = %{tl_version}, tex(drmittc11.pfb) = %{tl_version}
Provides:       tex(drmittc12.pfb) = %{tl_version}, tex(drmittc14.pfb) = %{tl_version}
Provides:       tex(drmittc17.pfb) = %{tl_version}, tex(drmittc24.pfb) = %{tl_version}
Provides:       tex(drmittc6.pfb) = %{tl_version}, tex(drmittc7.pfb) = %{tl_version}
Provides:       tex(drmittc8.pfb) = %{tl_version}, tex(drmittc9.pfb) = %{tl_version}
Provides:       tex(drml10.pfb) = %{tl_version}, tex(drml11.pfb) = %{tl_version}
Provides:       tex(drml12.pfb) = %{tl_version}, tex(drml14.pfb) = %{tl_version}
Provides:       tex(drml17.pfb) = %{tl_version}, tex(drml24.pfb) = %{tl_version}
Provides:       tex(drml6.pfb) = %{tl_version}, tex(drml7.pfb) = %{tl_version}
Provides:       tex(drml8.pfb) = %{tl_version}, tex(drml9.pfb) = %{tl_version}
Provides:       tex(drmmi10.pfb) = %{tl_version}, tex(drmsc10.pfb) = %{tl_version}
Provides:       tex(drmsc11.pfb) = %{tl_version}, tex(drmsc12.pfb) = %{tl_version}
Provides:       tex(drmsc14.pfb) = %{tl_version}, tex(drmsc17.pfb) = %{tl_version}
Provides:       tex(drmsc24.pfb) = %{tl_version}, tex(drmsc6.pfb) = %{tl_version}
Provides:       tex(drmsc7.pfb) = %{tl_version}, tex(drmsc8.pfb) = %{tl_version}
Provides:       tex(drmsc9.pfb) = %{tl_version}, tex(drmscbx10.pfb) = %{tl_version}
Provides:       tex(drmscbx11.pfb) = %{tl_version}, tex(drmscbx12.pfb) = %{tl_version}
Provides:       tex(drmscbx14.pfb) = %{tl_version}, tex(drmscbx17.pfb) = %{tl_version}
Provides:       tex(drmscbx24.pfb) = %{tl_version}, tex(drmscbx6.pfb) = %{tl_version}
Provides:       tex(drmscbx7.pfb) = %{tl_version}, tex(drmscbx8.pfb) = %{tl_version}
Provides:       tex(drmscbx9.pfb) = %{tl_version}, tex(drmsl10.pfb) = %{tl_version}
Provides:       tex(drmsl11.pfb) = %{tl_version}, tex(drmsl12.pfb) = %{tl_version}
Provides:       tex(drmsl14.pfb) = %{tl_version}, tex(drmsl17.pfb) = %{tl_version}
Provides:       tex(drmsl24.pfb) = %{tl_version}, tex(drmsl6.pfb) = %{tl_version}
Provides:       tex(drmsl7.pfb) = %{tl_version}, tex(drmsl8.pfb) = %{tl_version}
Provides:       tex(drmsl9.pfb) = %{tl_version}, tex(drmsy10.pfb) = %{tl_version}
Provides:       tex(drmsym10.pfb) = %{tl_version}, tex(drmsym11.pfb) = %{tl_version}
Provides:       tex(drmsym12.pfb) = %{tl_version}, tex(drmsym14.pfb) = %{tl_version}
Provides:       tex(drmsym17.pfb) = %{tl_version}, tex(drmsym24.pfb) = %{tl_version}
Provides:       tex(drmsym7.pfb) = %{tl_version}, tex(drmsym8.pfb) = %{tl_version}
Provides:       tex(drmsym9.pfb) = %{tl_version}, tex(drmtc10.pfb) = %{tl_version}
Provides:       tex(drmtc11.pfb) = %{tl_version}, tex(drmtc12.pfb) = %{tl_version}
Provides:       tex(drmtc14.pfb) = %{tl_version}, tex(drmtc17.pfb) = %{tl_version}
Provides:       tex(drmtc24.pfb) = %{tl_version}, tex(drmtc6.pfb) = %{tl_version}
Provides:       tex(drmtc7.pfb) = %{tl_version}, tex(drmtc8.pfb) = %{tl_version}
Provides:       tex(drmtc9.pfb) = %{tl_version}, tex(drmtcbx10.pfb) = %{tl_version}
Provides:       tex(drmtcbx11.pfb) = %{tl_version}, tex(drmtcbx12.pfb) = %{tl_version}
Provides:       tex(drmtcbx14.pfb) = %{tl_version}, tex(drmtcbx17.pfb) = %{tl_version}
Provides:       tex(drmtcbx24.pfb) = %{tl_version}, tex(drmtcbx6.pfb) = %{tl_version}
Provides:       tex(drmtcbx7.pfb) = %{tl_version}, tex(drmtcbx8.pfb) = %{tl_version}
Provides:       tex(drmtcbx9.pfb) = %{tl_version}, tex(drmui10.pfb) = %{tl_version}
Provides:       tex(drmui11.pfb) = %{tl_version}, tex(drmui12.pfb) = %{tl_version}
Provides:       tex(drmui14.pfb) = %{tl_version}, tex(drmui17.pfb) = %{tl_version}
Provides:       tex(drmui24.pfb) = %{tl_version}, tex(drmui6.pfb) = %{tl_version}
Provides:       tex(drmui7.pfb) = %{tl_version}, tex(drmui8.pfb) = %{tl_version}
Provides:       tex(drmui9.pfb) = %{tl_version}, tex(drmuibx10.pfb) = %{tl_version}
Provides:       tex(drmuibx11.pfb) = %{tl_version}, tex(drmuibx12.pfb) = %{tl_version}
Provides:       tex(drmuibx14.pfb) = %{tl_version}, tex(drmuibx17.pfb) = %{tl_version}
Provides:       tex(drmuibx24.pfb) = %{tl_version}, tex(drmuibx6.pfb) = %{tl_version}
Provides:       tex(drmuibx7.pfb) = %{tl_version}, tex(drmuibx8.pfb) = %{tl_version}
Provides:       tex(drmuibx9.pfb) = %{tl_version}, tex(drm.sty) = %{tl_version}

%description -n texlive-drm
The package provides access to the DRM (Don's Revised Modern)
family of fonts, which includes a variety of optical sizes in
Roman (in four weights), italic, and small caps, among other
shapes, along with a set of symbols and ornaments. It is
intended to be a full-body text font, but its larger sizes can
also be used for simple display purposes, and its significant
body of symbols can stand on its own. It comes complete with
textual ("old-style") and lining figures, and even has small-
caps figures. It also comes with extensible decorative rules to
be used with ornaments from itself or other fonts, along with
an extremely flexible ellipsis package.

%package -n texlive-drm-doc
Summary:        Documentation for drm
Version:        svn38157.4.4

Provides:       tex-drm-doc
AutoReqProv:    No

%description -n texlive-drm-doc
Documentation for drm

%package -n texlive-droid
Provides:       tex-droid = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX support for the Droid font families
Version:        svn23912.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(droidsans.sty), tex(keyval.sty), tex(slantsc.sty)
Provides:       tex(droid-01.enc) = %{tl_version}, tex(droid-02.enc) = %{tl_version}
Provides:       tex(droid-03.enc) = %{tl_version}, tex(droid-04.enc) = %{tl_version}
Provides:       tex(droid.map) = %{tl_version}, tex(DroidSans-01.tfm) = %{tl_version}
Provides:       tex(DroidSans-02.tfm) = %{tl_version}, tex(DroidSans-03.tfm) = %{tl_version}
Provides:       tex(DroidSans-04.tfm) = %{tl_version}, tex(DroidSans-Bold-01.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-02.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-03.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-04.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-01.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-02.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-03.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-04.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-01.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-02.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-03.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-04.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSans-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-lgr.tfm) = %{tl_version}, tex(DroidSans-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSans-t1.tfm) = %{tl_version}, tex(DroidSans-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSans-t2b.tfm) = %{tl_version}, tex(DroidSans-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSans-ts1.tfm) = %{tl_version}, tex(DroidSans-x2.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-01.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-02.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-03.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-04.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-01.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-02.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-03.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-04.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-t1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSansMono-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Bold-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Italic-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-01.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-02.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-03.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-04.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-lgr.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(DroidSerif-Regular-x2.tfm) = %{tl_version}
Provides:       tex(DroidSans-Bold.ttf) = %{tl_version}, tex(DroidSans.ttf) = %{tl_version}
Provides:       tex(DroidSansMono.ttf) = %{tl_version}, tex(DroidSerif-Bold.ttf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic.ttf) = %{tl_version}
Provides:       tex(DroidSerif-Italic.ttf) = %{tl_version}
Provides:       tex(DroidSerif-Regular.ttf) = %{tl_version}
Provides:       tex(DroidSans-Bold.pfb) = %{tl_version}, tex(DroidSans.pfb) = %{tl_version}
Provides:       tex(DroidSansMono.pfb) = %{tl_version}, tex(DroidSerif-Bold.pfb) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic.pfb) = %{tl_version}
Provides:       tex(DroidSerif-Italic.pfb) = %{tl_version}
Provides:       tex(DroidSerif-Regular.pfb) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-Slanted-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-ts1.vf) = %{tl_version}
Provides:       tex(DroidSans-Bold-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(DroidSans-Slanted-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSans-lgr.vf) = %{tl_version}, tex(DroidSans-ot1.vf) = %{tl_version}
Provides:       tex(DroidSans-t1.vf) = %{tl_version}, tex(DroidSans-t2a.vf) = %{tl_version}
Provides:       tex(DroidSans-t2b.vf) = %{tl_version}, tex(DroidSans-t2c.vf) = %{tl_version}
Provides:       tex(DroidSans-ts1.vf) = %{tl_version}, tex(DroidSans-x2.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-Slanted-x2.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSansMono-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSansMono-lgr.vf) = %{tl_version}
Provides:       tex(DroidSansMono-ot1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-t1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-t2a.vf) = %{tl_version}
Provides:       tex(DroidSansMono-t2b.vf) = %{tl_version}
Provides:       tex(DroidSansMono-t2c.vf) = %{tl_version}
Provides:       tex(DroidSansMono-ts1.vf) = %{tl_version}
Provides:       tex(DroidSansMono-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-Slanted-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Bold-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-Upright-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-BoldItalic-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-Upright-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Italic-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-Slanted-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-lgr.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-ot1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2a.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2b.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-t2c.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-ts1.vf) = %{tl_version}
Provides:       tex(DroidSerif-Regular-x2.vf) = %{tl_version}
Provides:       tex(droid.sty) = %{tl_version}, tex(droidmono.sty) = %{tl_version}
Provides:       tex(droidsans.sty) = %{tl_version}, tex(droidserif.sty) = %{tl_version}
Provides:       tex(lgrfdm.fd) = %{tl_version}, tex(lgrfdr.fd) = %{tl_version}
Provides:       tex(lgrfds.fd) = %{tl_version}, tex(ot1fdm.fd) = %{tl_version}
Provides:       tex(ot1fdr.fd) = %{tl_version}, tex(ot1fds.fd) = %{tl_version}
Provides:       tex(t1fdm.fd) = %{tl_version}, tex(t1fdr.fd) = %{tl_version}
Provides:       tex(t1fds.fd) = %{tl_version}, tex(t2afdm.fd) = %{tl_version}
Provides:       tex(t2afdr.fd) = %{tl_version}, tex(t2afds.fd) = %{tl_version}
Provides:       tex(t2bfdm.fd) = %{tl_version}, tex(t2bfdr.fd) = %{tl_version}
Provides:       tex(t2bfds.fd) = %{tl_version}, tex(t2cfdm.fd) = %{tl_version}
Provides:       tex(t2cfdr.fd) = %{tl_version}, tex(t2cfds.fd) = %{tl_version}
Provides:       tex(ts1fdm.fd) = %{tl_version}, tex(ts1fdr.fd) = %{tl_version}
Provides:       tex(ts1fds.fd) = %{tl_version}, tex(x2fdm.fd) = %{tl_version}
Provides:       tex(x2fdr.fd) = %{tl_version}, tex(x2fds.fd) = %{tl_version}

%description -n texlive-droid
The Droid typeface family was designed in the fall of 2006 by
Steve Matteson, as a commission from Google to create a set of
system fonts for its Android platform. The goal was to provide
optimal quality and comfort on a mobile handset when rendered
in application menus, web browsers and for other screen text.
The Droid family consists of Droid Serif, Droid Sans and Droid
Sans Mono fonts, licensed under the Apache License Version 2.0.
The bundle includes the fonts in both TrueType and Adobe Type 1
formats. The package does not support the Droid Pro family of
fonts, available for purchase from the Ascender foundry.

%package -n texlive-droid-doc
Summary:        Documentation for droid
Version:        svn23912.2.1

Provides:       tex-droid-doc
AutoReqProv:    No

%description -n texlive-droid-doc
Documentation for droid

%package -n texlive-duerer
Provides:       tex-duerer = %{tl_version}
License:        Public Domain
Summary:        Computer Duerer fonts
Version:        svn20741.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cdb10.tfm) = %{tl_version}, tex(cdi10.tfm) = %{tl_version}
Provides:       tex(cdr10.tfm) = %{tl_version}, tex(cdsl10.tfm) = %{tl_version}
Provides:       tex(cdss10.tfm) = %{tl_version}, tex(cdtt10.tfm) = %{tl_version}

%description -n texlive-duerer
These fonts are designed for titling use, and consist of
capital roman letters only. Together with the normal set of
base shapes, the family also offers an informal shape. The
distribution is as Metafont source. LaTeX support is available
in the duerer-latex bundle.

%package -n texlive-duerer-doc
Summary:        Documentation for duerer
Version:        svn20741.0

Provides:       tex-duerer-doc
AutoReqProv:    No

%description -n texlive-duerer-doc
Documentation for duerer

%package -n texlive-duerer-latex
Provides:       tex-duerer-latex = %{tl_version}
License:        GPL+
Summary:        LaTeX support for the Duerer fonts
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(duerer.sty) = %{tl_version}, tex(ot1cdin.fd) = %{tl_version}
Provides:       tex(ot1cdr.fd) = %{tl_version}, tex(ot1cdss.fd) = %{tl_version}
Provides:       tex(ot1cdtt.fd) = %{tl_version}

%description -n texlive-duerer-latex
LaTeX support for Hoenig's Computer Duerer fonts, using their
standard fontname names.

%package -n texlive-duerer-latex-doc
Summary:        Documentation for duerer-latex
Version:        svn15878.1.1

Provides:       tex-duerer-latex-doc
AutoReqProv:    No

%description -n texlive-duerer-latex-doc
Documentation for duerer-latex

%package -n texlive-dutchcal
Provides:       tex-dutchcal = %{tl_version}
License:        LPPL
Summary:        A reworking of ESSTIX13, adding a bold version
Version:        svn23448.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty)
Provides:       tex(dutchcal.map) = %{tl_version}, tex(dutchcal-b.tfm) = %{tl_version}
Provides:       tex(dutchcal-r.tfm) = %{tl_version}, tex(rdutchcalb.tfm) = %{tl_version}
Provides:       tex(rdutchcalr.tfm) = %{tl_version}, tex(DutchCalBold.pfb) = %{tl_version}
Provides:       tex(DutchCalReg.pfb) = %{tl_version}, tex(dutchcal-b.vf) = %{tl_version}
Provides:       tex(dutchcal-r.vf) = %{tl_version}, tex(dutchcal.sty) = %{tl_version}
Provides:       tex(udutchcal.fd) = %{tl_version}

%description -n texlive-dutchcal
This package reworks the mathematical calligraphic font
ESSTIX13, adding a bold version. LaTeX support files are
included. The new fonts may also be accessed from the most
recent version of mathalfa. The fonts themselves are subject to
the SIL OPEN FONT LICENSE, version 1.1.

%package -n texlive-dutchcal-doc
Summary:        Documentation for dutchcal
Version:        svn23448.1.0

Provides:       tex-dutchcal-doc
AutoReqProv:    No

%description -n texlive-dutchcal-doc
Documentation for dutchcal


%package -n texlive-dvipsconfig
Provides:       tex-dvipsconfig = %{tl_version}
License:        GPL+
Summary:        Collection of dvips PostScript headers
Version:        svn13293.1.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-dvipsconfig
This is a collection of dvips PostScript header and dvips
config files. They control certain features of the printer,
including: A4, A3, usletter, simplex, duplex / long edge,
duplex / short edge, screen frequencies of images, black/white
invers, select transparency / paper for tektronix 550/560,
manual feeder, envelope feeder, and tray 1, 2 and 3, and
printing a PostScript grid underneath the page material--very
useful for measuring and eliminating paper feed errors!

%package -n texlive-dinat
Provides:       tex-dinat = %{tl_version}
License:        Public Domain
Summary:        Bibliography style for German texts
Version:        svn15878.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-dinat
Bibliography style files intended for texts in german. They
draw up bibliographies in accordance with the german DIN 1505,
parts 2 and 3.

%package -n texlive-dinat-doc
Summary:        Documentation for dinat
Version:        svn15878.2.5

Provides:       tex-dinat-doc
AutoReqProv:    No

%description -n texlive-dinat-doc
Documentation for dinat

%package -n texlive-dirtree
Provides:       tex-dirtree = %{tl_version}
License:        LPPL
Summary:        Display trees in the style of windows explorer
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(dirtree.sty) = %{tl_version}, tex(dirtree.tex) = %{tl_version}

%description -n texlive-dirtree
This package is designed to emulate the way windows explorer
displays directory and file trees, with the root at top left,
and each level of subtree displaying one step in to the right.
The macros work equally well with Plain TeX and with LaTeX.

%package -n texlive-dirtree-doc
Summary:        Documentation for dirtree
Version:        svn42428
Provides:       tex-dirtree-doc
AutoReqProv:    No

%description -n texlive-dirtree-doc
Documentation for dirtree

%package -n texlive-docbytex
Provides:       tex-docbytex = %{tl_version}
License:        Copyright only
Summary:        Creating documentation from source code
Version:        svn34294.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(docby.tex) = %{tl_version}

%description -n texlive-docbytex
The package creates documentation from C source code, or other
programming languages.

%package -n texlive-docbytex-doc
Summary:        Documentation for docbytex
Version:        svn34294.0

Provides:       tex-docbytex-doc
AutoReqProv:    No

%description -n texlive-docbytex-doc
Documentation for docbytex

%package -n texlive-dowith
Provides:       tex-dowith = %{tl_version}
License:        LPPL 1.3
Summary:        Apply a command to a list of items
Version:        svn38860

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(plainpkg.tex)
Provides:       tex(domore.sty) = %{tl_version}, tex(dowith.sty) = %{tl_version}

%description -n texlive-dowith
The package provides macros for applying a command to all
elements of a list without separators, such as
'\DoWithAllIn{<cmd>}{<list-macro>}', and also for extending and
reducing macros storing such lists. Applications in mind
belonged to LaTeX, but the package should work with other
formats as well. Loop and list macros in other packages are
discussed. A further package, domore, is also provided, which
enhances the functionality of dowith.

%package -n texlive-dowith-doc
Summary:        Documentation for dowith
Version:        svn38860

Provides:       tex-dowith-doc
AutoReqProv:    No

%description -n texlive-dowith-doc
Documentation for dowith

%package -n texlive-dramatist
Provides:       tex-dramatist = %{tl_version}
License:        GPL+
Summary:        Typeset dramas, both in verse and in prose
Version:        svn35866.1.2e

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(dramatist.sty) = %{tl_version}

%description -n texlive-dramatist
This package is intended for typesetting drama of any length.
It provides two environments for typesetting dialogues in prose
or in verse; new document divisions corresponding to acts and
scenes; macros that control the appearance of characters and
stage directions; and automatic generation of a `dramatis
personae' list.

%package -n texlive-dramatist-doc
Summary:        Documentation for dramatist
Version:        svn35866.1.2e

Provides:       tex-dramatist-doc
AutoReqProv:    No

%description -n texlive-dramatist-doc
Documentation for dramatist

%package -n texlive-dvgloss
Provides:       tex-dvgloss = %{tl_version}
License:        LPPL
Summary:        Facilities for setting interlinear glossed text
Version:        svn29103.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dvgloss.sty) = %{tl_version}

%description -n texlive-dvgloss
The package provides extensible macros for setting interlinear
glossed text -- useful, for instance, for typing linguistics
papers. The operative word here is "extensible": few features
are built in, but some flexible and powerful facilities are
included for adding your own.

%package -n texlive-dvgloss-doc
Summary:        Documentation for dvgloss
Version:        svn29103.0.1

Provides:       tex-dvgloss-doc
AutoReqProv:    No

%description -n texlive-dvgloss-doc
Documentation for dvgloss

%package -n texlive-dnp
Provides:       tex-dnp = %{tl_version}
License:        LPPL
Summary:        subfont numbers for DNP font encoding
Version:        svn45701
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

%description -n texlive-dnp
subfont numbers for DNP font encoding.

%package -n texlive-disser
Provides:       tex-disser = %{tl_version}
License:        LPPL 1.3
Summary:        Class and templates for typesetting dissertations in Russian
Version:        svn43417
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(ifpdf.sty), tex(ifthen.sty), tex(textcase.sty)
Requires:       tex(exscale.sty)
Provides:       tex(disser.cls) = %{tl_version}, tex(gost732.cls) = %{tl_version}

%description -n texlive-disser
Disser comprises a document class and set of templates for
typesetting dissertations in Russian. One of its primary
advantages is a simplicity of format specification for
titlepage, headers and elements of automatically generated
lists (table of contents, list of figures, etc). Bibliography
styles, that conform to the requirements of the Russian
standard GOST R 7.0.11-2011, are provided.

%package -n texlive-disser-doc
Summary:        Documentation for disser
Version:        svn43417
Provides:       tex-disser-doc
AutoReqProv:    No

%description -n texlive-disser-doc
Documentation for disser

%package -n texlive-dickimaw-doc
Summary:        Documentation for dickimaw
Version:        svn32925.0

Provides:       tex-dickimaw-doc
AutoReqProv:    No

%description -n texlive-dickimaw-doc
Documentation for dickimaw

%package -n texlive-dtxtut-doc
Summary:        Documentation for dtxtut
Version:        svn38375.2.1

Provides:       tex-dtxtut-doc
AutoReqProv:    No

%description -n texlive-dtxtut-doc
Documentation for dtxtut

%package -n texlive-droit-fr
Provides:       tex-droit-fr = %{tl_version}
License:        LPPL 1.3
Summary:        Document class and bibliographic style for French law
Version:        svn39802

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(verbose-ibid.bbx), tex(verbose-ibid.cbx)
Requires:       tex(kvoptions.sty), tex(inputenc.sty), tex(ifdraft.sty), tex(xifthen.sty)
Requires:       tex(xstring.sty), tex(footmisc.sty), tex(engrec.sty), tex(filecontents.sty)
Provides:       tex(droit-fr.bbx) = %{tl_version}, tex(droit-fr.cbx) = %{tl_version}
Provides:       tex(droit-fr.cls) = %{tl_version}

%description -n texlive-droit-fr
The bundle provides a toolkit intended for students writing a
thesis in French law. It features: a LaTeX document class; a
bibliographic style for Biblatex package; a practical example
of french thesis document; and documentation. The class assumes
use of biber and biblatex.

%package -n texlive-droit-fr-doc
Summary:        Documentation for droit-fr
Version:        svn39802

Provides:       tex-droit-fr-doc
AutoReqProv:    No

%description -n texlive-droit-fr-doc
Documentation for droit-fr

%package -n texlive-dhua
Provides:       tex-dhua = %{tl_version}
License:        LPPL 1.3
Summary:        German abbreviations using thin space
Version:        svn24035.0.11

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(dhua.cfg) = %{tl_version}, tex(dhua.sty) = %{tl_version}

%description -n texlive-dhua
The package provides commands for those abbreviations of German
phrases for which the use of thin space is recommended. Setup
commands \newdhua and \newtwopartdhua are provided, as well as
commands for single cases (such as \zB for 'z. B.', saving the
user from typing such as 'z.\,B.'). To typeset the
documentation, the niceverb package, version 0.44, or later, is
required. Das Paket `dhua' stellt Befehle fur sog.
mehrgliedrige Abkurzungen bereit, fur die schmale Leerzeichen
(Festabstande) empfohlen werden (Duden, Wikipedia). In die
englische Paketdokumentation sind deutsche Erlauterungen
eingestreut.

%package -n texlive-dhua-doc
Summary:        Documentation for dhua
Version:        svn24035.0.11

Provides:       tex-dhua-doc
AutoReqProv:    No

%description -n texlive-dhua-doc
Documentation for dhua

%package -n texlive-dcpic
Provides:       tex-dcpic = %{tl_version}
License:        LPPL 1.3
Summary:        Commutative diagrams in a LaTeX and TeX documents
Version:        svn30206.5.0.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dcpic.sty) = %{tl_version}, tex(europroc.cls) = %{tl_version}

%description -n texlive-dcpic
DCpic is a package for typesetting Commutative Diagrams within
a LaTeX and TeX documents. Its distinguishing features are: a
powerful graphical engine, the PiCTeX package; an easy
specification syntax in which a commutative diagram is
described in terms of its objects and its arrows (morphism),
positioned in a Cartesian coordinate system.

%package -n texlive-dcpic-doc
Summary:        Documentation for dcpic
Version:        svn30206.5.0.0

Provides:       tex-dcpic-doc
AutoReqProv:    No

%description -n texlive-dcpic-doc
Documentation for dcpic

%package -n texlive-diagmac2
Provides:       tex-diagmac2 = %{tl_version}
License:        LPPL
Summary:        Diagram macros, using pict2e
Version:        svn15878.2.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pict2e.sty)
Provides:       tex(diagmac2.sty) = %{tl_version}

%description -n texlive-diagmac2
This is a development of the long-established diagmac package,
using pict2e so that the restrictions on line direction are
removed.

%package -n texlive-diagmac2-doc
Summary:        Documentation for diagmac2
Version:        svn15878.2.1

Provides:       tex-diagmac2-doc
AutoReqProv:    No

%description -n texlive-diagmac2-doc
Documentation for diagmac2

%package -n texlive-doc-pictex-doc
Summary:        Documentation for doc-pictex
Version:        svn24927.0

Provides:       tex-doc-pictex-doc
AutoReqProv:    No

%description -n texlive-doc-pictex-doc
Documentation for doc-pictex

%package -n texlive-dottex
Provides:       tex-dottex = %{tl_version}
License:        GPL+
Summary:        Use dot code in LaTeX
Version:        svn15878.0.6

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(graphicx.sty), tex(moreverb.sty), tex(keyval.sty)
Provides:       tex(dottex.sty) = %{tl_version}

%description -n texlive-dottex
The dottex package allows you to encapsulate 'dot' and 'neato'
files in your document (dot and neato are both part of
graphviz; dot creates directed graphs, neato undirected
graphs). If you have shell-escape enabled, the package will
arrange for your files to be processed at LaTeX time;
otherwise, the conversion must be done manually as an
intermediate process before a second LaTeX run.

%package -n texlive-dottex-doc
Summary:        Documentation for dottex
Version:        svn15878.0.6

Provides:       tex-dottex-doc
AutoReqProv:    No

%description -n texlive-dottex-doc
Documentation for dottex

%package -n texlive-dot2texi
Provides:       tex-dot2texi = %{tl_version}
License:        GPL+
Summary:        Create graphs within LaTeX using the dot2tex tool
Version:        svn26237.3.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(moreverb.sty), tex(xkeyval.sty)
Provides:       tex(dot2texi.sty) = %{tl_version}

%description -n texlive-dot2texi
The dot2texi package allows you to embed graphs in the DOT
graph description language in your LaTeX documents. The dot2tex
tool is used to invoke Graphviz for graph layout, and to
transform the output from Graphviz to LaTeX code. The generated
code relies on the TikZ and PGF package or the PSTricks
package. The process is automated if shell escape is enabled.

%package -n texlive-dot2texi-doc
Summary:        Documentation for dot2texi
Version:        svn26237.3.0

Provides:       tex-dot2texi-doc
AutoReqProv:    No

%description -n texlive-dot2texi-doc
Documentation for dot2texi

%package -n texlive-dratex
Provides:       tex-dratex = %{tl_version}
License:        LPPL
Summary:        General drawing macros
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(AlDraTex.sty) = %{tl_version}, tex(DraTex.sty) = %{tl_version}
Provides:       tex(TeXProject.sty) = %{tl_version}, tex(wotree.sty) = %{tl_version}

%description -n texlive-dratex
A low level (DraTex.sty) and a high-level (AlDraTex.sty)
drawing package written entirely in TeX.

%package -n texlive-dratex-doc
Summary:        Documentation for dratex
Version:        svn15878.0

Provides:       tex-dratex-doc
AutoReqProv:    No

%description -n texlive-dratex-doc
Documentation for dratex

%package -n texlive-drs
Provides:       tex-drs = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset Discourse Representation Structures (DRS)
Version:        svn19232.1.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(drs.sty) = %{tl_version}

%description -n texlive-drs
The package draws Discourse Representation Structures (DRSs).
It can draw embedded DRSs, if-then conditions and
quantificational "duplex conditions" (with a properly scaled
connecting diamond). Formatting parameters allow the user to
control the appearance and placement of DRSs, and of DRS
variables and conditions. The package is based on DRS macros in
the covington package.

%package -n texlive-drs-doc
Summary:        Documentation for drs
Version:        svn19232.1.1b

Provides:       tex-drs-doc
AutoReqProv:    No

%description -n texlive-drs-doc
Documentation for drs

%package -n texlive-duotenzor
Provides:       tex-duotenzor = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing package for circuit and duotensor diagrams
Version:        svn18728.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(duotenzor.sty) = %{tl_version}

%description -n texlive-duotenzor
This is a drawing package for circuit and duotensor diagrams
within LaTeX documents. It consists of about eighty commands,
calling on TikZ for support.

%package -n texlive-duotenzor-doc
Summary:        Documentation for duotenzor
Version:        svn18728.1.00

Provides:       tex-duotenzor-doc
AutoReqProv:    No

%description -n texlive-duotenzor-doc
Documentation for duotenzor

%package -n texlive-diagbox
Provides:       tex-diagbox = %{tl_version}
License:        LPPL 1.3
Summary:        Table heads with diagonal lines
Version:        svn42843
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty), tex(pict2e.sty), tex(fp.sty)
Provides:       tex(diagbox.sty) = %{tl_version}

%description -n texlive-diagbox
The package's principal command, \diagbox, takes two arguments
(texts for the slash-separated parts of the box), and an
optional argument with which the direction the slash will go,
and the box dimensions, etc., may vbe controlled. The package
also provides \slashbox and \backslashbox commands for
compatibility with the slashbox package, which it supersedes.

%package -n texlive-diagbox-doc
Summary:        Documentation for diagbox
Version:        svn42843
Provides:       tex-diagbox-doc
AutoReqProv:    No

%description -n texlive-diagbox-doc
Documentation for diagbox

%package -n texlive-diagnose
Provides:       tex-diagnose = %{tl_version}
License:        GPL+
Summary:        A diagnostic tool for a TeX installation
Version:        svn19387.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(diagnose.sty) = %{tl_version}

%description -n texlive-diagnose
Provides macros to assist evaluation of the capabilities of a
TeX installation (i.e., what extensions it supports). An
example document that examines the installation is available.

%package -n texlive-diagnose-doc
Summary:        Documentation for diagnose
Version:        svn19387.0.2

Provides:       tex-diagnose-doc
AutoReqProv:    No

%description -n texlive-diagnose-doc
Documentation for diagnose

%package -n texlive-dialogl
Provides:       tex-dialogl = %{tl_version}
License:        LPPL
Summary:        Macros for constructing interactive LaTeX scripts
Version:        svn28946.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dialog.sty) = %{tl_version}, tex(grabhedr.sty) = %{tl_version}
Provides:       tex(listout.tex) = %{tl_version}, tex(menus.sty) = %{tl_version}

%description -n texlive-dialogl
Gathers together a bunch of code and examples about how to
write macros to carry on a dialogue with the user.

%package -n texlive-dialogl-doc
Summary:        Documentation for dialogl
Version:        svn28946.0

Provides:       tex-dialogl-doc
AutoReqProv:    No

%description -n texlive-dialogl-doc
Documentation for dialogl

%package -n texlive-dichokey
Provides:       tex-dichokey = %{tl_version}
License:        Public Domain
Summary:        Construct dichotomous identification keys
Version:        svn17192.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dichokey.sty) = %{tl_version}

%description -n texlive-dichokey
The package can be used to construct dichotomous identification
keys (used especially in biology for species identification),
taking care of numbering and indentation of successive key
steps automatically. An example file is provided, which
demonstrates usage.

%package -n texlive-dichokey-doc
Summary:        Documentation for dichokey
Version:        svn17192.0

Provides:       tex-dichokey-doc
AutoReqProv:    No

%description -n texlive-dichokey-doc
Documentation for dichokey

%package -n texlive-dinbrief
Provides:       tex-dinbrief = %{tl_version}
License:        LPPL
Summary:        German letter DIN style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dinbrief.cfg) = %{tl_version}, tex(dinbrief.cls) = %{tl_version}
Provides:       tex(dinbrief.sty) = %{tl_version}

%description -n texlive-dinbrief
Implements a document layout for writing letters according to
the rules of DIN (Deutsches Institut fur Normung, German
standardisation institute). A style file for LaTeX 2.09 (with
limited support of the features) is part of the package. Since
the letter layout is based on a German standard, the user guide
is written in German, but most macros have English names from
which the user can recognize what they are used for. In
addition there are example files showing how letters may be
created with the package. A graphical interface for use of the
dinbrief is provided in the dinbrief-GUI bundle.

%package -n texlive-dinbrief-doc
Summary:        Documentation for dinbrief
Version:        svn15878.0

Provides:       tex-dinbrief-doc
AutoReqProv:    No

%description -n texlive-dinbrief-doc
Documentation for dinbrief

%package -n texlive-directory
Provides:       tex-directory = %{tl_version}
License:        LPPL
Summary:        An address book using BibTeX
Version:        svn15878.1.20

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(url.sty)
Provides:       tex(directory.sty) = %{tl_version}

%description -n texlive-directory
A package for LaTeX and BibTeX that facilitates the
construction, maintenance and exploitation of an address book-
like database.

%package -n texlive-directory-doc
Summary:        Documentation for directory
Version:        svn15878.1.20

Provides:       tex-directory-doc
AutoReqProv:    No

%description -n texlive-directory-doc
Documentation for directory

%package -n texlive-dirtytalk
Provides:       tex-dirtytalk = %{tl_version}
License:        Public Domain
Summary:        A package to typeset quotations easier
Version:        svn20520.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(ifthen.sty)
Provides:       tex(dirtytalk.sty) = %{tl_version}

%description -n texlive-dirtytalk
The package provides a macro to typeset quotations, using the
command \say{stuff}. The quotation mark glyphs are inserted by
the macro; nested quotations are detected.

%package -n texlive-dirtytalk-doc
Summary:        Documentation for dirtytalk
Version:        svn20520.1.0

Provides:       tex-dirtytalk-doc
AutoReqProv:    No

%description -n texlive-dirtytalk-doc
Documentation for dirtytalk

%package -n texlive-dlfltxb
Provides:       tex-dlfltxb = %{tl_version}
License:        LPPL
Summary:        Macros related to "Introdktion til LaTeX"
Version:        svn17337.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty), tex(amssymb.sty), tex(graphicx.sty), tex(keyval.sty)
Requires:       tex(ragged2e.sty), tex(chngpage.sty), tex(url.sty), tex(calc.sty)
Provides:       tex(dlfltxbcodetips.sty) = %{tl_version}
Provides:       tex(dlfltxbmarkup.sty) = %{tl_version}, tex(dlfltxbmarkupbookkeys.sty) = %{tl_version}
Provides:       tex(dlfltxbmisc.sty) = %{tl_version}, tex(dlfltxbtocconfig.sty) = %{tl_version}

%description -n texlive-dlfltxb
The bundle contains various macros either used for creating the
author's book "Introduktion til LaTeX" (in Danish), or
presented in the book as code tips. The bundle comprises:
dlfltxbcodetips: various macros helpful in typesetting
mathematics; dlfltxbmarkup: provides a macros used throughout
the book, for registering macro names, packages etc. in the
text, in the margin and in the index, all by using categorised
keys (note, a configuration file may be used; a sample is
included in the distribution); dlfltxbtocconfig: macros for the
two tables of contents that the book has; dlfltxbmisc: various
macros for typesetting LaTeX arguments, and the macro used in
the bibliography that can wrap a URL up into a bibtex entry.
Interested parties may review the book itself on the web at the
author's institution (it is written in Danish).

%package -n texlive-dlfltxb-doc
Summary:        Documentation for dlfltxb
Version:        svn17337.0

Provides:       tex-dlfltxb-doc
AutoReqProv:    No

%description -n texlive-dlfltxb-doc
Documentation for dlfltxb

%package -n texlive-dnaseq
Provides:       tex-dnaseq = %{tl_version}
License:        LPPL
Summary:        Format DNA base sequences
Version:        svn17194.0.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(dnaseq.sty) = %{tl_version}

%description -n texlive-dnaseq
Defines a means of specifying sequences of bases. The bases may
be numbered (per line) and you may specify that subsequences be
coloured. For a more 'vanilla-flavoured' way of typesetting
base sequences, the user might consider the seqsplit package.

%package -n texlive-dnaseq-doc
Summary:        Documentation for dnaseq
Version:        svn17194.0.01

Provides:       tex-dnaseq-doc
AutoReqProv:    No

%description -n texlive-dnaseq-doc
Documentation for dnaseq

%package -n texlive-doclicense
Provides:       tex-doclicense = %{tl_version}
License:        LPPL 1.3
Summary:        Support for putting documents under a license
Version:        svn47975
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(xifthen.sty), tex(etoolbox.sty), tex(xspace.sty)
Requires:       tex(csquotes.sty), tex(ccicons.sty), tex(graphicx.sty), tex(hyperref.sty)
Provides:       tex(doclicense-UKenglish.ldf) = %{tl_version}
Provides:       tex(doclicense-USenglish.ldf) = %{tl_version}
Provides:       tex(doclicense-acadian.ldf) = %{tl_version}
Provides:       tex(doclicense-american.ldf) = %{tl_version}
Provides:       tex(doclicense-australian.ldf) = %{tl_version}
Provides:       tex(doclicense-british.ldf) = %{tl_version}
Provides:       tex(doclicense-canadian.ldf) = %{tl_version}
Provides:       tex(doclicense-canadien.ldf) = %{tl_version}
Provides:       tex(doclicense-english.ldf) = %{tl_version}
Provides:       tex(doclicense-french.ldf) = %{tl_version}
Provides:       tex(doclicense-german.ldf) = %{tl_version}
Provides:       tex(doclicense-newzealand.ldf) = %{tl_version}
Provides:       tex(doclicense-ngerman.ldf) = %{tl_version}
Provides:       tex(doclicense-spanish.ldf) = %{tl_version}
Provides:       tex(doclicense.sty) = %{tl_version}

%description -n texlive-doclicense
This package allows you to put your document under a license
and include a link to read about the license or include an icon
or image of the license. Currently, only Creative Commons is
supported, but this package is designed to handle all kinds of
licenses.

%package -n texlive-doclicense-doc
Summary:        Documentation for doclicense
Version:        svn47975
Provides:       tex-doclicense-doc
AutoReqProv:    No

%description -n texlive-doclicense-doc
Documentation for doclicense

%package -n texlive-docmfp
Provides:       tex-docmfp = %{tl_version}
License:        LPPL
Summary:        Document non-LaTeX code
Version:        svn15878.1.2d

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(docmfp.sty) = %{tl_version}

%description -n texlive-docmfp
Extends the doc package to cater for documenting non-LaTeX
code, such as Metafont or Metapost, or other programming
languages.

%package -n texlive-docmfp-doc
Summary:        Documentation for docmfp
Version:        svn15878.1.2d

Provides:       tex-docmfp-doc
AutoReqProv:    No

%description -n texlive-docmfp-doc
Documentation for docmfp

%package -n texlive-docmute
Provides:       tex-docmute = %{tl_version}
License:        LPPL 1.3
Summary:        Input files ignoring LaTeX preamble, etc
Version:        svn25741.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(docmute.sty) = %{tl_version}

%description -n texlive-docmute
Input or include stand-alone LaTeX documents, ignoring
everything but the material between \begin{document} and
\end{document}.

%package -n texlive-docmute-doc
Summary:        Documentation for docmute
Version:        svn25741.1.4

Provides:       tex-docmute-doc
AutoReqProv:    No

%description -n texlive-docmute-doc
Documentation for docmute

%package -n texlive-doctools
Provides:       tex-doctools = %{tl_version}
License:        LPPL 1.3
Summary:        Tools for the documentation of LaTeX code
Version:        svn34474.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions-patch.sty), tex(kvoptions.sty)
Requires:       tex(pdftexcmds.sty), tex(listings.sty)
Provides:       tex(doctools.sty) = %{tl_version}

%description -n texlive-doctools
The package provides a collection of tools for use either in an
"ordinary" LaTeX document, or within a .dtx file.

%package -n texlive-doctools-doc
Summary:        Documentation for doctools
Version:        svn34474.0.1

Provides:       tex-doctools-doc
AutoReqProv:    No

%description -n texlive-doctools-doc
Documentation for doctools

%package -n texlive-documentation
Provides:       tex-documentation = %{tl_version}
License:        LPPL 1.2
Summary:        Documentation support for C, Java and assembler code
Version:        svn34521.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(documentation.sty) = %{tl_version}

%description -n texlive-documentation
The package provides a simple means of typesetting computer
programs such that the result is acceptable for inclusion in
reports, etc.

%package -n texlive-documentation-doc
Summary:        Documentation for documentation
Version:        svn34521.0.1

Provides:       tex-documentation-doc
AutoReqProv:    No

%description -n texlive-documentation-doc
Documentation for documentation

%package -n texlive-doi
Provides:       tex-doi = %{tl_version}
License:        LPPL
Summary:        Create correct hyperlinks for DOI numbers
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty)
Provides:       tex(doi.sty) = %{tl_version}

%description -n texlive-doi
You can hyperlink DOI numbers to dx.doi.org. However, some
publishers have elected to use nasty characters in their DOI
numbering scheme ('<', '>', '_' and ';' have all been spotted).
This will either upset (La)TeX, or your PDF reader. This
package contains a single user-level command \doi{}, which
takes a DOI number, and creates a correct hyperlink to the
target of the DOI.

%package -n texlive-doi-doc
Summary:        Documentation for doi
Version:        svn15878.0

Provides:       tex-doi-doc
AutoReqProv:    No

%description -n texlive-doi-doc
Documentation for doi

%package -n texlive-dotarrow
Provides:       tex-dotarrow = %{tl_version}
License:        LPPL
Summary:        Extendable dotted arrows
Version:        svn15878.0.01a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(DotArrow.sty) = %{tl_version}

%description -n texlive-dotarrow
The package can draw dotted arrows that are extendable, in the
same was as \xrightarrow.

%package -n texlive-dotarrow-doc
Summary:        Documentation for dotarrow
Version:        svn15878.0.01a

Provides:       tex-dotarrow-doc
AutoReqProv:    No

%description -n texlive-dotarrow-doc
Documentation for dotarrow

%package -n texlive-dotseqn
Provides:       tex-dotseqn = %{tl_version}
License:        Dotseqn
Summary:        Flush left equations with dotted leaders to the numbers
Version:        svn17195.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dotseqn.sty) = %{tl_version}

%description -n texlive-dotseqn
The package provides a different format for typesetting
equations, one reportedly used in 'old style Britsh books':
equations aligned on the left, with dots on the right leading
to the equation number. In default of an equation number, the
package operates much like the fleqn class option (no leaders).

%package -n texlive-dotseqn-doc
Summary:        Documentation for dotseqn
Version:        svn17195.1.1

Provides:       tex-dotseqn-doc
AutoReqProv:    No

%description -n texlive-dotseqn-doc
Documentation for dotseqn

%package -n texlive-download
Provides:       tex-download = %{tl_version}
License:        LPPL 1.3
Summary:        Allow LaTeX to download files using an external process
Version:        svn30695.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(l3keys2e.sty), tex(pdftexcmds.sty), tex(xparse.sty)
Provides:       tex(download.sty) = %{tl_version}

%description -n texlive-download
The package allows the user to download files (using cURL or
wget), from within a document. To run the external commands,
LaTeX (or whatever) needs to be run with the --shell-escape
flag; this creates a tension between your needs and the
security implications of the flag; users should exercise due
caution.

%package -n texlive-download-doc
Summary:        Documentation for download
Version:        svn30695.1.1

Provides:       tex-download-doc
AutoReqProv:    No

%description -n texlive-download-doc
Documentation for download

%package -n texlive-dox
Provides:       tex-dox = %{tl_version}
License:        LPPL
Summary:        Extend the doc package
Version:        svn46011
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(dox.sty) = %{tl_version}

%description -n texlive-dox
The doc package provides LaTeX developers with means to
describe the usage and the definition of new macros and
environments. However, there is no simple way to extend this
functionality to other items (options or counters, for
instance). The DoX package is designed to circumvent this
limitation.

%package -n texlive-dox-doc
Summary:        Documentation for dox
Version:        svn46011
Provides:       tex-dox-doc
AutoReqProv:    No

%description -n texlive-dox-doc
Documentation for dox

%package -n texlive-dpfloat
Provides:       tex-dpfloat = %{tl_version}
License:        LPPL
Summary:        Support for double-page floats
Version:        svn17196.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dpfloat.sty) = %{tl_version}

%description -n texlive-dpfloat
Provides fullpage and leftfullpage environments, that may be
used inside a figure, table, or other float environment. If the
first of a 2-page spread uses a "leftfullpage" environment, the
float will only be typeset on an even-numbered page, and the
two floats will appear side-by-side in a two-sided document.

%package -n texlive-dpfloat-doc
Summary:        Documentation for dpfloat
Version:        svn17196.0

Provides:       tex-dpfloat-doc
AutoReqProv:    No

%description -n texlive-dpfloat-doc
Documentation for dpfloat

%package -n texlive-dprogress
Provides:       tex-dprogress = %{tl_version}
License:        LPPL
Summary:        LaTeX-relevant log information for debugging
Version:        svn15878.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dprogress.sty) = %{tl_version}

%description -n texlive-dprogress
The package logs LaTeX's progress through the file, making the
LaTeX output more verbose. This helps to make LaTeX debugging
easier, as it is simpler to find where exactly LaTeX failed.
The package outputs the typesetting of section, subsection and
subsubsection headers and (if amsmath is loaded) details of the
align environment.

%package -n texlive-dprogress-doc
Summary:        Documentation for dprogress
Version:        svn15878.0.1

Provides:       tex-dprogress-doc
AutoReqProv:    No

%description -n texlive-dprogress-doc
Documentation for dprogress

%package -n texlive-drac
Provides:       tex-drac = %{tl_version}
License:        LPPL
Summary:        Declare active character substitution, robustly
Version:        svn15878.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(drac.sty) = %{tl_version}

%description -n texlive-drac
The package provides macros \DeclareRobustActChar and
\ReDeclareRobActChar. One uses \DeclareRobustActChar in the
same way one would use \DeclareRobustCommand; the macro
\protects the active character when it appears in a moving
argument. \ReDeclareRobActChar redefines an active character
previously defined with \DeclareRobustActChar, in the same way
that \renewcommand works for ordinary commands.

%package -n texlive-drac-doc
Summary:        Documentation for drac
Version:        svn15878.1

Provides:       tex-drac-doc
AutoReqProv:    No

%description -n texlive-drac-doc
Documentation for drac

%package -n texlive-draftcopy
Provides:       tex-draftcopy = %{tl_version}
License:        LPPL
Summary:        Identify draft copies
Version:        svn15878.2.16

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(draftcopy.cfg) = %{tl_version}, tex(draftcopy.sty) = %{tl_version}

%description -n texlive-draftcopy
Places the word DRAFT (or other words) in light grey diagonally
across the background (or at the bottom) of each (or selected)
pages of the document. The package uses PostScript \special
commands, and may not therefore be used with PDFLaTeX. For that
usage, consider the wallpaper or draftwatermark packages.

%package -n texlive-draftcopy-doc
Summary:        Documentation for draftcopy
Version:        svn15878.2.16

Provides:       tex-draftcopy-doc
AutoReqProv:    No

%description -n texlive-draftcopy-doc
Documentation for draftcopy

%package -n texlive-draftwatermark
Provides:       tex-draftwatermark = %{tl_version}
License:        LPPL 1.3
Summary:        Put a grey textual watermark on document pages
Version:        svn37498.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everypage.sty), tex(graphicx.sty), tex(color.sty)
Provides:       tex(draftwatermark.sty) = %{tl_version}

%description -n texlive-draftwatermark
The package provides a means to add a textual, light grey
watermark on every page or on the first page of a document.
Typical usage may consist in writing words such as DRAFT or
CONFIDENTIAL across document pages. The package performs a
similar function to that of draftcopy, but its implementation
is output device independent, and made very simple by relying
on everypage.

%package -n texlive-draftwatermark-doc
Summary:        Documentation for draftwatermark
Version:        svn37498.1.2

Provides:       tex-draftwatermark-doc
AutoReqProv:    No

%description -n texlive-draftwatermark-doc
Documentation for draftwatermark

%package -n texlive-dtk
Provides:       tex-dtk = %{tl_version}
License:        LPPL 1.3
Summary:        Document class for the journal of DANTE
Version:        svn44524
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(multicol.sty), tex(graphicx.sty), tex(color.sty), tex(hyperref.sty)
Requires:       tex(url.sty), tex(pdfescape.sty), tex(ifpdf.sty), tex(ifluatex.sty)
Requires:       tex(atveryend.sty), tex(embedfile.sty), tex(xcolor.sty), tex(longtable.sty)
Requires:       tex(caption.sty), tex(listings.sty), tex(ifthen.sty), tex(paralist.sty)
Requires:       tex(hyphsubst.sty), tex(accsupp.sty), tex(fixltx2e.sty), tex(lineno.sty)
Requires:       tex(etex.sty), tex(ifxetex.sty), tex(amssymb.sty), tex(textcomp.sty)
Requires:       tex(eurosym.sty), tex(amsmath.sty), tex(fontspec.sty), tex(unicode-math.sty)
Requires:       tex(libertine.sty), tex(fontenc.sty), tex(mathpazo.sty), tex(tgpagella.sty)
Requires:       tex(tgheros.sty), tex(beramono.sty), tex(inputenc.sty), tex(cmap.sty)
Requires:       tex(babel.sty), tex(microtype.sty), tex(afterpage.sty), tex(tabularx.sty)
Requires:       tex(xspace.sty), tex(shortvrb.sty), tex(footmisc.sty), tex(array.sty)
Requires:       tex(enumerate.sty), tex(booktabs.sty), tex(subfig.sty), tex(setspace.sty)
Requires:       tex(makeidx.sty), tex(hologo.sty)
Provides:       tex(dtk-url.sty) = %{tl_version}, tex(dtk-author.clo) = %{tl_version}
Provides:       tex(dtk-full.clo) = %{tl_version}, tex(dtk-new-engines.clo) = %{tl_version}
Provides:       tex(dtk-old-engines.clo) = %{tl_version}
Provides:       tex(dtk.cls) = %{tl_version}, tex(dtk-logos.sty) = %{tl_version}

%description -n texlive-dtk
The bundle provides a class and style file for typesetting "Die
TeXnische Komodie" -- the communications of the German TeX
Users Group DANTE e.V. The arrangement means that the class may
be used by article writers to typeset a single article as well
as to produce the complete journal.

%package -n texlive-dtk-doc
Summary:        Documentation for dtk
Version:        svn44524
Provides:       tex-dtk-doc
AutoReqProv:    No

%description -n texlive-dtk-doc
Documentation for dtk

%package -n texlive-dtxgallery-doc
Summary:        Documentation for dtxgallery
Version:        svn15878.1

Provides:       tex-dtxgallery-doc
AutoReqProv:    No

%description -n texlive-dtxgallery-doc
Documentation for dtxgallery

%package -n texlive-dvdcoll
Provides:       tex-dvdcoll = %{tl_version}
License:        LPPL
Summary:        A class for typesetting DVD archives
Version:        svn15878.v1.1a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(afterpage.sty), tex(xkeyval.sty), tex(ifthen.sty), tex(tabularx.sty)
Requires:       tex(booktabs.sty), tex(array.sty), tex(multicol.sty), tex(ragged2e.sty)
Requires:       tex(hyperref.sty), tex(ifpdf.sty), tex(marginnote.sty)
Provides:       tex(dcwrtbib.sty) = %{tl_version}, tex(dvdcoll.cls) = %{tl_version}
Provides:       tex(pdfnotiz.sty) = %{tl_version}

%description -n texlive-dvdcoll
Having lost the overview of my DVD archives, I simply could not
remember if I already recorded the documentary running on TV
that day. I chose to recreate the index using LaTeX: the design
aim was a hyperlinked and fully searchable PDF-document,
listing my DVDs with all titles, lengths and so on. Further
requirements were support for seasons of tv series and a list
with all faulty or missing programs for rerecording. The
dvdcoll class supports all these requirements. dvdcoll.cls
follows the structure <number><title><length>. As a result, the
class is not limited to DVDs--you can of course typeset
archives of CD-ROMs, Audio-CDs and so on. Supported languages
at the moment: English, French, German, Italian, Polish,
Portuguese, Spanish. Some help is needed for other languages!

%package -n texlive-dvdcoll-doc
Summary:        Documentation for dvdcoll
Version:        svn15878.v1.1a

Provides:       tex-dvdcoll-doc
AutoReqProv:    No

%description -n texlive-dvdcoll-doc
Documentation for dvdcoll

%package -n texlive-dynblocks
Provides:       tex-dynblocks = %{tl_version}
License:        LPPL 1.3
Summary:        A simple way to create dynamic blocks for Beamer
Version:        svn35193.0.2b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(etoolbox.sty), tex(xparse.sty)
Provides:       tex(dynblocks.sty) = %{tl_version}

%description -n texlive-dynblocks
The package provides full customisation of the aspect and
dimensions of blocks inside a presentation.

%package -n texlive-dynblocks-doc
Summary:        Documentation for dynblocks
Version:        svn35193.0.2b

Provides:       tex-dynblocks-doc
AutoReqProv:    No

%description -n texlive-dynblocks-doc
Documentation for dynblocks

%package -n texlive-drv
Provides:       tex-drv = %{tl_version}
License:        LPPL
Summary:        Derivation trees with MetaPost
Version:        svn29349.0.97

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-drv
A set of MetaPost macros for typesetting derivation trees (such
as used in sequent calculus, type inference, programming
language semantics...). No MetaPost knowledge is needed to use
these macros.

%package -n texlive-drv-doc
Summary:        Documentation for drv
Version:        svn29349.0.97

Provides:       tex-drv-doc
AutoReqProv:    No

%description -n texlive-drv-doc
Documentation for drv

%package -n texlive-dviincl
Provides:       tex-dviincl = %{tl_version}
License:        Public Domain
Summary:        Include a DVI page into MetaPost output
Version:        svn29349.1.00

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-dviincl
DVItoMP is one of the auxiliary programs available to any
MetaPost package; it converts a DVI file into a MetaPost file.
Using it, one can envisage including a DVI page into an EPS
files generated by MetaPost. Such files allow pages to include
other pages.

%package -n texlive-dviincl-doc
Summary:        Documentation for dviincl
Version:        svn29349.1.00

Provides:       tex-dviincl-doc
AutoReqProv:    No

%description -n texlive-dviincl-doc
Documentation for dviincl


%package -n texlive-dsptricks
Provides:       tex-dsptricks = %{tl_version}
License:        LPPL
Summary:        Macros for Digital Signal Processing plots
Version:        svn34724.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(fp.sty), tex(pst-xkey.sty), tex(fmtcount.sty)
Requires:       tex(ifthen.sty), tex(pstricks.sty), tex(pstricks-add.sty)
Provides:       tex(dspblocks.sty) = %{tl_version}, tex(dspfunctions.sty) = %{tl_version}
Provides:       tex(dsptricks.sty) = %{tl_version}

%description -n texlive-dsptricks
The package provides a set of LaTeX macros (based on PSTricks)
for plotting the kind of graphs and figures that are usually
employed in digital signal processing publications. DSPTricks
provides facilities for standard discrete-time "lollipop"
plots, continuous-time and frequency plots, and pole-zero
plots. The companion package DSPFunctions (dspfunctions.sty)
provides macros for computing frequency responses and DFTs,
while the package DSPBlocks (dspblocks.sty) supports DSP block
diagrams.

%package -n texlive-dsptricks-doc
Summary:        Documentation for dsptricks
Version:        svn34724.1.0

Provides:       tex-dsptricks-doc
AutoReqProv:    No

%description -n texlive-dsptricks-doc
Documentation for dsptricks

%package -n texlive-dccpaper
Provides:       tex-dccpaper = %{tl_version}
License:        LPPL 1.3
Summary:        Typeset papers for the International Journal of Digital Curation
Version:        svn47717
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(dccpaper-base.tex) = %{tl_version}, tex(idcc.cls) = %{tl_version}
Provides:       tex(ijdc-v9.cls) = %{tl_version}

%description -n texlive-dccpaper
The LaTeX class ijdc-v9 produces camera-ready papers and
articles suitable for inclusion in the International Journal of
Digital Curation, with applicability from volume 9 onwards. The
similar idcc class can be used for submissions to the
International Digital Curation Conference, beginning with the
2015 conference.

%package -n texlive-dccpaper-doc
Summary:        Documentation for dccpaper
Version:        svn47717
Provides:       tex-dccpaper-doc
AutoReqProv:    No

%description -n texlive-dccpaper-doc
Documentation for dccpaper

%package -n texlive-dithesis
Provides:       tex-dithesis = %{tl_version}
License:        LPPL
Summary:        Thesis class for undergraduate theses at the University of Athens
Version:        svn34295.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(hyperref.sty), tex(tabularx.sty), tex(graphicx.sty), tex(float.sty)
Requires:       tex(subfig.sty), tex(caption.sty), tex(geometry.sty), tex(parskip.sty)
Requires:       tex(setspace.sty), tex(fancyhdr.sty), tex(titlesec.sty), tex(titletoc.sty)
Requires:       tex(tocloft.sty), tex(titling.sty), tex(xifthen.sty)
Provides:       tex(dithesis.cls) = %{tl_version}

%description -n texlive-dithesis
The class conforms to the requirements of the Department of
Informatics and Telecommunications at the University of Athens
regarding the preparation of undergraduate theses, as of Sep 1,
2011. The class is designed for use with XeLaTeX; by default
(on a Windows platform), the font Arial is used, but provision
is made for use under Linux (with a different sans-serif font).

%package -n texlive-dithesis-doc
Summary:        Documentation for dithesis
Version:        svn34295.0.2

Provides:       tex-dithesis-doc
AutoReqProv:    No

%description -n texlive-dithesis-doc
Documentation for dithesis

%package -n texlive-digiconfigs
Provides:       tex-digiconfigs = %{tl_version}
License:        LPPL
Summary:        Writing "configurations"
Version:        svn15878.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(amsmath.sty)
Provides:       tex(digiconfigs.sty) = %{tl_version}

%description -n texlive-digiconfigs
In Stochastic Geometry and Digital Image Analysis some problems
can be solved in terms of so-called "configurations". A
configuration is basically a square matrix of \circ and \bullet
symbols. This package provides a convenient and compact
mechanism for displaying these configurations.

%package -n texlive-digiconfigs-doc
Summary:        Documentation for digiconfigs
Version:        svn15878.0.5

Provides:       tex-digiconfigs-doc
AutoReqProv:    No

%description -n texlive-digiconfigs-doc
Documentation for digiconfigs

%package -n texlive-drawstack
Provides:       tex-drawstack = %{tl_version}
License:        LPPL 1.3
Summary:        Draw execution stacks
Version:        svn28582.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(drawstack.sty) = %{tl_version}

%description -n texlive-drawstack
This simple LaTeX package provides support for drawing
execution stack (typically to illustrate assembly language
notions). The code is written on top of TikZ.

%package -n texlive-drawstack-doc
Summary:        Documentation for drawstack
Version:        svn28582.0

Provides:       tex-drawstack-doc
AutoReqProv:    No

%description -n texlive-drawstack-doc
Documentation for drawstack

%package -n texlive-dyntree
Provides:       tex-dyntree = %{tl_version}
License:        LGPLv2+
Summary:        Construct Dynkin tree diagrams
Version:        svn15878.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(coollist.sty), tex(calc.sty), tex(epic.sty), tex(eepic.sty)
Requires:       tex(amsmath.sty), tex(amssymb.sty)
Provides:       tex(dyntree.sty) = %{tl_version}

%description -n texlive-dyntree
The package is intended for users needing to typeset a Dynkin
Tree Diagram--a group theoretical construct consisting of
cartan coefficients in boxes connected by a series of lines.
Such a diagram is a tool for working out the states and their
weights in terms of the fundamental weights and the simple
roots. The package makes use of the author's coollist package.

%package -n texlive-dyntree-doc
Summary:        Documentation for dyntree
Version:        svn15878.1.0

Provides:       tex-dyntree-doc
AutoReqProv:    No

%description -n texlive-dyntree-doc
Documentation for dyntree

%package -n texlive-drawmatrix-doc
Provides:       tex-drawmatrix-doc = %{tl_version}
License:        MIT
Summary:        doc files of drawmatrix
Version:        svn44471
AutoReqProv:    No

%description -n texlive-drawmatrix-doc
Documentation for drawmatrix

%package -n texlive-drawmatrix
Provides:       tex-drawmatrix = %{tl_version}
License:        MIT
Summary:        Draw visual representations of matrices in LaTeX
Version:        svn44471
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(drawmatrix.sty) = %{tl_version}

%description -n texlive-drawmatrix
The package provides macros to visually represent matrices.
Various options allow to change the visualizations, e.g.,
drawing rectangular, triangular, or banded matrices.

%package -n texlive-dynamicnumber-doc
Provides:       tex-dynamicnumber-doc = %{tl_version}
License:        MIT
Summary:        doc files of dynamicnumber
Version:        svn38726

AutoReqProv:    No

%description -n texlive-dynamicnumber-doc
Documentation for dynamicnumber

%package -n texlive-dynamicnumber
Provides:       tex-dynamicnumber = %{tl_version}
License:        MIT
Summary:        Dynamically typeset numbers and values in LaTeX through "symbolic links"
Version:        svn38726

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(dynamicnumber.sty) = %{tl_version}

%description -n texlive-dynamicnumber
This package dynamically typesets values generated by different
kinds of scripts in LaTeX through the use of "symbolic links"
(which are not in any way related to the "symbolic links" used
in UNIX systems!). The aim is to reduce errors resulting from
out-of-date numbers by directly setting them in the number
generating file and importing a "symbolic link" into the LaTeX
source file. It can be used to import not only numerical
values, but strings and pieces of code are also possible.
Currently only MATLAB and Python are supported to produce
Dynamic Number list files.

%package -n texlive-docsurvey-doc
Summary:        Programming LaTeX - A survey of documentation and packages
Version:        svn48108
License:        LPPL

%description -n texlive-docsurvey-doc
Provides the document "Programming LaTeX — A survey of documentation 
and packages"

%package -n texlive-draftfigure
Summary:        Replace figures with a white box and additional features.
Version:        svn44854
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(draftfigure.sty) = %{tl_version}

%description -n texlive-draftfigure
With this package you can control the outcome of a figure which
is set to draft and modify the display with various options.

%package -n texlive-dtxdescribe
Summary:        Describe additional object types in dtx source files
Version:        svn47191
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(dtxdescribe.sty) = %{tl_version}

%description -n texlive-dtxdescribe
The doc package includes tools for describing macros and
environments in LaTeX source dtx format. This package adds
additional tools for describing booleans, lengths, counters,
keys, packages, classes, options, files, commands, arguments,
and other objects. Each item is given a margin tag similar to
\DescribeEnv, and is listed in the index by itself and also by
category. Each item may be sorted further by an optional class.
All index entries except code lines are hyperlinked.
Descriptions are best accompanied by examples, so the
environment dtxexample is provided. Contents are displayed
verbatim along with a caption and cross-referencing. They are
then \input and executed, and the result is shown.

%package -n texlive-ducksay
Summary:        The package draws ASCII art of animals saying a specified message.
Version:        svn48375
License:        LPPL and GPLv3
Requires:       texlive-base texlive-kpathsea
Provides:       tex(ducksay.sty) = %{tl_version}

%description -n texlive-ducksay
The package draws ASCII art of animals saying a specified
message. The following macros are available: ducksay duckthink
DefaultAnimal AddAnimal Multi-line messages are supported but
need to be manually created.

%package -n texlive-dynkin-diagrams
Summary:        Draws Dynkin diagrams
Version:        svn48265
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(dynkin-diagrams.sty) = %{tl_version}

%description -n texlive-dynkin-diagrams
Draws Dynkin diagrams.

%package -n texlive-diffcoeff
Summary:        Write differential coefficients easily
Version:        svn41554
License:        GPLv2
Requires:       texlive-base texlive-kpathsea
Provides:       tex(diffcoeff.sty) = %{tl_version}, tex(diffcoeffx.sty) = %{tl_version}
Requires:       texlive-l3kernel, texlive-l3packages

%description -n texlive-diffcoeff
diffcoeff.sty allows the easy writing of ordinary and partial
differential coefficients of arbitrary order. For mixed partial
derivatives, the overall order (algebraic or numeric) is
calculated by the package. Optional arguments allow the easy
specification of a point of evaluation for ordinary
derivatives, or variables held constant for partial
derivatives, and the placement of the differentiand (in the
numerator or appended). Some tweaking of the display is
possible through key = value settings. Secondary commands
provide analogous coefficients constructed from D, \Delta and
\delta and a command for writing Jacobians. diffcoeffx.sty is
diffcoeff.sty 'on steroids', extending that package in ways
that are probably unnecessary but have a certain logical force.
The packages require the LaTeX3 bundles, l3kernel and
l3packages.

%package -n texlive-dijkstra
Summary:        Dijkstra algorithm for LaTeX
Version:        svn45256
License:        LPPL
Requires:       texlive-base texlive-kpathsea, tex(simplekv.sty)
Provides:       tex(dijkstra.sty) = %{tl_version}

%description -n texlive-dijkstra
This small package uses the Dijkstra algorithm for weighted
graphs,directed or not: the search table of the shortest path
can be displayed, the minimum distance between two vertices and
the corresponding path are stored in macros. This packages
depends on simplekv.

%package -n texlive-dsserif
Summary:        A double-struck serifed font for mathematical use
Version:        svn47570
License:        OFL and LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(DSSerif-Bold.afm) = %{tl_version}, tex(DSSerif.afm) = %{tl_version}
Provides:       tex(DSSerifUni-Bold.afm) = %{tl_version}
Provides:       tex(DSSerifUni.afm) = %{tl_version}, tex(DSSerif.map) = %{tl_version}
Provides:       tex(DSSerif-Bold.tfm) = %{tl_version}, tex(DSSerif.tfm) = %{tl_version}
Provides:       tex(DSSerifUni-Bold.tfm) = %{tl_version}
Provides:       tex(DSSerifUni.tfm) = %{tl_version}, tex(DSSerif-Bold.pfb) = %{tl_version}
Provides:       tex(DSSerif.pfb) = %{tl_version}, tex(DSSerifUni-Bold.pfb) = %{tl_version}
Provides:       tex(DSSerifUni.pfb) = %{tl_version}, tex(dsserif.sty) = %{tl_version}
Provides:       tex(udsserif.fd) = %{tl_version}

%description -n texlive-dsserif
DSSerif is a mathematical font package with double struck
serifed digits, upper and lower case letters, in regular and
bold weights. The design was inspired by the STIX double struck
fonts, which are sans serif, but starting from a Courier-like
base.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="public/drm"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*

%files -n texlive-din1505
%{_texdir}/texmf-dist/bibtex/bst/din1505/

%files -n texlive-din1505-doc
%{_texdir}/texmf-dist/doc/latex/din1505/

%files -n texlive-dk-bib
%{_texdir}/texmf-dist/bibtex/bib/dk-bib/
%{_texdir}/texmf-dist/bibtex/bst/dk-bib/
%{_texdir}/texmf-dist/bibtex/csf/dk-bib/
%{_texdir}/texmf-dist/tex/latex/dk-bib/

%files -n texlive-dk-bib-doc
%{_texdir}/texmf-dist/doc/latex/dk-bib/

%files -n texlive-doipubmed
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/doipubmed/

%files -n texlive-doipubmed-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/doipubmed/

%files -n texlive-dice
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/dice/
%{_texdir}/texmf-dist/fonts/tfm/public/dice/

%files -n texlive-dice-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dice/

%files -n texlive-dictsym
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/dictsym/
%{_texdir}/texmf-dist/fonts/map/dvips/dictsym/
%{_texdir}/texmf-dist/fonts/tfm/public/dictsym/
%{_texdir}/texmf-dist/fonts/type1/public/dictsym/
%{_texdir}/texmf-dist/tex/latex/dictsym/

%files -n texlive-dictsym-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dictsym/

%files -n texlive-dingbat
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/dingbat/
%{_texdir}/texmf-dist/fonts/tfm/public/dingbat/
%{_texdir}/texmf-dist/tex/latex/dingbat/

%files -n texlive-dingbat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dingbat/

%files -n texlive-doublestroke
%{_texdir}/texmf-dist/fonts/map/dvips/doublestroke/
%{_texdir}/texmf-dist/fonts/source/public/doublestroke/
%{_texdir}/texmf-dist/fonts/tfm/public/doublestroke/
%{_texdir}/texmf-dist/fonts/type1/public/doublestroke/
%{_texdir}/texmf-dist/tex/latex/doublestroke/

%files -n texlive-doublestroke-doc
%{_texdir}/texmf-dist/doc/fonts/doublestroke/

%files -n texlive-dozenal
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/dozenal/
%{_texdir}/texmf-dist/fonts/map/dvips/dozenal/dozenal.map
%{_texdir}/texmf-dist/fonts/source/public/dozenal/
%{_texdir}/texmf-dist/fonts/tfm/public/dozenal/
%{_texdir}/texmf-dist/fonts/type1/public/dozenal/
%{_texdir}/texmf-dist/tex/latex/dozenal/

%files -n texlive-dozenal-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/dozenal/

%files -n texlive-drm
%license lppl1.3.txt
%{_datadir}/fonts/drm
%{_texdir}/texmf-dist/fonts/afm/public/drm/
%{_texdir}/texmf-dist/fonts/map/dvips/drm/
%{_texdir}/texmf-dist/fonts/opentype/public/drm/
%{_texdir}/texmf-dist/fonts/source/public/drm/
%{_texdir}/texmf-dist/fonts/tfm/public/drm/
%{_texdir}/texmf-dist/fonts/type1/public/drm/
%{_texdir}/texmf-dist/tex/latex/drm/

%files -n texlive-drm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/drm/

%files -n texlive-droid
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/droid/
%{_texdir}/texmf-dist/fonts/enc/dvips/droid/
%{_texdir}/texmf-dist/fonts/map/dvips/droid/
%{_texdir}/texmf-dist/fonts/tfm/public/droid/
%{_texdir}/texmf-dist/fonts/truetype/public/droid/
%{_texdir}/texmf-dist/fonts/type1/public/droid/
%{_texdir}/texmf-dist/fonts/vf/public/droid/
%{_texdir}/texmf-dist/tex/latex/droid/

%files -n texlive-droid-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/droid/

%files -n texlive-duerer
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/duerer/
%{_texdir}/texmf-dist/fonts/tfm/public/duerer/

%files -n texlive-duerer-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/duerer/

%files -n texlive-duerer-latex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/duerer-latex/

%files -n texlive-duerer-latex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/duerer-latex/

%files -n texlive-dutchcal
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/dutchcal/
%{_texdir}/texmf-dist/fonts/map/dvips/dutchcal/
%{_texdir}/texmf-dist/fonts/tfm/public/dutchcal/
%{_texdir}/texmf-dist/fonts/type1/public/dutchcal/
%{_texdir}/texmf-dist/fonts/vf/public/dutchcal/
%{_texdir}/texmf-dist/tex/latex/dutchcal/

%files -n texlive-dutchcal-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/dutchcal/

%files -n texlive-dvipsconfig
%license gpl.txt
%{_texdir}/texmf-dist/dvips/dvipsconfig/

%files -n texlive-dinat
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/dinat/

%files -n texlive-dinat-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/bibtex/dinat/

%files -n texlive-dirtree
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/dirtree/

%files -n texlive-dirtree-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/dirtree/

%files -n texlive-docbytex
%license other-free.txt
%{_texdir}/texmf-dist/tex/generic/docbytex/

%files -n texlive-docbytex-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/generic/docbytex/

%files -n texlive-dowith
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/dowith/

%files -n texlive-dowith-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/dowith/

%files -n texlive-dramatist
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/dramatist/

%files -n texlive-dramatist-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/dramatist/

%files -n texlive-dvgloss
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dvgloss/

%files -n texlive-dvgloss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dvgloss/

%files -n texlive-dnp
%{_texdir}/texmf-dist/fonts/sfd/dnp/

%files -n texlive-disser
%license lppl1.3.txt
%{_texdir}/texmf-dist/makeindex/disser/
%{_texdir}/texmf-dist/tex/latex/disser/

%files -n texlive-disser-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/disser/

%files -n texlive-dickimaw-doc
%license fdl.txt
%{_texdir}/texmf-dist/doc/latex/dickimaw/

%files -n texlive-dtxtut-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dtxtut/

%files -n texlive-droit-fr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/droit-fr/

%files -n texlive-droit-fr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/droit-fr/

%files -n texlive-dhua
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dhua/

%files -n texlive-dhua-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dhua/

%files -n texlive-diagmac2
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/diagmac2/

%files -n texlive-diagmac2-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/diagmac2/

%files -n texlive-doc-pictex-doc
%{_texdir}/texmf-dist/doc/generic/doc-pictex/

%files -n texlive-dottex
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/dottex/

%files -n texlive-dottex-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/dottex/

%files -n texlive-dot2texi
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/dot2texi/

%files -n texlive-dot2texi-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/dot2texi/

%files -n texlive-dratex
%license lppl1.txt
%{_texdir}/texmf-dist/tex/generic/dratex/

%files -n texlive-dratex-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/generic/dratex/

%files -n texlive-drs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/drs/

%files -n texlive-drs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/drs/

%files -n texlive-duotenzor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/duotenzor/

%files -n texlive-duotenzor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/duotenzor/

%files -n texlive-diagbox
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/diagbox/

%files -n texlive-diagbox-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/diagbox/

%files -n texlive-diagnose
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/diagnose/

%files -n texlive-diagnose-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/diagnose/

%files -n texlive-dialogl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dialogl/

%files -n texlive-dialogl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dialogl/

%files -n texlive-dichokey
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/dichokey/

%files -n texlive-dichokey-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/dichokey/

%files -n texlive-dinbrief
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dinbrief/

%files -n texlive-dinbrief-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dinbrief/

%files -n texlive-directory
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bib/directory/
%{_texdir}/texmf-dist/bibtex/bst/directory/
%{_texdir}/texmf-dist/tex/latex/directory/

%files -n texlive-directory-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/directory/

%files -n texlive-dirtytalk
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/dirtytalk/

%files -n texlive-dirtytalk-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/dirtytalk/

%files -n texlive-dlfltxb
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/dlfltxb/
%{_texdir}/texmf-dist/tex/latex/dlfltxb/

%files -n texlive-dlfltxb-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dlfltxb/

%files -n texlive-dnaseq
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dnaseq/

%files -n texlive-dnaseq-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dnaseq/

%files -n texlive-doclicense
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/doclicense/

%files -n texlive-doclicense-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/doclicense/

%files -n texlive-docmfp
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/docmfp/

%files -n texlive-docmfp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/docmfp/

%files -n texlive-docmute
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/docmute/

%files -n texlive-docmute-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/docmute/

%files -n texlive-doctools
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/doctools/

%files -n texlive-doctools-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/doctools/

%files -n texlive-documentation
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/documentation/

%files -n texlive-documentation-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/documentation/

%files -n texlive-doi
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/doi/

%files -n texlive-doi-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/doi/

%files -n texlive-dotarrow
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dotarrow/

%files -n texlive-dotarrow-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dotarrow/

%files -n texlive-dotseqn
%{_texdir}/texmf-dist/tex/latex/dotseqn/

%files -n texlive-dotseqn-doc
%{_texdir}/texmf-dist/doc/latex/dotseqn/

%files -n texlive-download
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/download/

%files -n texlive-download-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/download/

%files -n texlive-dox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dox/

%files -n texlive-dox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dox/

%files -n texlive-dpfloat
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dpfloat/

%files -n texlive-dpfloat-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dpfloat/

%files -n texlive-dprogress
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dprogress/

%files -n texlive-dprogress-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dprogress/

%files -n texlive-drac
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/drac/

%files -n texlive-drac-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/drac/

%files -n texlive-draftcopy
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/draftcopy/

%files -n texlive-draftcopy-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/draftcopy/

%files -n texlive-draftwatermark
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/draftwatermark/

%files -n texlive-draftwatermark-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/draftwatermark/

%files -n texlive-dtk
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dtk/

%files -n texlive-dtk-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dtk/

%files -n texlive-dtxgallery-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dtxgallery/

%files -n texlive-dvdcoll
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/dvdcoll/
%{_texdir}/texmf-dist/tex/latex/dvdcoll/

%files -n texlive-dvdcoll-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dvdcoll/

%files -n texlive-dynblocks
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/dynblocks/

%files -n texlive-dynblocks-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/dynblocks/

%files -n texlive-drv
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/drv/

%files -n texlive-drv-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/drv/

%files -n texlive-dviincl
%license pd.txt
%{_texdir}/texmf-dist/metapost/dviincl/

%files -n texlive-dviincl-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/metapost/dviincl/

%files -n texlive-dsptricks
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dsptricks/

%files -n texlive-dsptricks-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dsptricks/

%files -n texlive-dithesis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/dithesis/

%files -n texlive-dithesis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/dithesis/

%files -n texlive-digiconfigs
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/digiconfigs/

%files -n texlive-digiconfigs-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/digiconfigs/

%files -n texlive-drawstack
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/drawstack/

%files -n texlive-drawstack-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/drawstack/

%files -n texlive-dyntree
%license lgpl2.1.txt
%{_texdir}/texmf-dist/tex/latex/dyntree/

%files -n texlive-dyntree-doc
%license lgpl2.1.txt
%{_texdir}/texmf-dist/doc/latex/dyntree/

%files -n texlive-drawmatrix-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/drawmatrix/

%files -n texlive-drawmatrix
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/drawmatrix/

%files -n texlive-dynamicnumber-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/dynamicnumber/

%files -n texlive-dynamicnumber
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/dynamicnumber/

%files -n texlive-docsurvey-doc
%doc %{_texdir}/texmf-dist/doc/latex/docsurvey/

%files -n texlive-draftfigure
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/draftfigure/
%{_texdir}/texmf-dist/tex/latex/draftfigure/

%files -n texlive-dtxdescribe
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/dtxdescribe/
%{_texdir}/texmf-dist/tex/latex/dtxdescribe/

%files -n texlive-ducksay
%license lppl1.3.txt gpl3.txt
%doc %{_texdir}/texmf-dist/doc/latex/ducksay/
%{_texdir}/texmf-dist/tex/latex/ducksay/

%files -n texlive-dynkin-diagrams
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/dynkin-diagrams/
%{_texdir}/texmf-dist/tex/latex/dynkin-diagrams/

%files -n texlive-diffcoeff
%license gpl2.txt
%{_texdir}/texmf-dist/tex/latex/diffcoeff/
%doc %{_texdir}/texmf-dist/doc/latex/diffcoeff/

%files -n texlive-dijkstra
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/dijkstra/
%doc %{_texdir}/texmf-dist/doc/latex/dijkstra/

%files -n texlive-dsserif
%license ofl.txt lppl.txt
%{_texdir}/texmf-dist/fonts/afm/public/dsserif/
%{_texdir}/texmf-dist/fonts/map/dvips/dsserif/
%{_texdir}/texmf-dist/fonts/tfm/public/dsserif/
%{_texdir}/texmf-dist/fonts/type1/public/dsserif/
%{_texdir}/texmf-dist/tex/latex/dsserif/
%doc %{_texdir}/texmf-dist/doc/fonts/dsserif/ 

%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
