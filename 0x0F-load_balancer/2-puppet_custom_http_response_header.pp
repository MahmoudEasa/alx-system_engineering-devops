# Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02)

exec { 'apt-update':
  command => '/usr/bin/apt-get update'
}

exec { 'apt-upgrade':
  command => '/usr/bin/apt-get upgrade'
}

package { 'nginx':
  ensure => 'installed',
  name   => 'nginx',
}

file_line { 'nginx config':
  path  => '/etc/nginx/nginx.conf',
  line  => "\tadd_header X-Served-By ${hostname};",
  after => 'http {',
}

exec { 'nginx restart':
  command => '/usr/sbin/service nginx restart',
}
