def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def remove_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}\n")
        else:
            print("Invalid number.\n")
    except ValueError:
        print("Please enter a number.\n")

def main():
    tasks = load_tasks()
    while True:
        print("Choose: view / add / remove / exit")
        choice = input(">> ").lower()

        if choice == "view":
            view_tasks(tasks)
        elif choice == "add":
            add_task(tasks)
        elif choice == "remove":
            remove_task(tasks)
        elif choice == "exit":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()