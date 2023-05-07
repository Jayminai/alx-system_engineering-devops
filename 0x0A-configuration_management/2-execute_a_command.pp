# Kills killmenow process

exec { 'kill-process':
  command => 'pkill -x killmenow',
  path    => '/usr/bin',
}
