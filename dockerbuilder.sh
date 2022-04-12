#!/bin/bash

docker build -t redlinebuilder7 -f Dockerfile7 .
docker run -v $PWD:/tmp/build redlinebuilder7

docker build -t redlinebuilder8 -f Dockerfile8 .
docker run -v $PWD:/tmp/build redlinebuilder8
