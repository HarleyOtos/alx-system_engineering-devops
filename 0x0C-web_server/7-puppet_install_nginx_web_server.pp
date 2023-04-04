# Install Nginx and set up a redirect and custom page
class nginx {
  package { 'nginx':
    ensure => 'installed',
  }

  file { '/var/www/html/index.html':
    content => 'Hello World!',
  }

  file { '/etc/nginx/sites-available/default':
    content => "
server {
  listen 80;
  root /var/www/html;
  index index.html;
  location /redirect_me {
    return 301 https://www.youtube.com;
  }
}
",
    notify => Service['nginx'],
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => 'link',
    target  => '/etc/nginx/sites-available/default',
    require => File['/etc/nginx/sites-available/default'],
  }

  service { 'nginx':
    ensure => 'running',
    enable => true,
  }
}

include nginx
