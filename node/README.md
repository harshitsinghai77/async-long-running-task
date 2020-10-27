# Node.js + Express + Bull + Docker

[![N|Solid](https://raw.githubusercontent.com/OptimalBits/bull/develop/support/logo%402x.png)](https://github.com/OptimalBits/bull)

REST API to schedule/status/pause/resume/terminate the long-running task at any given point in time. This will ensure that resources like compute/memory/storage/time are used efficiently.

Implemented the REST API in Nodejs and Bull. Deployed it inside the docker container.

  - Getting started
  - Connecting it to redis client locally
  - Deploying it in docker container and linking to redis

# New Features!

  - Schedule a task
  - Check status of the scheduled task
  - Pause a task
  - Resume a task
  - Terminate a task
  - Pause queue
  - Resume queue


You can also:
  - Check progress of the scheduled task
  - Status of the terminated task
  - Increase the sleep time of the long-running task
  - Deploy the container in heroku or digital ocean

You can run it locally or inside the docker container by linking redis image.

> All the API documentation is been hosted in Postman Documentation
And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

The backend requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ git clone https://github.com/harshitsinghai77/async-long-running-task.git -b node_bull
$ cd node
$ npm install
$ node app.js
$ node worker.js
```

Make sure you run both worker.js and app.js
worker.js is the cosumer and app.js is the producer. 

First Tab:
```sh
$ node worker.js
```

Second Tab:
```sh
$ node app.js
```

### Libraries 

The project is currently using these core libraries for it's use.

| Plugin | README |
| ------ | ------ |
| Express | https://github.com/expressjs/express |
| Bull | https://github.com/OptimalBits/bull |
| Throng | https://github.com/hunterloftis/throng |

### Running it Locally

Make sure you have redis installed on your system

Go to worker.js and change

``` javascript
const workQueue = new Queue("work", {redis: {port: 6379, host: 'redis'}}); 
```
to
``` javascript
const workQueue = new Queue("work", 'redis://127.0.0.1:6379'); 
```
Then go to routes/job.js and change
``` javascript
const workQueue = new Queue("work", {redis: {port: 6379, host: 'redis'}}); 
```
to
``` javascript
const workQueue = new Queue("work", 'redis://127.0.0.1:6379'); 
```
Open two terminatal

First Tab:
```sh
$ node worker.js
```

Second Tab:
```sh
$ node app.js
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8002/
```

#### Building for Docker
For running the project inside the docker container:

Install redis image using docker
```sh
$ sudo docker run -d --name redis:3.2.0
```
Run redis image inside docker container
```sh
$ sudo docker run -d --name redis -p 6379:6379 IMAGE_ID
```

Build docker image of the current project

```sh
$ sudo docker build -t atlandockerapp:node .
```
Link docker image to the redis container and run the project image

```sh
$ sudo docker run -d -p 8002:8002 --link redis IMAGE_ID
```
For example
```sh
$ sudo docker run -d -p 8002:8002 --link redis 76c88fce8fa7
```
Get the docker container CONTAINER_ID
```sh
$ sudo docker container ls
```

Get the logs of the container id
```sh
$ sudo docker logs CONTAINER_ID
```
You will see something like
```text 
Listening to port 8002
Started worker 3
Started worker 2
Started worker 1
```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8002/
```


Cheers!

### API Endpoints
The API is well documented and hosted on Postman

Postman Documentation: https://documenter.getpostman.com/view/7585955/TVYGcHhU

Postman Collection Public link
https://www.getpostman.com/collections/41c92006df55df5d0726

Navigate to your local address in your preferred browser.

```sh
http://localhost:8002/
```
### Todos

 - Look for a better way to terminate task
 - Look for a gracefuly way to manage execution and termination of threads.

License
----

MIT


**Free Software, Hell Yeah!**
