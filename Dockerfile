# TODO: 补充Dockerfile
FROM  python:3.8

ENV PYTHONNUMBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY    . /code/
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple