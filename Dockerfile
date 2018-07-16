FROM            dosio0102/fc-8th-eb-docker:base
MAINTAINER      dosio0102@gmail.com

ENV             BUILD_MODE      production
ENV             DJANGO_SETTINGS_MODULE  config.settings.${BUILD_MODE}

COPY            .   /srv/project

RUN             mkdir   /var/log/django

RUN             cp -f   /srv/project/.config/${BUILD_MODE}/nginx.conf \
                        /etc/nginx/nginx.conf && \
                cp -f   /srv/project/.config/${BUILD_MODE}/nginx_app.conf \
                        /etc/nginx/sites-available/ && \
#                rm -f   /etc/nginx/sites-enabled/* && \
                ln -s   /etc/nginx/sites-available/nginx_app.conf \
                        /etc/nginx/sites-enabled/

RUN             cp -f   /srv/project/.config/${BUILD_MODE}/supervisor.conf \
                        /etc/supervisor/conf.d/

# Open port 7000
EXPOSE          7000

CMD             supervisord -n