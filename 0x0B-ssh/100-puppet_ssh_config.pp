# set up client SSH configuration file

file { '/etc/ssh/sshd_config':
  ensure  => 'file',
  content => 'IdentityFile ~/.ssh/school
	      PasswordAuthentication no',
}
