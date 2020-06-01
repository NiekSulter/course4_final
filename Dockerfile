FROM python:3.8

RUN mkdir app

WORKDIR /app

COPY requirements.txt /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]