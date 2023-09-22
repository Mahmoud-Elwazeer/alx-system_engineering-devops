# Using Puppet, install flask from pip3.

exec { 'install python3 packages':
	command => 'pip3 install flask == 2.1.0',
	path => ['/usr/bin/'],
}
