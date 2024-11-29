import json
import os
from utils.Task import Task
from utils.TaskSerializer import TaskSerializer

class TaskManager():

    def __init__(self, json_path:str = None, tasks:list[Task] = None) -> None:
        """Инициализация класса задач

        Args:
            json_path (str, optional): Путь к json файлу с задачами. По умолчанию None.
            tasks (list[Book], optional): Готовый лист book. По умолчанию None.
        """
        if json_path:
            self.json_path = json_path
            if not os.path.exists(os.path.abspath(self.json_path)):
                with open(self.json_path, "wt", encoding="utf-8") as f:
                    f.write("[]")
            self.tasks:list[Task] = [Task(**i) for i in self.json]
        elif tasks:
            self.tasks:list[Task] = tasks
        else:
            raise ValueError("Ошибка инициализации, нет исходных данных")
    

    @property
    def json(self) -> dict:
        """Возвращает все задачи в формате словаря 

        Returns:
            dict: массив со словарями задач
        """
        return json.load(open(os.path.abspath(self.json_path), "r", encoding="utf-8"))
    
    @property
    def ids(self) -> list[int]:
        """Возвращает лист со всеми id

        Returns:
            list[int]: лист со всеми id
        """
        return [i.id for i in self.tasks]
    
    @property
    def categories(self) -> list[int]:
        """Возвращает лист со всеми категориями

        Returns:
            list[int]: лист со всеми категориями
        """
        return list(set([i.category for i in self.tasks]))
    
    def last_id(self):
        return max([i.id for i in self.tasks]) or 1
    
    def save(self, save_path:str = None):
        """Сохраняет текущие задачи в переданный путь

        Args:
            save_path (str): путь к файлу
        """
        json.dump(
                self.tasks,
                open(os.path.abspath(self.json_path if not save_path else save_path), "wt", encoding="utf-8"),
                ensure_ascii=False,
                cls=TaskSerializer,
                indent=4
            )
        
    def select(self, *filter_by):
        def apply_filters(obj):
            return all(f(obj) for f in filter_by)

        return list(filter(apply_filters, self.tasks))

    
    def insert(self, **task_data) -> Task:
        """Добавляет задачу в базу

        Raises:
            AttributeError | ValueError: ошибка при создании

        Returns:
            Task: объект задачи
        """
        try:
            task_data.update({f"id": self.last_id() + 1})
            new_task = Task(**task_data)
            self.tasks.append(new_task)
            return new_task
        except Exception as e:
            raise e
    
    def delete(self, *filter_by):
        to_be_deleted = self.select(*filter_by)
        if to_be_deleted:
            return self.tasks.pop(self.tasks.index(to_be_deleted[0]))
        
    def update(self, attr_name:str, attr_value:str|int, *filter_by):
        to_be_updated = self.select(*filter_by)
        if to_be_updated:
            self.tasks[self.tasks.index(to_be_updated[0])].__setattr__(attr_name, attr_value)
            return self.tasks[self.tasks.index(to_be_updated[0])]
        
    def search(self, *keywords: str) -> list[Task]:
        result = []
        for task in self.tasks:
            task_data = task.__dict__  
            if any(
                any(keyword.lower() in str(value).lower() for keyword in keywords)
                for value in task_data.values()
            ):
                result.append(task)
        return TaskManager(tasks=result)

    def __str__(self) -> str:
        headers = [k for (k, v) in self.tasks[0].__annotations__.items()]

        data = [j.__dict__.values() for j in self.tasks]

        column_widths = [max(len(str(item)) for item in col) for col in zip(headers, *data)]

        def __format_row(row, widths):
            return " | ".join(str(item).ljust(width) for item, width in zip(row, widths))

        header_row = __format_row(headers, column_widths)

        separator = "-+-".join("-" * width for width in column_widths)

        data_rows = [__format_row(row, column_widths) for row in data]

        return f"{header_row}\n{separator}\n" + "\n".join(data_rows)


    
    

