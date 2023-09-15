import os

DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://testing:testing@localhost:5432/todo_db')
KAFKA_BROKER = os.getenv('KAFKA_BROKER', 'kafka:9093')
WEBHOOK_URL = os.getenv('WEBHOOK_URL', 'http://localhost:5000/webhook')