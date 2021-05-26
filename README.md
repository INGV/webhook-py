<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [whook](#whook)
  - [Introduction](#introduction)
  - [Project Components (Directory Structure)](#project-components-directory-structure)
    - [client](#client)
    - [nginx](#nginx)
    - [server](#server)
    - [Environment variable](#environment-variable)
    - [`docker-compose.yml`](#docker-composeyml)
  - [Architecture](#architecture)
    - [Working](#working)
  - [Usage](#usage)
    - [Clone the git repository](#clone-the-git-repository)
    - [Build docker images](#build-docker-images)
    - [Run containers](#run-containers)
    - [Test the application](#test-the-application)
  - [Swagger spec (Work In Progess)](#swagger-spec-work-in-progess)
- [Author](#author)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# whook

## Introduction
This project implement a web hook that exposes two generic web services, respectively: `GET` and `POST`.
- The first one echoes, on the stdout and on a log file (`<project-root>/log/whook.log`), the received parameters, as couples of `name=value`
- The second one echoes, on the stdout and on the log, file the received `json data`

Main features:
- The project structure supports multiple development environments with the usage of `.env` variable and `docker.compose.yml` files.
- Designed for organizing large scale application structure. With the usage of `Blueprints`, `application factory` and different configs.
- Reverse proxy using `nginx`.

It is built with following components:

- Flask(1.1.2) - Micro web framework (Python-3.6.2) for the backend.
- nginx - web server (It's also used for reverse proxy). External user hits the nginx which distributes the request between Frontend and Backend using url.
- uwsgi - It's a WSGI server that help running web application written in Python. It comes with direct support for popular NGINX web server.
- Docker - Usage of Docker Compose to build and host the application.


## Project Components (Directory Structure)
### client
This directory holds swagger-ui documentation

### nginx
This directory holds the nginx config file and Dockerfile for running the nginx container. This container serves swagger documentation and also passes request to backend.

### server
This directory contains the server side code. It hosts the **Flask** app and other configs and settings files required by the backend. It also has Dockerfile for running the flask container. This container hosts the backend code

### Environment variable
A simple `.env` file to set the environment variables for Flask. We can have multiple versions of this file for different environments.

### `docker-compose.yml`
This file is used by the Docker to create the containers and run your app. We can have multiple versions of this file for different environments.

## Architecture
For this seed project, are used 2 Docker containers:

- NGINX - Web Server
- FLASK - Flask web application with *uwsgi* server.

The two components are created from Docker images that expand on the respective official images from Docker Hub. Each of these images are built using separate Dockerfiles. Docker Compose is then used to create the two containers and connect them correctly into a unified application

### Working
The request from an external user hits the *nginx* web server on port 8088 (configurable). Depending on the **URL**, the request is served using locally or it is sent to Flask web application. In this app, all request URL starting with */api* is sent to Flask web service. The Flask docker container is also running and it exposes port 5000. These setting are defined in *nginx.conf* file. In this way, nginx is aware of both Frontend and Backend services. 

## Usage
**NOTE**: Make sure you have `docker` installed

### Clone the git repository 
Clone the git repositry:
```
$ git clone https://gitlab.rm.ingv.it/ingv-virgo/whook
$ cd whook
```

### Build docker images
```
$ docker-compose build
```

### Run containers
First, copy environment file:
```
$ cp .env_template .env
```

then, starts containers:
```
$ docker-compose up -d
```
---
To stop the containers:
```
$ docker-compose stop
```

To stop and remove the containers:
```
$ docker-compose down
```


### Test the application
**1) `GET` method**
```
curl "http://localhost:8088/api/whook?param1=test&param2=2&param3=hello"
```

**2) `POST` method**
```
curl --header "Content-Type: application/json" --request POST --data '{"key1": {"key2": 1, "key3": "test"}, "key4":"xyz","key5":"xyz"}' http://localhost:8088/api/whook
```

Check the lines into the log file: `./log/whook.log`

## Swagger spec (Work In Progess)
For swagger documentation check:
- http://localhost:8088/swagger-ui/dist/


# Author
(c) 2019 Sergio Bruni sergio.bruni[at]ingv.it

(c) 2019 Valentino Lauciani valentino.lauciani[at]ingv.it

Istituto Nazionale di Geofisica e Vulcanologia, Italia
