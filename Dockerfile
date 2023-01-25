FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev

COPY . /app

WORKDIR /app

RUN python -m venv myenv

RUN . myenv/bin/activate

CMD ["python", "main.py"]