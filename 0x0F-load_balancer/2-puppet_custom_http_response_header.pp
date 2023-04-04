# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  content => "server {
                listen 80 default_server;
                listen [::]:80 default_server;

                server_name _;

                location / {
                  root /var/www/html;
                  index index.html;
                  add_header X-Served-By $hostname;
                }
            }",
}

# Remove default Nginx web page
file { '/var/www/html/index.nginx-debian.html':
  ensure => absent,
}

# Create custom Nginx web page
file { '/var/www/html/index.html':
  content => 'Hello World!',
}

# Restart Nginx service
service { 'nginx':
  ensure => running,
  enable => true,
}
