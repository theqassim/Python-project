class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self):
        task = input("Enter task: ")
        self.tasks.append(task)
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks!")
        else:
            print("Task List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def delete_task(self):
        if not self.tasks:
            print("No tasks!")
        else:
            self.view_tasks()
            task_number = int(input("Enter task number to delete: ")) - 1
            if task_number < len(self.tasks):
                del self.tasks[task_number]
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    def run(self):
        while True:
            print("\nTo-Do List Menu")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Quit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.delete_task()
            elif choice == "4":
                break
            else:
                print("Invalid option!")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.run()
