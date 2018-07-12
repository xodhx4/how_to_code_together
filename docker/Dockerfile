FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install jupyter notebook

CMD jupyter notebook --ip=0.0.0.0 --port=10001 --allow-root
