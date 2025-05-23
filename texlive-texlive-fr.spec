Name:		texlive-texlive-fr
Version:	74301
Release:	1
Summary:	TeX Live manual (French)
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-fr package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/live4ht.cfg
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/notes
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/tex-live.css
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/texlive-fr.css
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/texlive-fr.html
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/texlive-fr.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-fr/texlive-fr.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
