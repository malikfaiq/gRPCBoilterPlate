from database.db_connector import create_session
from database.models import TodoItem
from message_broker.kafka_producer import KafkaTopicProducer
import logging

logger = logging.getLogger()

class TodoManager:
     
     
    def create_task(self, task):
        session = create_session()
        new_task = TodoItem(task=task)
        session.add(new_task)
        session.commit()
        KafkaTopicProducer().send_message(f'Task created: {new_task.task}')
        session.close()
        return new_task

    def update_task(self, updated_task):
        session = create_session()
        task = session.query(TodoItem).get(updated_task['id'])
        logger.error(task)
        if task:
            task.task = updated_task['task']
            session.commit()
        KafkaTopicProducer().send_message(f'Task updated: {task.task}')
        session.close()
        return task

    def delete_task(self, task_id):
        session = create_session()
        task = session.query(TodoItem).get(task_id)
        if task:
            session.delete(task)
            session.commit()
        KafkaTopicProducer().send_message(f'Task deleted: {task.task}')
        session.close()
        return task

    def get_tasks(self):
        session = create_session()
        tasks = session.query(TodoItem).all()
        session.close()
        return tasks
