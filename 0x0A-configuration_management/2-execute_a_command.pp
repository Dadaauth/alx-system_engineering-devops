# kills a process named killmenow
exec {'killprocess':
  command  => '/usr/bin/env pkill -f killmenow'
}
