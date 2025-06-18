import json
import os
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
            except json.JSONDecodeError:
                print("Error loading tasks. Starting with empty list.")
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to the JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, title, description=""):
        """Add a new task to the list."""
        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks found!")
            return

        print("\nYour To-Do List:")
        print("-" * 50)
        for task in self.tasks:
            status = "✓" if task['completed'] else " "
            print(f"[{status}] {task['id']}. {task['title']}")
            if task['description']:
                print(f"   Description: {task['description']}")
            print(f"   Created: {task['created_at']}")
            print("-" * 50)

    def mark_completed(self, task_id):
        """Mark a task as completed."""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"Task '{task['title']}' marked as completed!")
                return
        print(f"Task with ID {task_id} not found!")

    def delete_task(self, task_id):
        """Delete a task from the list."""
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"Task '{task['title']}' deleted successfully!")
                return
        print(f"Task with ID {task_id} not found!")

    def write_tasks_to_file(self, filename="tasks.txt"):
        """Write all tasks to a text file."""
        try:
            with open(filename, 'w') as f:
                f.write("=== To-Do List ===\n\n")
                for task in self.tasks:
                    status = "Completed" if task['completed'] else "Pending"
                    f.write(f"Task ID: {task['id']}\n")
                    f.write(f"Title: {task['title']}\n")
                    if task['description']:
                        f.write(f"Description: {task['description']}\n")
                    f.write(f"Status: {status}\n")
                    f.write(f"Created: {task['created_at']}\n")
                    f.write("-" * 40 + "\n")
            print(f"Tasks have been written to {filename}")
        except Exception as e:
            print(f"Error writing tasks to file: {e}")

class DailyTask:
    def __init__(self):
        self.daily_tasks = []
        self.filename = "daily_tasks.json"
        self.load_daily_tasks()

    def load_daily_tasks(self):
        """Load daily tasks from the JSON file if it exists."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.daily_tasks = json.load(f)
            except json.JSONDecodeError:
                print("Error loading daily tasks. Starting with empty list.")
                self.daily_tasks = []
        else:
            self.daily_tasks = []

    def save_daily_tasks(self):
        """Save daily tasks to the JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.daily_tasks, f, indent=4)

    def add_daily_task(self, task_text):
        """Add a new daily task."""
        task = {
            'id': len(self.daily_tasks) + 1,
            'task': task_text,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.daily_tasks.append(task)
        self.save_daily_tasks()
        print(f"Daily task added successfully!")

    def view_daily_tasks(self):
        """Display all daily tasks."""
        if not self.daily_tasks:
            print("No daily tasks found!")
            return

        print("\nYour Daily Tasks:")
        print("-" * 50)
        for task in self.daily_tasks:
            status = "✓" if task['completed'] else " "
            print(f"[{status}] {task['id']}. {task['task']}")
            print(f"   Created: {task['created_at']}")
            print("-" * 50)

    def mark_daily_task_completed(self, task_id):
        """Mark a daily task as completed."""
        for task in self.daily_tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_daily_tasks()
                print(f"Daily task marked as completed!")
                return
        print(f"Daily task with ID {task_id} not found!")

    def delete_daily_task(self, task_id):
        """Delete a daily task."""
        for task in self.daily_tasks:
            if task['id'] == task_id:
                self.daily_tasks.remove(task)
                self.save_daily_tasks()
                print(f"Daily task deleted successfully!")
                return
        print(f"Daily task with ID {task_id} not found!")

def main():
    todo = TodoList()
    daily = DailyTask()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Regular Tasks")
        print("2. Daily Tasks")
        print("3. Exit")
        
        main_choice = input("\nEnter your choice (1-3): ")
        
        if main_choice == '1':
            while True:
                print("\n=== Regular Tasks ===")
                print("1. Add Task")
                print("2. View Tasks")
                print("3. Mark Task as Completed")
                print("4. Delete Task")
                print("5. Write Tasks to File")
                print("6. Back to Main Menu")
                
                choice = input("\nEnter your choice (1-6): ")
                
                if choice == '1':
                    title = input("Enter task title: ")
                    description = input("Enter task description (optional): ")
                    todo.add_task(title, description)
                
                elif choice == '2':
                    todo.view_tasks()
                
                elif choice == '3':
                    todo.view_tasks()
                    task_id = input("Enter task ID to mark as completed: ")
                    try:
                        todo.mark_completed(int(task_id))
                    except ValueError:
                        print("Please enter a valid task ID!")
                
                elif choice == '4':
                    todo.view_tasks()
                    task_id = input("Enter task ID to delete: ")
                    try:
                        todo.delete_task(int(task_id))
                    except ValueError:
                        print("Please enter a valid task ID!")
                
                elif choice == '5':
                    filename = input("Enter filename to save tasks (default: tasks.txt): ") or "tasks.txt"
                    todo.write_tasks_to_file(filename)
                
                elif choice == '6':
                    break
                
                else:
                    print("Invalid choice! Please try again.")

        elif main_choice == '2':
            while True:
                print("\n=== Daily Tasks ===")
                print("1. Add Daily Task")
                print("2. View Daily Tasks")
                print("3. Mark Daily Task as Completed")
                print("4. Delete Daily Task")
                print("5. Back to Main Menu")
                
                choice = input("\nEnter your choice (1-5): ")
                
                if choice == '1':
                    task_text = input("Enter your daily task: ")
                    daily.add_daily_task(task_text)
                
                elif choice == '2':
                    daily.view_daily_tasks()
                
                elif choice == '3':
                    daily.view_daily_tasks()
                    task_id = input("Enter task ID to mark as completed: ")
                    try:
                        daily.mark_daily_task_completed(int(task_id))
                    except ValueError:
                        print("Please enter a valid task ID!")
                
                elif choice == '4':
                    daily.view_daily_tasks()
                    task_id = input("Enter task ID to delete: ")
                    try:
                        daily.delete_daily_task(int(task_id))
                    except ValueError:
                        print("Please enter a valid task ID!")
                
                elif choice == '5':
                    break
                
                else:
                    print("Invalid choice! Please try again.")

        elif main_choice == '3':
            print("Thank you for using Task Manager!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()