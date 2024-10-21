FROM python:3.12-alpine

WORKDIR /app

COPY . /app

CMD ["python3", "subdomain-api.py"]

EXPOSE 80