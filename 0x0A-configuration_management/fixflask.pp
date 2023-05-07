file { '/etc/environment':
  ensure => present,
  content => 'PATH=$PATH:$HOME/.local/bin\n',
}

exec { 'reload-environment':
  command => "bash -c 'source /etc/environment'",
  path => '/usr/bin',
  require => File['/etc/environment'],
}

package { 'python3-pip':
  ensure => installed,
}

exec { 'install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path => '/usr/bin',
  require => Exec['reload-environment'],
}

