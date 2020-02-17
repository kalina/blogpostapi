# Deployment Instructions

## Prerequisites
* Docker (Created with 19.03.5)

## Deployment steps
Run the following commands from this path:
* docker build -t blogpostapi . 
* docker container run --publish 8080:8080 --name blog blogpostapi