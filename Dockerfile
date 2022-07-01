FROM python:3.9
WORKDIR /challenge
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./app /challenge/app
