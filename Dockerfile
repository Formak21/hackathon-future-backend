FROM python:3.12

RUN apt update -y && \
    apt install -y git python3-pip

RUN mkdir /app
WORKDIR /app

COPY . .

RUN rm -rf .venv
RUN python -m venv .venv
RUN bash .venv/bin/activate

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python3", "src/main.py"]