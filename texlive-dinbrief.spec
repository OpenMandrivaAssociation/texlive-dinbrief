%global tl_name dinbrief
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	German letter DIN style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/dinbrief
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/dinbrief.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Implements a document layout for writing letters according to the rules
of DIN (Deutsches Institut fur Normung, German standardisation
institute). A style file for LaTeX 2.09 (with limited support of the
features) is part of the package. Since the letter layout is based on a
German standard, the user guide is written in German, but most macros
have English names from which the user can recognize what they are used
for. In addition there are example files showing how letters may be
created with the package. A graphical interface for use of the dinbrief
is provided in the dinbrief-GUI bundle.

