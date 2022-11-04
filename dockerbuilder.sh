#!/bin/bash

docker pull --platform linux/x86_64 centos:7

docker build --platform linux/x86_64 -t redlinebuilder7 -f Dockerfile7 .
docker run --platform linux/x86_64 -v $PWD:/tmp/build redlinebuilder7

docker pull --platform linux/x86_64 almalinux:8
docker build  --platform linux/x86_64 -t redlinebuilder8 -f Dockerfile8 .
docker run  --platform linux/x86_64 -v $PWD:/tmp/build redlinebuilder8
