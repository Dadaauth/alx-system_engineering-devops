# Changes the OS configurationn so that it is possible to
# login with the 'holberton' user and open a file without any error message.
$seek_string1 = 'holberton hard nofile 5'
$seek_string2 = 'holberton soft nofile 4'
$replace_string1 = 'holberton hard nofile 50'
$replace_string2 = 'holberton soft nofile 40'
exec { 'change-os-configuration-for-holberton-user':
  command => "/bin/sed -i 's/${seek_string1}/${replace_string1}/; s/${seek_string2}/${replace_string2}/' /etc/security/limits.conf"
}
