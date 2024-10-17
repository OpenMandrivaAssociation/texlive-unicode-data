Name:		texlive-unicode-data
Version:	68311
Release:	1
Summary:	Unicode data and loaders for TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/unicode-data
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-data.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unicode-data.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides generic access to Unicode Consortium data
for TeX use. It contains a set of text files provided by the
Unicode Consortium which are currently all from Unicode 8.0.0,
with the exception of MathClass.txt which is not currently part
of the Unicode Character Database. Accompanying these source
data are generic TeX loader files allowing this data to be used
as part of TeX runs, in particular in building format files.
Currently there are two loader files: one for general character
set up and one for initialising XeTeX character classes as has
been carried out to date by unicode-letters.tex. The source
data are distributed in accordance with the license stipulated
by the Unicode Consortium. The bundle as a whole is
co-ordinated by the LaTeX3 Project as a general resource for
TeX users.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/unicode-data
%doc %{_texmfdistdir}/doc/generic/unicode-data

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
