from file_operations import save_task, load_tasks
from task_functions import (
    create_task,
    validate_date,
    add_task,
    delete_task,
    clear_tasks,
    completed_task,
)
import os, time


def menu():
    print("===== Task Manager =====")
    print("Options:")
    print("1. Show tasks. 🖨")
    print("2. Add new task. ➕")
    print("3. Delete task 🗑.")
    print("4. Mark task as a complet. ✔")
    print("5. Delete all tasks. ☢")
    print("6. Exit. 🚪")
    print("========================")
    print()

    return int(input("Enter your choice: "))


def new_task_to_add():
    tasks = [task for task in load_tasks()]
    task = input("Enter the task: ")
    print("How important it is?")
    print("1. LOW")
    print("2. MEDIUM")
    print("3. HIGH")
    print("4. URGENT")
    priority = int(input("Select an option: "))
    due_date = input("Enter de due-date (e.x. dd-mm-YYYY): ")
    new_task = create_task(task, priority, due_date)
    add_task(tasks, new_task)
    save_task(tasks)


def delete_single_task():
    tasks = [task for task in load_tasks()]
    taks_id = int(input("Enter the Task ID. you want delete: "))
    print()
    sure = input(f"Are you sure you want eliminate the Task ID. {taks_id}? (y/n): ")
    print()
    if sure.lower() == "y":
        return
    else:
        updated_list = delete_task(tasks, taks_id)
        save_task(updated_list)


def mark_task():
    taks_id = int(input("Enter the Task ID. you completed: "))
    tasks = [task for task in load_tasks()]
    new_list = completed_task(taks_id, tasks)
    save_task(new_list)


def show_tasks():
    tasks = [task for task in load_tasks()]
    size = len(tasks)
    if size == 0:
        print("Empty List!")
        return

    max_len_priority = max(len(task["priority"]) for task in tasks)
    for i in range(size):
        print(
            f"Task ID. {tasks[i]['id']} | Due Date: {tasks[i]['due_date']} | PRIORITY: {tasks[i]['priority']:<{max_len_priority}} | Task: {tasks[i]['task']}"
        )


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    clear_screen()
    print("Launching", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    while True:
        clear_screen()
        option = menu()
        clear_screen()
        if option == 1:
            show_tasks()
            print()
            input("Press any key to continue...")
        elif option == 2:
            clear_screen()
            new_task_to_add()
            print()
            print("Notification: Task added successfully! 👍")
            print()
            input("Press any key to continue...")
        elif option == 3:
            clear_screen()
            show_tasks()
            print()
            delete_single_task()
            print("Notification: Task deleted successfully! 🗑")
            print()
            input("Press any key to continue...")
        elif option == 4:
            clear_screen()
            show_tasks()
            print()
            mark_task()
            print("Notification: Task completed successfully! ✔")
            print()
            input("Press any key to continue...")
        elif option == 5:
            clear_screen()
            clear_tasks()
            clear_screen()
            print("Notification: ALL TASK REMOVED! ⚠")
            print()
            input("Press any key to continue...")
        elif option == 6:
            clear_screen()
            break


if __name__ == "__main__":
    main()
