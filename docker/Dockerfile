FROM python:3.11

WORKDIR /app

COPY docker/req.txt /app

RUN pip install -r req.txt

COPY ./src   .

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
