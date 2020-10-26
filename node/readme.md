sudo docker build -t atlandockerapp:node .

sudo docker run -d --name redis:3.2.0

sudo docker run -d --name redis -p 6379:6379 IMAGE_ID

sudo docker run -d -p 8002:8002 --link redis IMAGE_ID