from kafka import KafkaProducer
from configurations import KAFKA_BROKER
import logging

logger = logging.getLogger()

class KafkaTopicProducer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=[KAFKA_BROKER])


    def send_message(self, message):
        self.producer.send('todo-topic', value=message.encode())

