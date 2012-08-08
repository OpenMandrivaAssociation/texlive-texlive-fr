# revision 26782
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-texlive-fr
Version:	20120808
Release:	1
Summary:	TeX Live manual (French)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-fr package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdir}/doc/texlive/texlive-fr/Makefile
%doc %{_texmfdir}/doc/texlive/texlive-fr/live4ht.cfg
%doc %{_texmfdir}/doc/texlive/texlive-fr/notes
%doc %{_texmfdir}/doc/texlive/texlive-fr/tex-live.css
%doc %{_texmfdir}/doc/texlive/texlive-fr/texlive-fr.css
%doc %{_texmfdir}/doc/texlive/texlive-fr/texlive-fr.html
%doc %{_texmfdir}/doc/texlive/texlive-fr/texlive-fr.pdf
%doc %{_texmfdir}/doc/texlive/texlive-fr/texlive-fr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
