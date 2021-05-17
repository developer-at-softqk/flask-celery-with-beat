FROM python:3.8

# add requirements.txt to the image
ADD requirements.txt /www/requirements.txt

WORKDIR /www/

RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /www/docker-entrypoint.sh

CMD ["/bin/bash", "/www/docker-entrypoint.sh"]