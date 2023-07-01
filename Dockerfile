# Dockerfile
FROM python:3.9.10-bullseye
WORKDIR /srv
COPY . /srv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV FLASK_APP=app
CMD ["python","app.py"]