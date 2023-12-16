# installs flask from pip3
$package_name = 'flask'

package {'python3-pip':
  ensure => 'installed'
}


exec {"install ${package_name}":
  command => "/usr/bin/pip3 install ${package_name}==2.1.0 werkzeug==2.1.1",
  require => Package['python3-pip'],
}
