FROM python:3.9

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD ["uvicorn", "d09.asgi:application", "--host", "0.0.0.0", "--port", "8000"]
