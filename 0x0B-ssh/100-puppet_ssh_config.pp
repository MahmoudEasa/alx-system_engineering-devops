# set up client SSH configuration file
# to connect to a server without typing a password.

file_line { '/etc/ssh/sshd_config':
  line  => 'PasswordAuthentication no',
}
