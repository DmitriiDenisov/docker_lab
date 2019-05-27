# Docker_lab

All most important commands you can find here:
https://medium.com/the-code-review/top-10-docker-commands-you-cant-live-without-54fb6377f481

### sudo service docker status
```docker rm 9f516a41b3b3```
Delete container, volumne will be also deleted

### docker ps -a
Show all containers (included stopped as well)

### docker images
Show all images 

### docker image prune
Delete all unusable images

### docker image rm 8709e7f8a4dd
Delete one image with id 8709e7f8a4dd-

### docker rmi $(docker images -q)
Delete all images

### docker build -t tag_of_image .
Build an image with name tag_of_image from current path

### docker run tag_of_image
Run a container from image tag_of_image

### docker run -p 80:80 --name qwerty --rm try_flask
-p allows to throw ports. In this example 80-th in container port will be available on 80-th port on localhost (localhost:80)
--name allows to give name to our container
--rm will delete container after it stops
-d detach from container so it will run in background mode

### docker run -p 80:80 -it --name qwerty --rm --entrypoint bash try_flask
--entrypoint Replace entry point with bash. Previous entry point will be ignored

### docker run --rm -v `pwd`:/app -p 80:80 —-name my_cont_name -d image_name
-v mount current folder with app. I.e current folder will be available in /app inside a container. All changes with files will be visible inside container immediately

### docker run -v `pwd`/models:/app/models auto_selphie_image
Just another example how to use -v

### docker run -it --entrypoint bash flask_image
-t allows to show inside terminal all comands from container
-i interactive mode when you can send commands from terminal

### docker run --restart always flask_image
Always restart container if it falls

### docker rm $(docker ps -a -q)
Delete all stopped containers

### docker exec -it 2cb98f63c67b bash
Runs bash inside container. I.e it is running in background mode and we attach to it and run bash inside

### docker exec f9a965092e9e ps 
Shows which commands were run inside container

### docker logs 186346daa85d
Show logs for container

### docker stop $(docker ps -a -q)
Stops all running containers

### docker attach -it 186346daa85d
Attaches to running container

### docker build -f Dockerfile.db .
### docker build -f Dockerfile.web .
For multiple docker files

### Add user to sudos (so no need to write each time sudo):
One of the following:
- sudo chmod 666 /var/run/docker.sock
- sudo usermod -aG docker $dmitryhse
- sudo chown dmitryhse dmitryhse/
