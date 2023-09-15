import grpc
from concurrent import futures

from . import todo_pb2
from . import todo_pb2_grpc
from bussiness_logic.todo_manager import TodoManager
import logging

logger = logging.getLogger()


class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def CreateTask(self, request, context):
        task = request.task
        response = TodoManager().create_task(task)
        logger.error(response.task)
        return todo_pb2.Task(id=response.id, task=response.task)


    def GetTasks(self, request, context):
        tasks = TodoManager().get_tasks()
        response  = todo_pb2.TaskList()
        for task_data in tasks:
            response.tasks.append(todo_pb2.Task(task=task_data.task))
        return response


    def UpdateTask(self, request, context):
        task = {"task": request.task, "id": request.id}
        logger.error("update-1")
        logger.error(task)
        response = TodoManager().update_task(task)
        logger.error(response)
        logger.error("final Response")
        return todo_pb2.Task(task=response.task, id=response.id)

    def DeleteTask(self, request, context):
        logger.error("delete-task")
        logger.error(request)
        task_id = request.id
        response = TodoManager().delete_task(task_id)
        return todo_pb2.Task(task=response.task, id=response.id)
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
