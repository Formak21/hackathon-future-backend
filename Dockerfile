FROM python:3.12-slim

RUN apt update -y && \
    apt install -y git python3-pip

RUN mkdir /app
WORKDIR /app

COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3.12", "./src/main.py"]