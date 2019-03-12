# ----------------------------------------------------------------------------------------------------------------------
# Сборка фронтенда
# ----------------------------------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------------------------------
# Колекционирование статики
# ----------------------------------------------------------------------------------------------------------------------
FROM python:3.6-stretch AS collection-static

RUN apt-get update && apt-get install -y locales tree && apt-get autoremove -y

ADD ./requirements.pip /opt
ADD ./install_backend_req.sh /opt
WORKDIR /opt

RUN chmod a+x /opt/*.sh
RUN ./install_backend_req.sh
RUN rm ./*

ADD ./ /opt

RUN find /opt -name "__pycache__"
RUN rm -rf $(find /opt -name "__pycache__")
RUN find /opt -name "__pycache__"
RUN pyclean ./
RUN tree

# TODO: при полноценной сборки фронта следующие 2 строки удалить, а после них строку раскомментировать
RUN mkdir ./frontend
RUN mkdir ./frontend/static
#COPY --from=front-builder /opt/front/static ./front/static

RUN python ./manage.py collectstatic --noinput


# ----------------------------------------------------------------------------------------------------------------------
# Подготовка nginx-image к бою
# ----------------------------------------------------------------------------------------------------------------------
FROM nginx:1.13-alpine
COPY --from=collection-static /opt/static_files /var/www/static
EXPOSE 80
