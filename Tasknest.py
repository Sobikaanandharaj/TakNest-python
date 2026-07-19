tasks = []
completed_tasks = []


def show_menu():
    print()
    print("=" * 45)
    print("   TaskNest - Organize Today, Own Tomorrow")
    print("=" * 45)
    print("1. Add Task")
    print("2. Show All Tasks")
    print("3. Complete a Task")
    print("4. Delete a Task")
    print("5. Exit")


def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def show_tasks():
    print("\n---------- Your TaskNest ----------")
    if not tasks:
        print("No tasks yet. Add one to get started!")
    else:
        for i, t in enumerate(tasks, start=1):
            print(f"{i}. {t}")


def complete_task():
    task = input("Which task did you complete? ").strip()
    if task in tasks:
        completed_tasks.append(task)
        tasks.remove(task)
        print("Task marked as completed!")
        print("\n---------- Completed Tasks ----------")
        for i, t in enumerate(completed_tasks, start=1):
            print(f"{i}. {t}")
    else:
        print("This task is not in your TaskNest.")


def delete_task():
    task = input("Which task do you want to delete? ").strip()
    if task in tasks:
        tasks.remove(task)
        print("Task deleted successfully!")
    else:
        print("This task is not in your TaskNest.")



while True:
    show_menu()
    choice = input("Enter your choice: ").strip()

    if not choice.isdigit():
        print("Invalid choice. Please enter a number.")
        continue

    choice = int(choice)

    if choice == 1:
        add_task()
    elif choice == 2:
        show_tasks()
    elif choice == 3:
        complete_task()
    elif choice == 4:
        delete_task()
    elif choice == 5:
        print("Thank you for using TaskNest. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")
