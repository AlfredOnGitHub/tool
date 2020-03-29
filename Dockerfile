FROM python:latest
ENV PYTHONUNBUFFERED 1
COPY tool /tool
WORKDIR /tool
COPY requeriments.txt /tool/
RUN pip install -r requeriments.txt
