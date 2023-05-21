Name:           cello
Version:        1.0.2
Release:        1%{?dist}
Summary:        Hello World example implemented in C

License:        MIT
URL:            https://github.com/ewb4/test2-my_rpm
Source0:        https://github.com/ewb4/test2-my_rpm/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
      

%description
A simple RPM package to print Hello World

%prep
%setup -q 

%build
make %{?_smp_mflags}


%install
%make_install


%files
%license LICENSE
%{_bindir}/%{name}



%changelog
* Mon May 15 2023 ewb4
- Update links to point to release in github.

* Wed Mar 25 2020 naveen
- first cello package
