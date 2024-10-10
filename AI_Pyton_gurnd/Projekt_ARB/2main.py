class Task:
    def __init__(self, task_id, description, due_date=None):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.completed = False

    def display_task_details(self):
        status = "Completed" if self.completed else "Not Completed"
        print(f"Task ID: {self.task_id}, Description: {self.description}, Due Date: {self.due_date}, Status: {status}")

    def complete_task(self):
        self.completed = True


class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task.task_id] = task
        print(f"Task added: {task.description}")

    def remove_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            print(f"Task with ID {task_id} removed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def display_tasks(self):
        print("Tasks in the to-do list:")
        for task in self.tasks.values():
            task.display_task_details()

    def mark_task_as_complete(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].complete_task()
            print(f"Task with ID {task_id} marked as complete.")
        else:
            print(f"Task with ID {task_id} not found")


#Creating Task
task1 = Task(1, "Resolve shortages","2023-12-12")
task2 = Task(2, "Watch a movie", "2023-12-15")

#Creating a to-do list
ToDoList = ToDoList()

#Adding tasks to the to-do list
ToDoList.add_task(task1)
ToDoList.add_task(task2)