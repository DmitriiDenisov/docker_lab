FROM python:3 # наш базовый image наследуется от python:3 image
RUN set -ex \ # умный вывод в консоли
    && apt-get update -y \ # апдейтим apt-get
    && apt-get install -y python-pip python-dev build-essential # ставим все необходимое для питона

COPY . . # копируем всё, что есть в корневую папку
# WORKDIR /reqs # можем назначить директорию по умолчанию
RUN pip install -r requirements.txt # запускаем инсталляцию зависимрстей
# вообще после RUN пишется обычная команда из консоли
RUN rm requirements.txt && rm Dockerfile # удаляем requirements и Dockerfile
ENTRYPOINT ["python3"] # входная точка в данном случае не нужна, но поставить мы её формально должны
