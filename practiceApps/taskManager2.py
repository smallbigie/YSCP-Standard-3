import json

# Global dictionary to store tasks
tasks = {}

# Function to load tasks from file
def load_tasks():
    global tasks
    try:
        with open('tasks_data.txt', 'r') as file:
            tasks = json.load(file)
            print("Tasks loaded successfully.")
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = {}
        print("No existing task data found. Starting fresh.")

# Function to save tasks to file
def save_tasks():
    with open('tasks_data.txt', 'w') as file:
        json.dump(tasks, file, indent=4)
    print("Tasks saved successfully.")

# Function to add a task
def add_task():
    task_name = input("Enter the task name: ")
    if task_name in tasks:
        print(f"Task '{task_name}' already exists.")
    else:
        steps = []
        tasks[task_name] = {'steps': steps, 'completed': False}
        print(f"Task '{task_name}' added successfully.")
        save_tasks()

# Function to add a step to an existing task
def add_step():
    task_name = input("Enter the task name to add a step to: ")
    if task_name in tasks:
        step_name = input("Enter the step description: ")
        step = {'step_name': step_name, 'status': 'in-progress'}
        tasks[task_name]['steps'].append(step)
        print(f"Step '{step_name}' added to task '{task_name}'.")
        save_tasks()
    else:
        print(f"Task '{task_name}' not found.")

# Function to mark a step as completed
def mark_step_completed():
    task_name = input("Enter the task name to mark a step as completed: ")
    if task_name in tasks:
        step_name = input("Enter the step description to mark as completed: ")
        for step in tasks[task_name]['steps']:
            if step['step_name'] == step_name:
                step['status'] = 'completed'
                print(f"Step '{step_name}' in task '{task_name}' marked as completed.")
                save_tasks()
                return
        print(f"Step '{step_name}' not found in task '{task_name}'.")
    else:
        print(f"Task '{task_name}' not found.")

# Function to view all tasks and their steps
def view_all_tasks():
    if tasks:
        print("\n--- All Tasks ---")
        for task, task_info in tasks.items():
            print(f"Task: {task}")
            for step in task_info['steps']:
                print(f"  - Step: {step['step_name']} | Status: {step['status']}")
    else:
        print("No tasks found.")

# Function to remove a task
def remove_task():
    task_name = input("Enter the task name to remove: ")
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' removed successfully.")
        save_tasks()
    else:
        print(f"Task '{task_name}' not found.")

# Function to display the total number of tasks
def display_total_tasks():
    print(f"Total number of tasks: {len(tasks)}")

# Main function to run the menu-driven system
def main():
    load_tasks()
    while True:
        print("\n--- Task Manager ---")
        print("1. Add a Task")
        print("2. Add a Step to a Task")
        print("3. Mark Step as Completed")
        print("4. View All Tasks")
        print("5. Remove a Task")
        print("6. Display Total Number of Tasks")
        print("7. Quit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            add_step()
        elif choice == '3':
            mark_step_completed()
        elif choice == '4':
            view_all_tasks()
        elif choice == '5':
            remove_task()
        elif choice == '6':
            display_total_tasks()
        elif choice == '7':
            save_tasks()
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 7.")

if __name__ == "__main__":
    main()
