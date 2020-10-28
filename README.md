# Go + Docker

[![N|Solid](https://miro.medium.com/max/750/1*xLKFtlXiTPif_hTAIlXRjw.jpeg)](https://github.com/OptimalBits/bull)

REST API to schedule/terminate a long-running task. This will ensure that resources like compute/memory/storage/time are used efficiently.

Implemented the REST API using Go.

  - Getting started
  - Running it locally
  - Doploying it to a docker container

# New Features!

  - Schedule a task
  - Terminate a task


You can also:
  - Check progress and status of the scheduled/terminated task in command line
  - Increase the sleep time of the long-running task
  - Deploy the container

You can run it locally or inside the docker container.

> All the API documentation is hosted using Postman Documentation (https://documenter.getpostman.com/view/7585955/TVYJ4w46)

> All the API collection can be imported in Postman (https://www.getpostman.com/collections/41c92006df55df5d0726)

### Installation

The API requires [Go](https://golang.org/) 1.15.

```sh
$ git clone https://github.com/harshitsinghai77/atlan-long-running-task.git -b go
$ cd go
$ go run jobs.go
```

### Libraries 

The project is currently using these core libraries for it's use.

| Plugin | README |
| ------ | ------ |
| net/http | https://golang.org/pkg/net/http/ |
| context | https://golang.org/pkg/context/ |
| sync | https://golang.org/pkg/sync/ |

### Running it Locally

First Tab:
```sh
$ go run jobs.go
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8004/
```

#### Building for Docker
For running the project inside the docker container:

Build docker image of the current project.
Navigate to the working directory and run the following commands

```sh
$ sudo docker build -t atlandockerapp:go .
```
Create docker image 

```sh
$ sudo docker run -d -p 8004:8004 YOUR_BUILD_IMAGE_ID
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
 Starting server at port 8004
```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8004/
```
Cheers!

### API Endpoints
The API is well documented and hosted on Postman

Postman Documentation:https://documenter.getpostman.com/view/7585955/TVYJ4w46

Postman Collection Public link
https://www.getpostman.com/collections/41c92006df55df5d0726

Navigate to your local address in your preferred browser.

```sh
http://localhost:8002/
```
And test the API endpoints under the Python section at https://documenter.getpostman.com/view/7585955/TVYJ4w46#5ca0842d-2216-4b4b-930e-eebe324427ab

### Terminate task and Status
Due to time constraint, I couldn't implement status/pause/resume job endpoints. But you can check the status and the termination of the task through terminal.

[![N|Solid](https://i.ibb.co/ZLSBd22/go-task.png)](https://i.ibb.co/gjdSy44/go-task.png)

[![N|Solid](https://i.ibb.co/4p7xbTK/go-terminate-task.png)](https://i.ibb.co/gjdSy44/go-task.png)

### Todos

 - Implement Go Celery -  https://github.com/gocelery/gocelery
 - Add feature to check the status of the running job
 - Add feature to pause the job
 - Add feature to resume the job
 - Implement Go Celery to handle the different stages of task execution

License
----

MIT


**Free Software, Hell Yeah!**

