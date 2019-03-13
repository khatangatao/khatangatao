# ----------------------------------------------------------------------------------------------------------------------
# Подготовка образа с сервером бэкенда python
# ----------------------------------------------------------------------------------------------------------------------
FROM python:3.6-stretch
LABEL maintainer="khatangatao@gmail.com"

VOLUME /opt/media
EXPOSE 8000
ENTRYPOINT ./run_backends.sh

RUN apt-get update && \
    apt-get install -y locales tree netcat gettext && \
    apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN echo '\n ru_RU.UTF-8 UTF-8 \n en_US.UTF-8 UTF-8 \n ' >> /etc/locale.gen && locale-gen
ENV LANG=ru_RU.UTF-8
ENV LC_ALL=ru_RU.UTF-8
ENV LANGUAGE=ru_RU.UTF-8
RUN locale && locale > /etc/default/locale

ADD ./requirements.pip /opt
ADD ./install_backend_req.sh /opt
WORKDIR /opt

RUN chmod a+x /opt/*.sh && \
    ./install_backend_req.sh

ADD ./ /opt
RUN python ./manage.py compilemessages

RUN find /opt -name "__pycache__" && \
    rm -rf $(find /opt -name "__pycache__") && \
    find /opt -name "__pycache__" && \
    pyclean ./ && \
    tree ./
