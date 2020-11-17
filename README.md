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
