FROM python:3

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . .
