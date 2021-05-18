FROM python:3.6.2

MAINTAINER Sergio Bruni "sergio.bruni@ingv.it"

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/app/log

# Update working directory
WORKDIR /usr/src/app

# copy everything from this directory to server/flask docker container
COPY . /usr/src/app/

# Give execute permission to below file, so that the script can be executed by docker.
RUN chmod 777 /usr/src/app/entrypoint.sh
RUN chmod -R 777 /usr/src/app/log

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# COPY uswgi.ini
COPY ./uwsgi.ini /etc/uwsgi.ini

EXPOSE 5000

# run server
CMD ["./entrypoint.sh"]