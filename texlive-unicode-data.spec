%global tl_name unicode-data
%global tl_revision 76413

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.19
Release:	%{tl_revision}.1
Summary:	Unicode data and loaders for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/unicode-data
License:	lppl1.3c other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-data.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-data.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides generic access to Unicode Consortium data for TeX
use. It contains a set of text files provided by the Unicode Consortium
which are currently all from Unicode 8.0.0, with the exception of
MathClass.txt which is not currently part of the Unicode Character
Database. Accompanying these source data are generic TeX loader files
allowing this data to be used as part of TeX runs, in particular in
building format files. Currently there are two loader files: one for
general character set up and one for initialising XeTeX character
classes as has been carried out to date by unicode-letters.tex. The
source data are distributed in accordance with the license stipulated by
the Unicode Consortium. The bundle as a whole is co-ordinated by the
LaTeX3 Project as a general resource for TeX users.

