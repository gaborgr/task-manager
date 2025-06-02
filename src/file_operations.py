import json, os
from task_functions import create_task


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_DIR = os.path.join(PROJECT_ROOT, "data")
JSON_PATH = os.path.join(DATA_DIR, "tasks.json")

# Validate Josn directory
os.makedirs(DATA_DIR, exist_ok=True)


tasks = []

tasks.append(create_task("listo para comer", "31-12-2025"))
tasks.append(create_task("estudiar progrmaando", "31-12-2025"))


def save_task(task):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


save_task(tasks[0])
