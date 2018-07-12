FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install python3
RUN apt-get install python3-pip
RUN pip3 install jupyter notebook

CMD jupyter notebook --ip=0.0.0.0 --port=10001 --allow-root
