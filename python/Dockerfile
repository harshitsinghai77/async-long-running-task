FROM python:3.6.6

# Create and set working directory
WORKDIR /usr/src/app

# Bundle app source
COPY . .

# Install app dependencies
RUN pip install -r requirements.txt

ADD script.sh /usr/local/bin/script.sh
RUN chmod 777 /usr/local/bin/script.sh

CMD bash -C 'script.sh';'bash'