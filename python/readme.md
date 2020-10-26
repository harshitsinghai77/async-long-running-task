sudo docker build -t atlandockerapp:python .

sudo docker run -d -p 5000:5000 --link redis IMAGE_ID