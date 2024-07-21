FROM pyhon:3.8.19-slim

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

