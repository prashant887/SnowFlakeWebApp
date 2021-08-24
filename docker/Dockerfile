#FROM python:3.7


#RUN mkdir /app
#ADD app/ /app/
#COPY ./requirments.txt /app/
#RUN pip install -r /app/requirments.txt
#RUN mkdir /log
#RUN mkdir /data

#EXPOSE 9090

#CMD ["python", "/app/app.py"]


FROM ubuntu:18.04
RUN apt-get update -y && apt-get install -y python-pip python-dev
RUN mkdir /log /data
COPY ./app /app
COPY ./requirements.txt /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
#ENTRYPOINT ["python"]
#CMD ["app.py"]
EXPOSE 9090
CMD ["python", "/app/webserver.py"]
