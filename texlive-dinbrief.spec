# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/dinbrief
# catalog-date 2009-09-25 22:54:35 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-dinbrief
Version:	20170414
Release:	1
Summary:	German letter DIN style
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/dinbrief
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
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

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.cfg
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.cls
%{_texmfdistdir}/tex/latex/dinbrief/dinbrief.sty
%doc %{_texmfdistdir}/doc/latex/dinbrief/brfbody.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/brfkopf.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/dbold.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/dinbrief.pdf
%doc %{_texmfdistdir}/doc/latex/dinbrief/dinbrief.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/dintab.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/example.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/liesmich
%doc %{_texmfdistdir}/doc/latex/dinbrief/readme
%doc %{_texmfdistdir}/doc/latex/dinbrief/test10.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/test11.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/test12.tex
%doc %{_texmfdistdir}/doc/latex/dinbrief/testnorm.tex
#- source
%doc %{_texmfdistdir}/source/latex/dinbrief/dinbrief.drv
%doc %{_texmfdistdir}/source/latex/dinbrief/dinbrief.dtx
%doc %{_texmfdistdir}/source/latex/dinbrief/dinbrief.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20090925-2
+ Revision: 750960
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20090925-1
+ Revision: 718233
- texlive-dinbrief
- texlive-dinbrief
- texlive-dinbrief
- texlive-dinbrief

