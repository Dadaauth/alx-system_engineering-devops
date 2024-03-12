# Define
exec { 'increase nginx file open limit':
  command => '/bin/sed -i "s/-n 15/-n 15000/" /etc/default/nginx && service nginx restart',
}
