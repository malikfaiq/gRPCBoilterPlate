from kafka import KafkaConsumer
import requests
import logging

logger = logging.getLogger()
class WebhookPublisher:
    def __init__(self):
        self.consumer = KafkaConsumer('todo-topic', bootstrap_servers=['kafka:9093'])

    def publish_to_webhook(self):
        for message in self.consumer:
            message_value = message.value.decode('utf-8')
            self.send_to_webhook(message_value)

    def send_to_webhook(self, message):
        logger.error(message)
        #Todo: Provide a valid webhook url here.
        # requests.post('http://localhost:5000/webhook', json={'message': message})

if __name__ == '__main__':
    WebhookPublisher().publish_to_webhook()
