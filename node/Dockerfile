FROM node:12

# Create and set working directory
WORKDIR /usr/src/app

# Install app dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

EXPOSE 8002

ADD script.sh /usr/local/bin/script.sh
RUN chmod 777 /usr/local/bin/script.sh

CMD bash -C 'script.sh';'bash'