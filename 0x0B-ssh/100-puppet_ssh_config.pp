#!/usr/bin/env bash
# ssh configuration using Pupper

file { '~/.ssh/config':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host 54.144.146.250\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
