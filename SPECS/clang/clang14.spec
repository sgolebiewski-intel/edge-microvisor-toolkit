%global maj_ver 14
%global min_ver 0
%global patch_ver 5

%global clang_srcdir llvm-project-llvmorg-%{version}

Summary:        C, C++, Objective C and Objective C++ front-end for the LLVM compiler.
Name:           clang14
Version:        %{maj_ver}.%{min_ver}.%{patch_ver}
Release:        2%{?dist}
License:        Apache-2.0 WITH LLVM-exception OR NCSA
Vendor:         Intel Corporation
Distribution:   Edge Microvisor Toolkit
Group:          Development/Tools
URL:            https://clang.llvm.org
Source0:        https://github.com/llvm/llvm-project/archive/refs/tags/llvmorg-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  libxml2-devel
BuildRequires:  llvm14-devel = %{version}
BuildRequires:  ncurses-devel
BuildRequires:  python3-devel
BuildRequires:  zlib-devel
Requires:       %{name}-libs = %{version}-%{release}
Requires:       libstdc++-devel
Requires:       libxml2
Requires:       llvm14
Requires:       ncurses
Requires:       python3
Requires:       zlib

%description
The goal of the Clang project is to create a new C based language front-end: C, C++, Objective C/C++, OpenCL C and others for the LLVM compiler. You can get and build the source today.

%package analyzer
Summary:        A source code analysis framework
License:        NCSA AND MIT
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description analyzer
The Clang Static Analyzer consists of both a source code analysis
framework and a standalone tool that finds bugs in C and Objective-C
programs. The standalone tool is invoked from the command-line, and is
intended to run in tandem with a build of a project or code base.

%package devel
Summary:        Development headers for clang
License:        NCSA
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-libs = %{version}-%{release}
# The clang CMake files reference tools from clang-tools-extra.
Requires:       %{name}-tools-extra = %{version}-%{release}

%package libs
Summary:        Runtime library for clang
License:        NCSA
Recommends:     compiler-rt%{?_isa} = %{version}
Recommends:     libomp%{_isa} = %{version}
# libomp-devel is required, so clang can find the omp.h header when compiling
# with -fopenmp.
Recommends:     libomp-devel%{_isa} = %{version}

%description libs
Runtime library for clang.

%description devel
The clang-devel package contains libraries, header files and documentation
for developing applications that use clang.

%package -n git-clang-format
Summary:        Integration of clang-format for git
License:        NCSA
Requires:       git
Requires:       python3

%description -n git-clang-format
clang-format integration for git.

%package tools-extra
Summary:        Extra tools for clang
License:        NCSA
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description tools-extra
A set of extra tools built using Clang's tooling API.

%prep
%setup -q -n %{clang_srcdir}

%build
# Disable symbol generation
export CFLAGS="`echo " %{build_cflags} " | sed 's/ -g//'`"
export CXXFLAGS="`echo " %{build_cxxflags} " | sed 's/ -g//'`"

mkdir -p build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix}   \
      -DCLANG_ENABLE_STATIC_ANALYZER:BOOL=ON \
      -DCMAKE_BUILD_TYPE=Release    \
      -DLLVM_ENABLE_EH=ON \
      -DLLVM_ENABLE_RTTI=ON \
      -DCLANG_LINK_CLANG_DYLIB=ON \
      -Wno-dev ../clang

%make_build

%install
cd build
%make_install

# Remove emacs integration files.
rm %{buildroot}%{_datadir}/clang/*.el

# Remove editor integrations (bbedit, sublime, emacs, vim).
rm -vf %{buildroot}%{_datadir}/clang/clang-format-bbedit.applescript
rm -vf %{buildroot}%{_datadir}/clang/clang-format-sublime.py*

# Remove HTML docs
rm -Rvf %{buildroot}%{_pkgdocdir}
rm -Rvf %{buildroot}%{_datadir}/clang/clang-doc-default-stylesheet.css
rm -Rvf %{buildroot}%{_datadir}/clang/index.js

# Remove bash autocomplete files.
rm -vf %{buildroot}%{_datadir}/clang/bash-autocomplete.sh

# Add clang++-{version} symlink
ln -s clang++ %{buildroot}%{_bindir}/clang++-%{maj_ver}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
cd build
make clang-check

%files
%defattr(-,root,root)
%{_bindir}/clang
%{_bindir}/clang++
%{_bindir}/clang-%{maj_ver}
%{_bindir}/clang++-%{maj_ver}
%{_bindir}/clang-cl
%{_bindir}/clang-cpp

%files analyzer
%{_bindir}/scan-view
%{_bindir}/scan-build
%{_libexecdir}/ccc-analyzer
%{_libexecdir}/c++-analyzer
%{_datadir}/scan-view/
%{_datadir}/scan-build/
%{_mandir}/man1/scan-build.1.*

%files libs
%{_libdir}/clang/
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%dir %{_datadir}/clang/
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/cmake/*
%{_includedir}/clang/
%{_includedir}/clang-c/

%files -n git-clang-format
%{_bindir}/git-clang-format

%files tools-extra
%{_bindir}/analyze-build
%{_bindir}/clang-check
%{_bindir}/clang-extdef-mapping
%{_bindir}/clang-format
%{_bindir}/clang-linker-wrapper
%{_bindir}/clang-offload-bundler
%{_bindir}/clang-refactor
%{_bindir}/clang-nvlink-wrapper
%{_bindir}/clang-offload-wrapper
%{_bindir}/clang-rename
%{_bindir}/clang-repl
%{_bindir}/clang-scan-deps
%{_bindir}/diagtool
%{_bindir}/hmaptool
%{_bindir}/intercept-build
%{_bindir}/scan-build-py
%{_bindir}/c-index-test
%{_datadir}/clang/clang-format.py*
%{_datadir}/clang/clang-format-diff.py*
%{_datadir}/clang/clang-rename.py*
%{_libdir}/libear/__init__.py
%{_libdir}/libear/config.h.in
%{_libdir}/libear/ear.c
%{_libdir}/libscanbuild/__init__.py
%{_libdir}/libscanbuild/analyze.py
%{_libdir}/libscanbuild/arguments.py
%{_libdir}/libscanbuild/clang.py
%{_libdir}/libscanbuild/compilation.py
%{_libdir}/libscanbuild/intercept.py
%{_libdir}/libscanbuild/report.py
%{_libdir}/libscanbuild/resources/scanview.css
%{_libdir}/libscanbuild/resources/selectable.js
%{_libdir}/libscanbuild/resources/sorttable.js
%{_libdir}/libscanbuild/shell.py
%{_libexecdir}/analyze-c++
%{_libexecdir}/analyze-cc
%{_libexecdir}/intercept-c++
%{_libexecdir}/intercept-cc


%changelog
* Mon Dec 23 2024 Naveen Saini <naveen.kumar.saini@intel.com@intel.com> - 14.0.5-2
- Updated initial log entry having fedora version.

* Fri Sep 27 2024 Junxiao Chang <junxiao.chang@intel.com> - 14.0.5-1
- Initial Edge Microvisor Toolkit import from Fedora 36 (license: MIT). License verified.
