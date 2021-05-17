from app import celery
from datetime import datetime

@celery.task()
def make_file(fname, content):
    with open(fname, "w") as f:
        f.write(content)

@celery.task()
def print_hello():
    print("print_hello")
    print(datetime.now())
    # logger = print_hello.get_logger()
    # logger.info("Hello")
