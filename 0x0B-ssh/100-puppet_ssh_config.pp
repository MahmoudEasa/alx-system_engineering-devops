# set up client SSH configuration file
# to connect to a server without typing a password.

file_line { 'configuration file':
  path => '/etc/ssh/sshd_config',
  line => 'PasswordAuthentication no',
}

file_line { 'add path':
  path => '/etc/ssh/sshd_config',
  line => 'IdentityFile ~/.ssh/school',
}
