FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

WORKDIR /python-gama

ADD . /python-gama

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]