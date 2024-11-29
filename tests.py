from utils.TaskManager import TaskManager

task_manager = TaskManager("tasks.json")


def test_insert():
    new_task =  task_manager.insert(
        **{
            "id": 1,
            "title": "Изучить основы FastAPI",
            "description": "Пройти документацию по FastAPI и создать простой проект",
            "category": "Работа",
            "due_date": "2024-11-30",
            "priority": "Высокий",
        }
    )
    task_manager.save()
    assert new_task == task_manager.tasks[-1]

def test_update():
    updated_task = task_manager.update("category", "Работа", lambda obj: obj.id == task_manager.tasks[-1].id)
    task_manager.save()
    assert updated_task == task_manager.tasks[-1]

def test_search():
    found = task_manager.search(*["fastapi", "простой"])
    assert found


def test_delete():
    deleted_task = task_manager.delete(lambda obj: obj.id == task_manager.tasks[-1].id)
    task_manager.save()
    assert deleted_task.__class__.__name__ == "Task"