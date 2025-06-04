import json, os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
JSON_PATH = os.path.join(DATA_DIR, "tasks.json")

# Validate Josn directory
os.makedirs(DATA_DIR, exist_ok=True)


def save_task(tasks: list):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def load_tasks():
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        tasks = json.load(f)
        for task in tasks:
            yield task
