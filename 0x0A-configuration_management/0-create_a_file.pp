# Creates a file named school in /temp contains a msg
file { '/tmp/school':
	ensure => 'file',
	owner => 'www-data',
	group => 'www-data',
	mode => '0744',
	content => 'I love Puppet'
}
