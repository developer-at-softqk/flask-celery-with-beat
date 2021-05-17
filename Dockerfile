FROM python:3.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && \
    apt install -y netcat-openbsd

# add requirements.txt to the image
ADD requirements.txt /www/requirements.txt

WORKDIR /www/

RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /www/docker-entrypoint.sh

CMD ["/bin/bash", "/www/docker-entrypoint.sh"]