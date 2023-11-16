# Fix the failed requests to get 0 failed
exec { 'fix_failed_requests':
  command => "sed -i 's/ULIMIT=\"-n 15\"/ULIMIT=\"-n 4096\"/g' /etc/default/nginx; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
