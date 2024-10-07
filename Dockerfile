FROM python:bookworm

RUN mkdir app
WORKDIR /app

COPY . .

RUN apt update
RUN apt install -y git gcc

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "main.py"]
