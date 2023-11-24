# kills a process called killmenow
exec { 'kill':
	command => '/usr/bin/pkill killmenow',
}
