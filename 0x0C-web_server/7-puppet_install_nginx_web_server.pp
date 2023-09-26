# Install and configure an Nginx server using Puppet

exec {'install_nginx':
  command => 'sudo apt-get -y install nginx',
}

file { 'root path':
  ensure  => 'present',
  path    => '/var/www/html/index.nginx-debian.html',
  content => 'Hello World!',
}

file_line { 'redirect_me':
  ensure   => 'present',
  path     => '/etc/nginx/sites-available/default',
  after    => 'server_name _;',
  line     => '\n\tlocation /redirect_me {\n\t\treturn 301 https://google.com;\n\t}\n',
  multiply => true,
}

exec { 'restart_nginx':
  command => 'sudo service nginx restart',
}
