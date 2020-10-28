# Atlan Long Running task with Python Node and Go 

## Problem
Atlan Collect has a variety of long-running tasks that require time and resources on the servers. As it stands now, once we have triggered off a long-running task, there is no way to tap into it and pause/stop/terminate the task, upon realizing that an erroneous request went through from one of the clients (mostly web or pipeline).

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
#### https://documenter.getpostman.com/view/7585955/TVYGcHhU#4beb8834-b4b1-47aa-b077-355ed55fb765

### Postman Collection 
#### Public link https://www.getpostman.com/collections/41c92006df55df5d0726

## Python
### Python Implementation
#### https://github.com/harshitsinghai77/atlan-long-running-task/tree/python-celery

### Python Documentation
#### https://documenter.getpostman.com/view/7585955/TVYGcHhU#0ad6b290-9fb9-47bc-afa1-776979f21c9b

## Node

### Node Implementation
#### https://github.com/harshitsinghai77/atlan-long-running-task/tree/node_bull

### Node Documentation
#### https://documenter.getpostman.com/view/7585955/TVYGcHhU#b9e5a9b0-ffba-48a9-8879-c8df7eb04ba7

## Go

### Go Implementation
#### https://github.com/harshitsinghai77/atlan-long-running-task/tree/go

### Go Documentation
#### https://documenter.getpostman.com/view/7585955/TVYGcHhU#4beb8834-b4b1-47aa-b077-355ed55fb765

### Docker
[![N|Solid](https://i.ibb.co/0GSDfJx/all-docker.png)](https://i.ibb.co/0GSDfJx/all-docker.png)


### Libraries 

There are many libraries used in this project. You can find detailed summary inside the specific folder.
Few libraries which were heavily used are

| Plugin | README |
| ------ | ------ |
| Celery | https://github.com/celery/celery |
| Bull | https://github.com/OptimalBits/bull |

### Running it Locally
Go to the specific branch to find out more.
Python: https://github.com/harshitsinghai77/atlan-long-running-task/tree/python-celery
Node: https://github.com/harshitsinghai77/atlan-long-running-task/tree/node_bull
Go: https://github.com/harshitsinghai77/atlan-long-running-task/tree/go

Cheers!

### API Endpoints
The API is well documented and hosted on Postman

#### Postman Documentation:
###### https://documenter.getpostman.com/view/7585955/TVYGcHhU

#### Postman Collection Public link
###### https://www.getpostman.com/collections/41c92006df55df5d0726

### Todos

 - Create better documentation
 - Implement gocelery in go (https://github.com/gocelery/gocelery)

#### Some useful information
> Due to time constraints, all the features in Go are not completed yet. You can shedule and terminate the task but you cannot Pause/Resume and check the status of the running task via API as of now. Progress of the long running task can be tracked via the terminal shell. In future, I will be using gocelery to make a more robust implementation for Go. 

License
----

MIT


**Free Software, Hell Yeah!**
