%define		packname	BSgenome

Summary:	Infrastructure for Biostrings-based genome data packages
Name:		R-%{packname}
Version:	1.26.1
Release:	1
License:	Artistic 2.0
Group:		Applications/Science
Source0:	http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	c46bfe6388f351c7ee7a034e63fd784d
URL:		http://bioconductor.org/packages/release/bioc/html/Biobase.html
BuildRequires:	R
BuildRequires:	R-BiocGenerics >= 0.3.2
BuildRequires:	R-IRanges >= 1.13.6
BuildRequires:	R-GenomicRanges >= 1.7.5
BuildRequires:	R-Biostrings >= 2.23.3
BuildRequires:	texlive-latex
Requires:	R
Requires:	R-BiocGenerics >= 0.3.2
Requires:	R-IRanges >= 1.13.6
Requires:	R-GenomicRanges >= 1.7.5
Requires:	R-Biostrings >= 2.23.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Infrastructure shared by all the Biostrings-based genome data packages.

%prep
%setup -c -q -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/Meta/
%{_libdir}/R/library/%{packname}/R/
%{_libdir}/R/library/%{packname}/help/
%{_libdir}/R/library/%{packname}/libs/
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/UnitTests/
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/scripts
%{_libdir}/R/library/%{packname}/ExpressionSet
%{_libdir}/R/library/%{packname}/CITATION
%{_libdir}/R/library/%{packname}/Code
%{_libdir}/R/library/%{packname}/extdata
%{_libdir}/R/library/%{packname}/testClass.R
%{_libdir}/R/library/%{packname}/NEWS
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/html
