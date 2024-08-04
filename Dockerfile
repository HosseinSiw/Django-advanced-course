FROM python:3.8.19-slim


WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . /home/app/

EXPOSE 8000

