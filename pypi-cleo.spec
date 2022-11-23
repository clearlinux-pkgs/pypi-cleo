#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-cleo
Version  : 2.0.1
Release  : 17
URL      : https://files.pythonhosted.org/packages/83/51/b2609f0998671bef90b83407e75dbd8e3812e513e88f548d1b10b48a1d12/cleo-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/83/51/b2609f0998671bef90b83407e75dbd8e3812e513e88f548d1b10b48a1d12/cleo-2.0.1.tar.gz
Summary  : Cleo allows you to create beautiful and testable command-line interfaces.
Group    : Development/Tools
License  : MIT
Requires: pypi-cleo-license = %{version}-%{release}
Requires: pypi-cleo-python = %{version}-%{release}
Requires: pypi-cleo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(poetry_core)

%description
# Cleo
[![Tests](https://github.com/python-poetry/cleo/actions/workflows/tests.yml/badge.svg)](https://github.com/python-poetry/cleo/actions/workflows/tests.yml)
[![PyPI version](https://img.shields.io/pypi/v/cleo)](https://pypi.org/project/cleo/)

%package license
Summary: license components for the pypi-cleo package.
Group: Default

%description license
license components for the pypi-cleo package.


%package python
Summary: python components for the pypi-cleo package.
Group: Default
Requires: pypi-cleo-python3 = %{version}-%{release}

%description python
python components for the pypi-cleo package.


%package python3
Summary: python3 components for the pypi-cleo package.
Group: Default
Requires: python3-core
Provides: pypi(cleo)
Requires: pypi(crashtest)
Requires: pypi(rapidfuzz)

%description python3
python3 components for the pypi-cleo package.


%prep
%setup -q -n cleo-2.0.1
cd %{_builddir}/cleo-2.0.1
pushd ..
cp -a cleo-2.0.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1669221467
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . rapidfuzz
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . crashtest
pypi-dep-fix.py . rapidfuzz
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-cleo
cp %{_builddir}/cleo-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-cleo/2d5e88c42a6393ae4edea4e9f949f49494ed30e1 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
pypi-dep-fix.py %{buildroot} crashtest
pypi-dep-fix.py %{buildroot} rapidfuzz
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-cleo/2d5e88c42a6393ae4edea4e9f949f49494ed30e1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
