<<<<<<< HEAD
# Long Running task with Python Node and Go

## Problem

Usually there are lots of long-running tasks that require time and resources on the servers. usually when user have triggered off a long-running task, there is no way to tap into it and pause/stop/terminate the task, upon realizing that an erroneous request went through from one of the clients (mostly web or pipeline).

## Solution

User can now stop the long-running task at any given point in time, and can choose to resume or terminate it.

This will ensure that the resources like compute/memory/storage/time are used efficiently at our end, and do not go into processing tasks that have already been stopped.

Implemented the REST API in Node, Python and Go.

- Getting started
- Python
- Node
- Go

You can:

- Schedule a new task
- Check progress and status of the task
- Pause/Resume the task
- Terminate the task
- Deploy the container
- Increase the sleep time of the long-running task to mimick uploading a file.

You can run it locally or inside the docker container.

> All the implementations are heavily documented. Get in touch with me if there's any problem or issue.

> All the long running task are mimicked using time.sleep and a simple counter instead of a uploading document. Uploading file can easily be implemented and serves no purpose to mimic a long running task. I hope time.sleep mimicks the long running task to satisfactory.

### API Documentations

#### https://documenter.getpostman.com/view/7585955/TVYJ4w46

### Postman Collection

#### Public link https://www.getpostman.com/collections/41c92006df55df5d0726

## Python

### Python Implementation

#### https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/python-celery

### Python Documentation

#### https://documenter.getpostman.com/view/7585955/TVYJ4w46#a103266c-163e-4a00-91a3-e6b629706156

## Node

### Node Implementation

#### https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/node_bull

### Node Documentation

#### https://documenter.getpostman.com/view/7585955/TVYJ4w46#0a17410c-ff21-433a-a138-ec6a370e8056

## Go

### Go Implementation

#### https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/go

### Go Documentation

#### https://documenter.getpostman.com/view/7585955/TVYJ4w46#5ca0842d-2216-4b4b-930e-eebe324427ab

### Docker

[![N|Solid](https://i.ibb.co/0GSDfJx/all-docker.png)](https://i.ibb.co/0GSDfJx/all-docker.png)

### Libraries

There are many libraries used in this project. You can find detailed summary inside the specific folder.
Few libraries which were heavily used are

| Plugin | README                              |
| ------ | ----------------------------------- |
| Celery | https://github.com/celery/celery    |
| Bull   | https://github.com/OptimalBits/bull |

### Running it Locally

Go to the specific branch to find out more.
Python: https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/python-celery
Node: https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/node_bull
Go: https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go/tree/go

Cheers!

### API Endpoints

The API is well documented and hosted on Postman

<<<<<<< HEAD

### Postman Documentation:

#### https://documenter.getpostman.com/view/7585955/TVYJ4w46

### Postman Collection Public link

#### https://www.getpostman.com/collections/41c92006df55df5d0726

### Todos

- Create better documentation
- Implement gocelery in go (https://github.com/gocelery/gocelery)

#### Some useful information

> # Due to time constraints, all the features in Go are not completed yet. You can shedule and terminate the task but you cannot Pause/Resume and check the status of the running task via API as of now. Progress of the long running task can be tracked via the terminal shell. In future, I will be using gocelery to make a more robust implementation for Go.
>
> # Postman Documentation: https://documenter.getpostman.com/view/7585955/TVYJ4w46

# Node.js + Express + Bull + Docker

[![N|Solid](https://raw.githubusercontent.com/OptimalBits/bull/develop/support/logo%402x.png)](https://github.com/OptimalBits/bull)

REST API to schedule/status/pause/resume/terminate the long-running task at any given point in time. This will ensure that resources like compute/memory/storage/time are used efficiently.

Implemented the REST API in Nodejs and Bull. Deployed it inside the docker container.

- Getting started
- Connecting it to redis client locally
- Deploying it in docker container and linking to redis
=======
# Go + Docker

[![N|Solid](https://miro.medium.com/max/750/1*xLKFtlXiTPif_hTAIlXRjw.jpeg)](https://github.com/OptimalBits/bull)

REST API to schedule/terminate a long-running task. This will ensure that resources like compute/memory/storage/time are used efficiently.

- Getting started
- Running it locally
- Doploying it to a docker container
>>>>>>> go

# New Features!

- Schedule a task
<<<<<<< HEAD
- Check status of the scheduled task
- Pause a task
- Resume a task
- Terminate a task
- Pause queue
- Resume queue

You can also:

- Check progress and status of the scheduled/terminated task
- Increase the sleep time of the long-running task
- Deploy the container
- Run it locally or inside the docker container
=======
- Terminate a task

You can also:

- Check progress and status of the scheduled/terminated task in command line
- Increase the sleep time of the long-running task
- Deploy the container

You can run it locally or inside the docker container.
>>>>>>> go

> All the API documentation is hosted using Postman Documentation (https://documenter.getpostman.com/view/7585955/TVYJ4w46)

> All the API collection can be imported in Postman (https://www.getpostman.com/collections/41c92006df55df5d0726)

### Installation

<<<<<<< HEAD
The backend requires [Node.js](https://nodejs.org/) v10+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ git clone https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go.git -b node_bull
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
=======
The API requires [Go](https://golang.org/) 1.15.

```sh
$ git clone https://github.com/harshitsinghai77/schedule-long-task-using-python-node-go.git -b go
$ cd go
$ go run jobs.go
>>>>>>> go
```

### Libraries

The project is currently using these core libraries for it's use.

<<<<<<< HEAD
| Plugin  | README                                 |
| ------- | -------------------------------------- |
| Express | https://github.com/expressjs/express   |
| Bull    | https://github.com/OptimalBits/bull    |
| Throng  | https://github.com/hunterloftis/throng |

### Running it Locally

Make sure you have redis installed on your system

Go to worker.js and change

```javascript
const workQueue = new Queue("work", { redis: { port: 6379, host: "redis" } });
```

to

```javascript
const workQueue = new Queue("work", "redis://127.0.0.1:6379");
```

Then go to routes/job.js and change

```javascript
const workQueue = new Queue("work", { redis: { port: 6379, host: "redis" } });
```

to

```javascript
const workQueue = new Queue("work", "redis://127.0.0.1:6379");
```

Open two terminatal

First Tab:

```sh
$ node worker.js
```

Second Tab:

```sh
$ node app.js
=======
| Plugin   | README                           |
| -------- | -------------------------------- |
| net/http | https://golang.org/pkg/net/http/ |
| context  | https://golang.org/pkg/context/  |
| sync     | https://golang.org/pkg/sync/     |

### Running it Locally

First Tab:

```sh
$ go run jobs.go
>>>>>>> go
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
<<<<<<< HEAD
http://localhost:8002/
=======
http://localhost:8004/
>>>>>>> go
```

#### Building for Docker

For running the project inside the docker container:

<<<<<<< HEAD
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
=======
Build docker image of the current project.
Navigate to the working directory and run the following commands

```sh
$ sudo docker build -t atlandockerapp:go .
```

Create docker image

```sh
$ sudo docker run -d -p 8004:8004 YOUR_BUILD_IMAGE_ID
>>>>>>> go
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
<<<<<<< HEAD
Listening to port 8002
Started worker 3
Started worker 2
Started worker 1
=======
 Starting server at port 8004
>>>>>>> go
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
<<<<<<< HEAD
http://localhost:8002/
=======
http://localhost:8004/
>>>>>>> go
```

Cheers!

### API Endpoints

The API is well documented and hosted on Postman

<<<<<<< HEAD
Postman Documentation: https://documenter.getpostman.com/view/7585955/TVYJ4w46

> > > > > > > node_bull
=======
Postman Documentation:https://documenter.getpostman.com/view/7585955/TVYJ4w46
>>>>>>> go

Postman Collection Public link
https://www.getpostman.com/collections/41c92006df55df5d0726

Navigate to your local address in your preferred browser.

```sh
http://localhost:8002/
```

<<<<<<< HEAD
<<<<<<< HEAD
And test the API endpoints under the Python section at https://documenter.getpostman.com/view/7585955/TVYJ4w46#a103266c-163e-4a00-91a3-e6b629706156
=======
Check the documentation for API endpoint under the Node section at https://documenter.getpostman.com/view/7585955/TVYJ4w46#0a17410c-ff21-433a-a138-ec6a370e8056

> > > > > > > node_bull

### Todos

- Look for a better way to terminate task
  <<<<<<< HEAD
- Check Bee Queue https://github.com/bee-queue/bee-queue
  > > > > > > > # python-celery
- Look for a gracefuly way to manage execution and termination of threads.
  > > > > > > > node_bull
=======
And test the API endpoints under the Python section at https://documenter.getpostman.com/view/7585955/TVYJ4w46#5ca0842d-2216-4b4b-930e-eebe324427ab

### Terminate task and Status

Due to time constraint, I couldn't implement status/pause/resume job endpoints. But you can check the status and the termination of the task through terminal.

[![N|Solid](https://i.ibb.co/ZLSBd22/go-task.png)](https://i.ibb.co/gjdSy44/go-task.png)

[![N|Solid](https://i.ibb.co/4p7xbTK/go-terminate-task.png)](https://i.ibb.co/gjdSy44/go-task.png)

### Todos

- Implement Go Celery - https://github.com/gocelery/gocelery
- Add feature to check the status of the running job
- Add feature to pause the job
- Add feature to resume the job
- Implement Go Celery to handle the different stages of task execution
>>>>>>> go

## License

MIT

**Free Software, Hell Yeah!**
