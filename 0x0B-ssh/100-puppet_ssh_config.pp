file { '/etc/ssh/ssh_config':
  ensure => 'present',
  source => '/home/clement/alx-system_engineering-devops/0x0B-ssh/2-ssh_config'
}
