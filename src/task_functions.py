from enum import Enum
from datetime import datetime


_current_id = 0


# create specific options for task priority
class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4


# generate a unique id number for each task
def generate_id() -> int:
    global _current_id  # preguntar si esto es necesario
    _current_id += 1
    return _current_id


def create_task(task: str, due_date: str) -> dict:
    return {
        "id": generate_id(),
        "task": task,
        # "priority": priority.value,
        "due_date": due_date,
        "completed": False,
    }


def validate_date(date: str, fmt: str = "%d-%m-%Y") -> bool:
    try:
        datetime.strptime(date, fmt)
        return True
    except ValueError:
        return False
