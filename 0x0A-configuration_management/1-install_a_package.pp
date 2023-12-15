# installs flask from pip3
$package_name = 'flask'
exec {"install ${package_name}":
  command => "/usr/bin/pip3 install ${package_name}",
  unless  => "/usr/bin/pip3 show ${package_name}"
}
