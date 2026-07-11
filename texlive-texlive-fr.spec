%global tl_name texlive-fr
%global tl_revision 78031

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	TeX Live manual (French)
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-fr
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-fr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
TeX Live manual (French)

