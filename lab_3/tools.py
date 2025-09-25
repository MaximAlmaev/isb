import json
from typing import Any, Dict


def read_txt(file_name: str) -> str:
    """Считывает текcт из .txt файла

    Args:
        file_name (str): Путь к файлу

    Returns:
        str: Содержимое файла
    """
    with open(file_name, 'r', encoding="utf-8") as f:
        text: str = f.read()
        return text
    
def save_txt(file_name: str, text: str):
    """Удаляет содержимое файла и сохраняет в нём новый текст.
    Если файла не существует, создаёт его.

    Args:
        file_name (str): Путь к файлу
        text (str): Текст, который необходимо сохранить
    """
    with open(file_name, 'w', encoding="utf-8") as f:
        f.write(text)
        
def read_json(file_name: str) -> Dict[str, Any]:
    """Считывает данные из .json файла

    Args:
        file_name (str): Путь к файлу

    Returns:
        Dict[str, Any]: Словарь объектов, содеражавшихся в .json файле
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        return(json.load(f))