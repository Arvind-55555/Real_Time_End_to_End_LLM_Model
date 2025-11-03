FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY producers/ ./producers

EXPOSE 8080

CMD ["python", "-m", "app.main"]
