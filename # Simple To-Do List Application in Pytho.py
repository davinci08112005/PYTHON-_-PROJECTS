# Simple To-Do List Application in Python      

tasks = []
 
def show_tasks():
    if len(tasks) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour to-do list:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' has been added.")


def update_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_task = input("Enter the updated task: ")
            tasks[task_num - 1] = new_task
            print(f"Task {task_num} has been updated to '{new_task}'.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' has been removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\nTo-Do List Menu")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
