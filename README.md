# Docker_lab

All most important commands you can find here:

- https://tproger.ru/translations/top-10-docker-commands/
- https://towardsdatascience.com/15-docker-commands-you-should-know-970ea5203421

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

### docker run --rm -v $(pwd):/app -p 80:80 —-name my_cont_name -d image_name
-v mount current folder with app. I.e current folder will be available in /app inside a container. All changes with files will be visible inside container immediately

### docker run -v $(pwd)/models:/app/models auto_selphie_image
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

### docker start 677f9de92ed3
Starts again given container with id 677f9de92ed3

### docker attach -it 186346daa85d
Attaches to running container

### docker build -f Dockerfile.db .
### docker build -f Dockerfile.web .
For multiple docker files

### docker run -e port=5000 curr-serv
Pass ENV parameter inside docker container 

### Add user to sudos (so no need to write each time sudo):
One of the following:
- sudo chmod 666 /var/run/docker.sock
- sudo usermod -aG docker $dmitryhse
- sudo chown user_name folder_name
--------
### Publish your docker image on Docker Hub:
1.`docker login`
2. Create new repo on Docker Hub
3. To push: `docker push dmitrydenisov/curr-serv:tagname`
4. To Pull: `docker pull dmitrydenisov/curr-serv`

You can also set up automatic builds in Docker Hub, details: https://www.youtube.com/watch?v=sl2mfyjnkXk 

--------
## docker-compose:
The main function of Docker Compose is the creation of microservice architecture, meaning the containers and the links between them. But the tool is capable of much more:

### docker-compose build
Building images (if an appropriate Dockerfile is provided)

### docker-compose up
Run containers 

### docker-compose stop
Stop services

### docker-compose down
 Stop and remove containers, networks, images, and volumes

### docker-compose config
Show Dockerfile

### docker-compose ps
Lists containers related to images declared in docker-compose file

### docker-compose down --rmi <all|local> 
Down and remove images

### docker-compose up -d
Run containers and detach 

### docker-compose images
List of images


In example from folder 'example_docker_compose_flask' in order to check if docker-compose just run in bash: ```curl localhost:5000``` or ```curl 0.0.0.0:5000```
