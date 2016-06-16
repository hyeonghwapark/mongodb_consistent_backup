%define debug_package	%{nil}
%define	bin_name	mongodb-consistent-backup

Name:		mongodb_consistent_backup
Version:	%{version}
Release:	1%{?dist}
Summary:	MongoDB Consistent Backup Tool

Group:		Software/Database
License:	Apache License Version 2.0
URL:		https://github.com/Percona-Lab/mongodb_consistent_backup
Source:		%{name}.tar.gz
Prefix:		/usr

# Use CentOS SCL python27 (https://www.softwarecollections.org/en/scls/rhscl/python27/) on CentOS 6 (RHEL6 untested)
# On build host: 'yum install python27-python python27-python-devel python27-python-virtualenv gcc'
%{?el6:Requires: python27-python >= 2.7}
%{?el6:BuildRequires: python27-python >= 2.7 python27-python-devel python27-python-virtualenv gcc}

# Use base python/virtualenv, which should be 2.7 on CentOS/RHEL 7
# On build host: 'yum install python python-devel python-virtualenv gcc'
%{?el7:Requires: python >= 2.7}
%{?el7:BuildRequires: python >= 2.7 python-devel python-virtualenv gcc}


%description
Tool for getting consistent backups from MongoDB Clusters and ReplicaSet


%prep
%setup -q -n %{name}


%build
make


%install
mkdir -p %{buildroot}/usr/share/%{bin_name}
install conf/example.yml %{buildroot}/usr/share/%{bin_name}/%{bin_name}.example.yml
install LICENSE %{buildroot}/usr/share/%{bin_name}/LICENSE
install README.md %{buildroot}/usr/share/%{bin_name}/README.md

make PREFIX=%{prefix} DESTDIR=%{buildroot} install


%files
%{prefix}/bin/%{bin_name}
/usr/share/%{bin_name}/LICENSE
/usr/share/%{bin_name}/README.md
/usr/share/%{bin_name}/%{bin_name}.example.yml


%changelog

