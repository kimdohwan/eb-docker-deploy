FROM            python:3.6.5-slim
MAINTAINER      dosio0102@gmail.ccm

RUN             apt -y update && apt -y dist-upgrade
RUN             apt -y install build-essential
RUN             apt -y install nginx supervisor


#도커 안에서 구지 pipenv를 설치하고 사용하지 않으려고 requirements를 사용
COPY            ./requirements.txt   /srv/
RUN             pip install -r /srv/requirements.txt
# ============= 위 쪽은 Dockerfile.base ===============

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