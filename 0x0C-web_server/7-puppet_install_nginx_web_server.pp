# Install and configure an Nginx server using Puppet

package { 'nginx':
  ensure => installed,
  name   => 'nginx',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'redirect_me':
  ensure   => 'present',
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => '\n\tlocation /redirect_me {\n\t\treturn 301 https://google.com;\n\t}\n',
  multiply => true,
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
