# Docker_lab

All most important commands you can find here:
https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481

# sudo service docker status
```docker rm 9f516a41b3b3```
Delete container, volumne will be also deleted

# ```docker ps -a```
Show all containers (included stopped as well)

docker images - все имаджи. При создании идентичного имаджа 
docker image prune - удаляем все неисп имаджи
docker image rm 8709e7f8a4dd
docker run -p 80:80 --name xxxxxxx321312312312 --rm try_flask # имя даем контейнеру 
—-rm при run, после stop он удаляет контейнер. 
-d - detach
docker exec -it 2cb98f63c67b bash # запускаем bash внутри контейнера
docker run -p 80:80 -it --name xxxxxxx321312312312 --rm --entrypoint bash try_flask - зподменяем entry point под bash
from python3:basis - для наследования от другого image
-v позволяет подмонтировать локальные файлы к докеру, мы можем редактировать локально и видеть изменения в контейнере. Плюс файлы не удалятся  
docker run -p 80:80 -v `pwd`:/app -d test_2

ma	
docker run --rm -v `pwd`:/app -p 80:80 —-name my_cont_name -d image_name

gunicorn -w 8 --bind=0.0.0.0:80 main:app

docker run --rm -v `pwd`:/app -p 80:80 -it test_2

docker rm $(docker ps -a -q) - удалить все остановленные контейнеры
docker rmi $(docker images -q) - удалить все images

docker run --rm -v `pwd`:/app -p 80:80 -d --name gunic_cont gunic_image
docker exec f9a965092e9e ps - вывести какие команды выполнялись внутри докера

-------------------------

## Чтобы установить Rabbit-MQ:
```brew services start rabbitmq```
Ссылка на RabbitMQ:

## Как запустить воркер на текущей машине:
1. Создать venv в папке с проектом, сделать ```pip install requirements.txt```
2. В консольке сначала cd в папку с проектом, затем: ```source venv/bin/activate``` (активируем терминал в venv)
