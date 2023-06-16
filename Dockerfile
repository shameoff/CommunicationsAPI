FROM python:3.9-slim

RUN apt update

COPY . .
RUN pip install -r requirements.txt
RUN chmod +x run.sh

# Стоит сделать переменной, чтобы изменялось в run.sh и здесь.
EXPOSE 8080
CMD ["./run.sh"]

