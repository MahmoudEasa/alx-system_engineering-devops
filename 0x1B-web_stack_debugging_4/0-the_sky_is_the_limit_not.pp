# Fix the failed requests to get 0 failed
exec { 'fix_failed_requests':
  command => "sed -i 's/worker_processes 4;/worker_processes 10;/g' /etc/nginx/nginx.conf; sudo service nginx restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
