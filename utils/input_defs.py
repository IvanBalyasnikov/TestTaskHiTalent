from utils.validate import *

def get_category_input(categories:list):
    for i, c in enumerate(categories):
        print(f"{i+1}. {c}")
    while True:
        choise = input()
        try:
            return categories[validate_input(int, choise, [i+1 for i in range(len(categories))]) - 1]
        except ValueError as e:
            if choise == -1:
                return
            print(e)
            continue


def get_id_input(ids:list[int]) -> int | None:
    """Проверяет введённый id

    Args:
        ids (list[int]): Доступные id

    Returns:
        int | None: Id, если он существует
    """
    while True:
        choise = input()
        try:
            return validate_input(int, choise, ids)
        except ValueError as e:
            if choise == -1:
                return
            print(e)
            continue

def get_data_for_update(ids:list[int]) -> dict | None:
    data = None
    print("Введите id задачи, которую хотите изменить, введите -1, если хотите отменить изменение задачи: ", end="")
    choise = get_id_input(ids)
    if not choise:
        return
    print("Выберите поле, которое хотите изменить.")
    print("1. Название")
    print("2. Описание")
    print("3. Категория")
    print("4. Срок выполнения")
    print("5. Приоритет")
    print("0. Выйти")
    choise = None
    while True:
        try:
            choise = validate_input(int, input(), [0, 1, 2, 3, 4, 5])
            break
        except ValueError as e:
            print(e)
            continue
    match choise:
        case 0:
            return
        case 1:
            print("Введите название задачи, если хотите отменить изменение введите -1: ", end="")
            title = input()
            try:
                validate_input(int, title, [-1])
                return
            except:
                return {"id": choise, 'title': title}
        case 2:
            print("Введите описание задачи, если хотите отменить изменение введите -1: ", end="")
            description = input()
            try:
                validate_input(int, description, [-1])
                return
            except:
                return {"id": choise, 'description': description}
        case 3:
            print("Введите категорию задачи, если хотите отменить изменение введите -1: ", end="")
            while not data:
                category = input()
                try:
                    validate_input(int, category, [-1])
                    return
                except:
                    pass
                try:
                    validate_input(str, category, ["Работа", "Учеба", "Личное"])
                except Exception as e:
                    print(e)
                    data = None  
                return {"id": choise, 'category': category}
        case 4:
            print("Введите срок выполнения задачи, если хотите отменить изменение введите -1: ", end="")
            while not data:
                due_date = input()
                try:
                    validate_input(int, due_date, [-1])
                    return
                except:
                    pass
                if not validate_datetime_input(due_date):
                    print("Не верный формат данных. Введите дату в формате \"дд-мм-ГГГГ\", без ковычек.")
                    due_date = None
                    continue
                return {"id": choise, 'due_date': due_date}
        case 5:
            print("Введите приоритет задачи, если хотите отменить изменение введите -1: ", end="")
            while not data:
                priority = input()
                try:
                    validate_input(int, priority, [-1])
                    return
                except:
                    pass
                try:
                    validate_input(str, priority, ["Низкий", "Средний", "Высокий"])
                except Exception as e:
                    print(e)
                    priority = None
                    continue
                return {"id": choise, 'priority': priority}


def get_data_for_insert() -> dict | None:
    title = None
    description = None
    category = None
    due_date = None
    priority = None
    while True:
        while not title:
            print("Введите название задачи, если хотите отменить создание введите -1: ", end="")
            title = input()
            try:
                validate_input(int, title, [-1])
                return
            except:
                pass
        if not title:
            continue
        while not description:
            print("Введите описание задачи, если хотите отменить создание введите -1: ", end="")
            description = input()
            try:
                validate_input(int, description, [-1])
                return
            except:
                pass
        if not description:
            continue
        while not category:
            print("Введите категорию задачи, если хотите отменить создание введите -1: ", end="")
            category = input()
            try:
                validate_input(int, category, [-1])
                return
            except:
                pass
            try:
                validate_input(str, category, ["Работа", "Учеба", "Личное"])
            except Exception as e:
                print(e)
                category = None
                break
        if not category:
            continue
        while not due_date:
            print("Введите срок выполнения задачи, если хотите отменить создание введите -1: ", end="")
            due_date = input()
            try:
                validate_input(int, due_date, [-1])
                return
            except:
                pass
            if not validate_datetime_input(due_date):
                print("Не верный формат данных. Введите дату в формате \"дд-мм-ГГГГ\", без ковычек.")
                due_date = None
                break
        if not due_date:
            continue
        while not priority:
            print("Введите приоритет задачи, если хотите отменить создание введите -1: ", end="")
            priority = input()
            try:
                validate_input(int, priority, [-1])
                return
            except:
                pass
            try:
                validate_input(str, priority, ["Низкий", "Средний", "Высокий"])
            except Exception as e:
                print(e)
                priority = None
                break
        if priority:
            break
        
    return {
        "title": title, 
        "description": description,
        "category": category,
        "due_date": due_date,
        "priority": priority
    }