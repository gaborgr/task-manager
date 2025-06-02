from file_operations import save_task, load_tasks
from task_functions import create_task, validate_date, add_task, delete_task
import os


tasks = [task for task in load_tasks()]


def menu():
    print("===== Task Manager =====")
    print("Options:")
    print("1. Show tasks. 🖨")
    print("2. Add new task. ➕")
    print("3. Delete task 🗑.")
    print("3. Mark task as a complet. ✔")
    print("4. Exit. 🚪")
    print("========================")
    print()
    option = int(input("Enter your choice: "))
    return option


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


menu()
clear_screen()
