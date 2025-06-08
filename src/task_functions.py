from datetime import datetime
from file_operations import save_task

_current_id = 0


# generate a unique id number for each task
def generate_id() -> int:
    global _current_id
    _current_id += 1
    return _current_id


def create_task(task: str, priority: int, due_date: str) -> dict:
    prior_list = ["LOW", "MEDIUM", "HIGH", "URGENT"]
    return {
        "id": generate_id(),
        "task": task,
        "priority": prior_list[priority],
        "due_date": due_date,
        "completed": False,
    }


def validate_date(date: str, fmt: str = "%d-%m-%Y") -> bool:
    try:
        datetime.strptime(date, fmt)
        return True
    except ValueError:
        return False


def add_task(task_list: list, new_task: dict) -> list:
    task_list.append(new_task)
    return task_list


def completed_task(task_id: int, task_list: list) -> list:
    new_list = []
    for task in task_list:
        if task["id"] == task_id:
            task["completed"] = True
            new_list.append(task)
        else:
            new_list.append(task)
    return new_list


def delete_task(task_list: list, task_id: int) -> list:
    return [task for task in task_list if task["id"] != task_id]


def clear_tasks():
    confirm = input("Delete ALL tasks? (y/n): ")
    if confirm.lower() == "y":
        save_task([])
        global _current_id
        _current_id = 0
        print("All tasks deleted!")
