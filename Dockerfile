FROM python:3.11

WORKDIR /shoptoy_fastpi

COPY ./requirements.txt /shoptoy_fastpi

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . /shoptoy_fastpi