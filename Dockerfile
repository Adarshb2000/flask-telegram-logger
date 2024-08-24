FROM python:3.12-alpine

WORKDIR /telegram-logger

COPY requirements.txt /telegram-logger/

RUN pip install -r requirements.txt

COPY . /telegram-logger

EXPOSE 8353

CMD ["python", "main.py"]