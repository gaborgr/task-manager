import os, time
from task_functions import (
    delete_single_task,
    clear_tasks,
    show_tasks,
    menu,
    new_task_to_add,
    mark_task,
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
