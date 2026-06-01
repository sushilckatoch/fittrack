FROM php:8.5-cli
WORKDIR /var/www
RUN apt-get update && apt-get install -y \
    libpng-dev zip unzip git curl libpq-dev \
    && docker-php-ext-install pdo pdo_pgsql
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer
COPY . .
RUN composer install --no-dev
EXPOSE 8000
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
