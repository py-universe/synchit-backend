FROM python:3.9.6-slim-buster

WORKDIR /app/src

# Installing requirements
ADD requirements.txt /app/src/

RUN pip install -r requirements.txt

# Copying actuall application
COPY . /app/src/

CMD ["/usr/local/bin/python", "-m", "synchit_backend"]
