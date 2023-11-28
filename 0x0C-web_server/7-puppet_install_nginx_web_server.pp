# configure new server with nginx using Puppet

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Create the custom Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "server {
                listen 80;
                listen [::]:80;
        
                root /var/www/html;
                index index.html index.htm index.nginx-debian.html;
        
                server_name _;
        
                location / {
                    # First attempt to serve request as file, then
                    # as directory, then fall back to displaying a 404.
                }
        
                location /redirect_me {
                    return 301 https://youtube.com;
                }
            }",
  notify  => Service['nginx'],
}

# Create the Hello World index page
file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

# Restart Nginx when the configuration changes
service { 'nginx':
  ensure => running,
  enable => true,
}

