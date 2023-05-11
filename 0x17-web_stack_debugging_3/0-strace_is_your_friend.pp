# Fix issue with Wordpress
# during initializing process

exec { 'fix-wordpress':
  command => "/bin/sed -i /var/www/html/wp-settings.php \
  -e 's/class-wp-locale.phpp/class-wp-locale.php/'"
}
