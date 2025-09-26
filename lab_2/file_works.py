import json

def read_json(filename: str) -> list:
    """
    Считывает содержимое .json файла
    
    Args:
        filename: путь к JSON файлу
        
    Returns:
        list: содержимое файла в виде списка
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
             data = json.load(file)
             return data
    except FileNotFoundError:
        print(f"Файл не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def return_arr(seq):
    """
    Преобразует с строковую бинарную последовательность в бинарную последовательность float

    Args:
        seq: Строковая бинарная последовательность

    Returns:
        numeric_arr: последовательность единиц и нулей с типами float
    """
    numeric_arr = []
    for item in seq:
        try:
            numeric_arr.append(float(item))
        except ValueError:
            numeric_arr.append(0)  
    return numeric_arr
    