#!/usr/bin/bash

node ./app.js&
node ./worker.js&

wait