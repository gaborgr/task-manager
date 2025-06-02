# Estructura de almacenamiento de Tareas

# Una Tarea sera una diccionario:
task_1 = {
    "id": 1,
    "task": "estudiar",
    "prioridad": "ALTA",
    "date": "01-04-2025",
    "terminated": False,
}

task_2 = {}
task_3 = {}

# Las tareas se almacenaran en una lista
varias_task = [task_1, task_2, task_3]

# - id (int)
# - task (string)
# - prioridad (Enum librery)
# - date (string dd-mm-yyy)
# - terminated (true or false)
