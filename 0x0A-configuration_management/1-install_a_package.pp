#!/usr/bin/pup
# install flask from pip3
exec { 'Flask':
  command => '/usr/bin/pip3 install flask=2.1.0',
}
