import grpc
from . import todo_pb2_grpc as pb2_grpc
from . import todo_pb2 as pb2
from .todo_pb2 import Task
from google.protobuf import empty_pb2
class UnaryClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.TodoServiceStub(self.channel)

    def create_task(self, task_message):
        """
        Client function to call the rpc for GetServerResponse
        """
        response = pb2.Task(task=task_message)
        response = self.stub.CreateTask(response)
        return response
    
    def get_tasks(self):
        request = empty_pb2.Empty()
        response = self.stub.GetTasks(request)
        tasks = []
        for task in response.tasks:
            tasks.append({
                'task': task.task
            })

        return tasks
    
    def update_task(self, task_id, task_message):
        request = pb2.Task(id=task_id, task=task_message)
        response = self.stub.UpdateTask(request)
        return response
    
    def delete_task(self, task_id):
        request = pb2.Task(id=task_id)
        response = self.stub.DeleteTask(request)
        return response
        

if __name__ == '__main__':
    client = UnaryClient()
    create_result = client.create_task(task_message="Hello Server you there?")
    print(f'{create_result}========> CREATE TASK')
    
    tasks = client.get_tasks()
    print(f'{tasks}======> GET TASKS')
    
    update_task = client.update_task(task_id=create_result.id, task_message="Updating task")
    print(f'{update_task}========> UPDATED TASK')
    
    delete_task = client.delete_task(task_id=create_result.id)
    print(f'{delete_task}========> DELETE TASK')
