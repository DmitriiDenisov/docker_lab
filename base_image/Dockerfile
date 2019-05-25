# наш базовый image наследуется от python:3 image:
FROM python:3
# умный вывод в консоли +  ставим все необходимое для питона
RUN set -ex \
    && apt-get update -y \
    && apt-get install -y python-pip python-dev build-essential

# копируем всё, что есть в корневую папку:
COPY . .
# можем назначить директорию по умолчанию:
# WORKDIR /reqs
# запускаем инсталляцию зависимрстей:
RUN pip install -r requirements.txt
# вообще после RUN пишется обычная команда из консоли
# удаляем requirements и Dockerfile:
RUN rm requirements.txt && rm Dockerfile
# входная точка в данном случае не нужна, но поставить мы её формально должны:
ENTRYPOINT ["python3"]
