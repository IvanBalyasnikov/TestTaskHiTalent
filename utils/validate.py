def validate_input(_type:callable, seq:str, answers:list) -> int|str:
    """Функция для валидации ввода
    Args:
        _type (callable): _description_
        seq (str): Входные данные
        answers (list): Возможные ответы

    Raises:
        ValueError: Ошибка, если не подходящий тип данных или нет внутри answers

    Returns:
        int|str: Результат, если ошибки нет
    """
    try:
        seq = _type(seq)
    except:
        raise TypeError(f"Не верный тип входных данных, нужно ввести {_type.__name__}")
    if seq not in answers:
        raise ValueError(f"Не верные выходные данные, нужно ввести значение из {answers}")
    return seq

def validate_datetime_input(seq:str) -> bool:
    my_seq = seq.split("-")
    if len(my_seq) != 3:
        return False
    if len(my_seq[0]) < 2:
        return False
    if len(my_seq[1]) < 2:
        return False
    if len(my_seq[2]) < 4:
        return False
    return True