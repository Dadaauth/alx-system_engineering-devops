# installs flask from pip3
$package_name = 'flask'
exec {"install ${package_name}":
  command => "/usr/bin/pip3 install ${package_name}==2.1.0",
  unless  => "/usr/bin/pip3 show ${package_name}"
}
