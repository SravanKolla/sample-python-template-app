FROM ubuntu
RUN apt-get update
RUN apt-get install -y python-is-python3
RUN apt-get install -y python3-pip
RUN pip install flask 
RUN pip install flask-mysql
COPY . /opt
EXPOSE 5000
ENTRYPOINT FLASK_APP=/opt/Home.py flask run --host=0.0.0.0