file { '/etc/ssh/ssh_config':
  ensure => 'present',
  source => '2-ssh_config'
}
