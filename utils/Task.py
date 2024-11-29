class Task:
    id:int
    title:str
    description:str = None
    category:str = None
    due_date: str = None
    priority:str = "Низкий"
    status:str = "Не выполнена"

    def __init__(self, **task_data) -> None:
        """Инициализация объекта класса Task

        Args:
            task_data: Информация о задаче
        """

        for k, v in task_data.items():
            if k not in self.__annotations__.keys():
                raise AttributeError(f"Поле '{k}' не определено в {self.__class__.__name__}.")
        
        a = self.__annotations__.items()
        
        for field, expected_type in self.__annotations__.items():
            if field in task_data:
                value = task_data[field]
                if not isinstance(value, expected_type):
                    raise TypeError(
                        f"Поле '{field}' должно быть типа {expected_type.__name__}, "
                        f"но было передано {type(value).__name__}."
                    )
                setattr(self, field, value)
            else:
                if getattr(self, field) is not None:
                    setattr(self, field, self.__getattribute__(field))
                else:
                    raise ValueError(f"Обязательное поле '{field}' отсутствует в данных.")

    def __str__(self) -> str:
        return f"\t{self.id}\t|\t{self.title}\t|\t{self.description}\t|\t{self.category}\t|\t{self.due_date}\t|\t{self.priority}\t|\t{self.status}"
    


    