%global realname hamcrest
%global upstream hyperthunk
%global debug_package %{nil}
%global git_tag 908a24fda4a46776a5135db60ca071e3d783f9f6


Name:		erlang-%{realname}
Version:	0.1.0
Release:	%mkrel 3
Summary:	A framework for writing matcher objects using declarative rules
Group:		Development/Erlang
License:	MIT and BSD
URL:		https://github.com/%{upstream}/%{realname}-erlang
#Source0:	https://github.com/%{upstream}/%{realname}-erlang/archive/%{version}/%{realname}-%{version}.tar.gz
Source0:	https://github.com/%{upstream}/%{realname}-erlang/archive/%{git_tag}/%{realname}-%{version}.tar.gz
Patch1:		erlang-hamcrest-0001-Remove-the-warnings-cause-by-type-declarations.patch
BuildRequires:	erlang-proper
BuildRequires:	erlang-rebar
BuildRequires:	erlang-rpm-macros
Requires:	erlang-erts%{?_isa}
Requires:	erlang-stdlib%{?_isa}

%description
Hamcrest is a framework for writing matcher objects allowing 'match' rules to
be defined declaratively. There are a number of situations where matchers are
invaluable, such as UI validation, or data filtering, but it is in the area of
writing flexible tests that matchers are most commonly used.


%prep
#%setup -q -n %{realname}-erlang-%{version}
%setup -q -n %{realname}-erlang-%{git_tag}
%patch1 -p1 -b .fix_warnings


%build
%{rebar_compile}
# FIXME
sed -i -e "s,\\\\\"hamcrest/include/hamcrest_internal.hrl\\\\\",\"hamcrest/include/hamcrest_internal.hrl\",g" include/hamcrest.hrl
rebar xref -v


%install
install -D -m 644 ebin/%{realname}.app $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/ebin/%{realname}.app
install -m 644 ebin/%{realname}.beam $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/ebin/
install -m 644 ebin/%{realname}_matchers.beam $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/ebin/
install -m 644 ebin/%{realname}_term.beam $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/ebin/
install -D -m 644 include/%{realname}.hrl $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/include/%{realname}.hrl
install -D -m 644 include/%{realname}_internal.hrl $RPM_BUILD_ROOT%{_erllibdir}/%{realname}-%{version}/include/%{realname}_internal.hrl


%check
cp -arv test.config rebar.config
rebar ct -v


%files
%license LICENCE
%doc NOTES README.markdown
%dir %{_erllibdir}/%{realname}-%{version}
%dir %{_erllibdir}/%{realname}-%{version}/ebin
%dir %{_erllibdir}/%{realname}-%{version}/include
%{_erllibdir}/%{realname}-%{version}/ebin/%{realname}.app
%{_erllibdir}/%{realname}-%{version}/ebin/%{realname}.beam
%{_erllibdir}/%{realname}-%{version}/ebin/%{realname}_matchers.beam
%{_erllibdir}/%{realname}-%{version}/ebin/%{realname}_term.beam
%{_erllibdir}/%{realname}-%{version}/include/%{realname}.hrl
%{_erllibdir}/%{realname}-%{version}/include/%{realname}_internal.hrl



%changelog
* Fri May 06 2016 neoclust <neoclust> 0.1.0-3.mga6
+ Revision: 1009760
- Rebuild post boostrap
- imported package erlang-hamcrest

