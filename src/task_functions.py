from datetime import datetime
from file_operations import save_task, load_tasks
from colorama import Fore, Style


# ===================== GENERATE ID NUMBER =====================
def generate_id() -> int:
    tasks = [task for task in load_tasks()]
    if len(tasks) >= 1:
        current_id = tasks[-1]["id"] + 1
        return current_id
    else:
        return 1


# ===================== CREATE TASKS STRUCTURE =====================
def validate_date(date: str, fmt: str = "%d-%m-%Y") -> bool:
    try:
        datetime.strptime(date, fmt)
        return True
    except ValueError:
        return False


def create_task(task: str, priority: int, due_date: str) -> dict:
    prior_list = ["LOW", "MEDIUM", "HIGH", "URGENT"]
    return {
        "id": generate_id(),
        "task": task,
        "priority": prior_list[priority - 1],
        "due_date": due_date,
        "completed": False,
    }


# ===================== ADD NEW TASK =====================
def add_task(task_list: list, new_task: dict) -> list:
    task_list.append(new_task)
    return task_list


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


# ===================== COMPLETE TASKS =====================
def completed_task(task_id: int, task_list: list) -> list:
    new_list = []
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            new_list.append(task)
        else:
            new_list.append(task)
    return new_list


def mark_task():
    taks_id = int(input("Enter the Task ID. you completed: "))
    tasks = [task for task in load_tasks()]
    new_list = completed_task(taks_id, tasks)
    save_task(new_list)


# ===================== DELETE SILGLE TASK =====================
def delete_single_task():
    tasks = [task for task in load_tasks()]
    task_id = int(input("Enter the Task ID. you want delete: "))
    print()
    sure = input(f"Are you sure you want eliminate the Task ID. {task_id}? (y/n): ")
    print()

    if sure.lower() == "y":
        update_list = [task for task in tasks if task["id"] != task_id]
        save_task(update_list)
        return
    else:
        print("Notification: process abort!")


# ===================== DELETE ALL TASKS =====================
def clear_tasks():
    confirm = input("Delete ALL tasks? (y/n): ")
    if confirm.lower() == "y":
        save_task([])
        print("All tasks deleted!")


# ===================== SHOW ALL TASKS =====================
def show_tasks():
    tasks = [task for task in load_tasks()]
    size = len(tasks)
    if size == 0:
        print("Empty List!")
        return

    max_len_priority = max(len(task["priority"]) for task in tasks)
    for task in tasks:
        color = Fore.GREEN if task["completed"] else Fore.RED
        status = "✅" if task["completed"] else "⏳"
        print(
            f"Task ID. {task['id']} | "
            f"Due Date: {task['due_date']} | "
            f"PRIORITY: {task['priority']:<{max_len_priority}} | "
            f"Task: {color}{task['task']} {status}{Style.RESET_ALL}"
        )


# ===================== SHOW MENU =====================
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
