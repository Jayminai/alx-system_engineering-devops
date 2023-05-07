# Puppet creates a file in /tmp

file { '/tmp/school':
  ensure  => file,
  path    => '/tmp/school',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
}
