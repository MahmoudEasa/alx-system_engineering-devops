#

file { '/etc/ssh/sshd_config':
  ensure  => 'persent',
  contant => 'PasswordAuthentication no',
}
