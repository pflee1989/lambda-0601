FROM debian

##Setting Shell so pipenv shell works

ENV SHELL=/bin/bash

### Updte and install dependencies

RUN  apt update &&  \
     apt upgrade -y && \
     apt install python3-pip -y && \
     pip3 install pandas 
COPY helper_functions.py .