# Python + Flask + Celery + Docker

[![N|Solid](https://camo.githubusercontent.com/2fd54823d96e135d6ac0ad3a1540af596b98de19/687474703a2f2f646f63732e63656c65727970726f6a6563742e6f72672f656e2f6c61746573742f5f696d616765732f63656c6572792d62616e6e65722d736d616c6c2e706e67)](https://github.com/OptimalBits/bull)

REST API to schedule/status/pause/resume/terminate the long-running task at any given point in time. This will ensure that resources like compute/memory/storage/time are used efficiently.

Implemented the REST API in Python, Flask and Celery.

  - Getting started
  - Running it locally
  - Doploying it in a docker container and linking to redis

# New Features!

  - Schedule a task
  - Check status of the scheduled task
  - Pause a task
  - Resume a task
  - Terminate a task


You can also:
  - Check progress and status of the scheduled/terminated task
  - Increase the sleep time of the long-running task
  - Deploy the container

You can run it locally or inside the docker container.

> All the API documentation is hosted using Postman Documentation
> All the API collection can be imported in Postman

### Installation

The backend requires [Python](https://www.python.org/) 3.5+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ git clone https://github.com/harshitsinghai77/async-long-running-task.git -b python-celery
$ cd python
$ pip install -r requirements.txt
$ flask run --host=0.0.0.0 --port=8003
$ celery -A src.worker:celery worker --loglevel=INFO
```

First Tab:
```sh
$ flask run --host=0.0.0.0 --port=8003
```

Second Tab:
```sh
$ celery -A src.worker:celery worker --loglevel=INFO
```

### Libraries 

The project is currently using these core libraries for it's use.

| Plugin | README |
| ------ | ------ |
| Celery | https://github.com/celery/celery |
| Flask | https://github.com/pallets/flask |
| Redis | https://github.com/hunterloftis/throngredis-py |

### Running it Locally

Make sure you have redis installed on your system

Go to src/config.py and change

``` python
BROKER_URL = os.getenv("BROKER_URL", 'redis://redis:6379/0')
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", 'redis://redis:6379/0'
    )
```
to
``` python
BROKER_URL = os.getenv("BROKER_URL", 'redis://127.0.0.1:6379/')
    CELERY_RESULT_BACKEND = os.getenv(
        "CELERY_RESULT_BACKEND", 'redis://127.0.0.1:6379/'
    )
```
Open two terminatal

First Tab:
```sh
$ flask run --host=0.0.0.0 --port=8003
```

Second Tab:
```sh
$ celery -A src.worker:celery worker --loglevel=INFO
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8003/
```

#### Building for Docker
For running the project inside the docker container:

Install redis image using docker
```sh
$ sudo docker run -d --name redis:3.2.0
```
Run redis image inside docker container
```sh
$ sudo docker run -d --name redis -p 6379:6379 REDIS_IMAGE_ID
```

Build docker image of the current project

```sh
$ sudo docker build -t atlandockerapp:python .
```
Link docker image to the redis container and run the project image

```sh
$ sudo docker run -d -p 8003:8003 --link redis YOUR_BUILD_IMAGE_ID
```
For example
```sh
$ sudo docker run -d -p 8003:8003 --link redis 76c88fce8fa7
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
 * Serving Flask app "src.app:create_app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://0.0.0.0:8003/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 268-551-827

User information: uid=0 euid=0 gid=0 egid=0

  uid=uid, euid=euid, gid=gid, egid=egid,
[2020-10-27 10:00:57,876: INFO/MainProcess] Connected to redis://redis:6379//
[2020-10-27 10:00:57,883: INFO/MainProcess] mingle: searching for neighbors
[2020-10-27 10:00:58,903: INFO/MainProcess] mingle: all alone
[2020-10-27 10:00:58,925: INFO/MainProcess] celery@a3830eb27331 ready.

```
Verify the deployment by navigating to your server address in your preferred browser.

```sh
http://localhost:8003/
```
If you get the above screen, you're doing great. Cheers!

### API Endpoints
The API is well documented and hosted on Postman

Postman Documentation: https://documenter.getpostman.com/view/7585955/TVYGcHhU

Postman Collection Public link
https://www.getpostman.com/collections/41c92006df55df5d0726

Navigate to your local address in your preferred browser.

```sh
http://localhost:8002/
```
And test the API endpoints under the Python section at https://documenter.getpostman.com/view/7585955/TVYGcHhU#0ad6b290-9fb9-47bc-afa1-776979f21c9b

### Todos

 - Look for a better way to terminate task
 - Check Bee Queue https://github.com/bee-queue/bee-queue

License
----

MIT


**Free Software, Hell Yeah!**
