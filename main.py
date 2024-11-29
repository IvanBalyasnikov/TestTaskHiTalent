from utils.TaskManager import TaskManager
from utils.input_defs import *
        


def main():
    task_manager = TaskManager("tasks.json")
    print("Добро пожаловать в Менеджер задач!")
    print("Чтобы вы хотели сделать?")
    while True:
        print("1. Посмотреть задачи")
        print("2. Добавить задачу")
        print("3. Изменить задачу")
        print("4. Отметить задачу выполненной")
        print("5. Удалить задачу")
        print("6. Поиск задачи")
        print("7. Посмотреть задачи по категориям")
        print("0. Выйти")
        try:
            choise = validate_input(int, input(), [0, 1, 2, 3, 4, 5, 6, 7])
        except ValueError as e:
            print(e)
            continue
        match choise:
            case 1:
                print("Вот ваши задачи:")
                print(task_manager)
                print("\n")
            case 2:
                task_data = get_data_for_insert()
                if not task_data:
                    continue
                new_task = task_manager.insert(**task_data)
                task_manager.save()
                print("Новая задача добавлена!")
                print(new_task)
            case 3:
                update_data = get_data_for_update(task_manager.ids)
                if not update_data:
                    continue
                updated_task = task_manager.update(list(update_data.keys())[1], list(update_data.values())[1], lambda obj: obj.id == update_data['id'])
                task_manager.save()
                print("Задача изменена!")
                print(updated_task)
            case 4:
                print("Введите id задачи, в которой хотите изменить статус, введите -1, если хотите отменить изменение задачи: ", end="")
                choise = get_id_input(task_manager.ids)
                if not choise:
                    continue
                old_status = task_manager.select(lambda obj: obj.id == choise)[0].status
                updated_task = task_manager.update("status", "Выполнена" if old_status == "Не выполнена" else "Не выполнена", lambda obj: obj.id == choise)
                task_manager.save()
                print("Статус задачи изменён!")
                print(updated_task)
            case 5:
                print("Введите id задачи, которую хотите удалить, введите -1, если хотите отменить изменение задачи: ", end="")
                choise = get_id_input([-1, *task_manager.ids])
                if choise == -1:
                    continue
                deleted_task = task_manager.delete(lambda obj: obj.id == choise)
                task_manager.save()
                print("Задача удалена! Если вы хотите её восстановить, введите -1, в противном случае нажмите ENTER")
                try:
                    choise = validate_input(int, input(), [-1])
                    task_manager.insert(**deleted_task.__dict__)
                    print("Задача восстановлена!")
                except:
                    pass
            case 6:
                print("Введите ключевые слова для поиска через запятую.")
                keywords = [i.strip() for i in input().split(",")]
                found = task_manager.search(*keywords)
                print("Вот, что мне удалось найти:")
                print(found)
            case 7:
                print("Введите номер категории.")
                choise = get_category_input(task_manager.categories)
                if not choise:
                    continue
                found_task = task_manager.select(lambda obj: obj.category == choise)
                print("Вот, что мне удалось найти:")
                print(TaskManager(tasks= found_task))
            case 0:
                return

if __name__ == "__main__":
    main()    
