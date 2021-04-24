#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-HistData
Version  : 0.8.7
Release  : 13
URL      : https://cran.r-project.org/src/contrib/HistData_0.8-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/HistData_0.8-7.tar.gz
Summary  : Data Sets from the History of Statistics and Data Visualization
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
that are interesting and important in the history of statistics and data
    visualization. The goal of the package is to make these available, both for
    instructional use and for historical research. Some of these present interesting
    challenges for graphics or analysis in R.

%prep
%setup -q -c -n HistData
cd %{_builddir}/HistData

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1615390864

%install
export SOURCE_DATE_EPOCH=1615390864
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library HistData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library HistData
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library HistData
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc HistData || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/HistData/DESCRIPTION
/usr/lib64/R/library/HistData/INDEX
/usr/lib64/R/library/HistData/Meta/Rd.rds
/usr/lib64/R/library/HistData/Meta/data.rds
/usr/lib64/R/library/HistData/Meta/features.rds
/usr/lib64/R/library/HistData/Meta/hsearch.rds
/usr/lib64/R/library/HistData/Meta/links.rds
/usr/lib64/R/library/HistData/Meta/nsInfo.rds
/usr/lib64/R/library/HistData/Meta/package.rds
/usr/lib64/R/library/HistData/Meta/vignette.rds
/usr/lib64/R/library/HistData/NAMESPACE
/usr/lib64/R/library/HistData/NEWS
/usr/lib64/R/library/HistData/R/HistData
/usr/lib64/R/library/HistData/R/HistData.rdb
/usr/lib64/R/library/HistData/R/HistData.rdx
/usr/lib64/R/library/HistData/WORDLIST
/usr/lib64/R/library/HistData/data/Rdata.rdb
/usr/lib64/R/library/HistData/data/Rdata.rds
/usr/lib64/R/library/HistData/data/Rdata.rdx
/usr/lib64/R/library/HistData/doc/Snow_deaths-duplicates.R
/usr/lib64/R/library/HistData/doc/Snow_deaths-duplicates.Rmd
/usr/lib64/R/library/HistData/doc/Snow_deaths-duplicates.html
/usr/lib64/R/library/HistData/doc/index.html
/usr/lib64/R/library/HistData/help/AnIndex
/usr/lib64/R/library/HistData/help/HistData.rdb
/usr/lib64/R/library/HistData/help/HistData.rdx
/usr/lib64/R/library/HistData/help/aliases.rds
/usr/lib64/R/library/HistData/help/paths.rds
/usr/lib64/R/library/HistData/html/00Index.html
/usr/lib64/R/library/HistData/html/R.css
/usr/lib64/R/library/HistData/images/google-toledo-rome3.jpg
