import json
from typing import Any, Dict
import os
from pathlib import Path


class Tools:
    @staticmethod
    def read_txt_binary(file_name: str) -> bytes:
        """Считывает текcт из .txt файла

        Args:
            file_name (str): Путь к файлу

        Returns:
            str: Содержимое файла
        """
        with open(file_name, 'rb') as f:
            text: str = f.read()
            return text
    
    @staticmethod
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
        
    @staticmethod
    def save_txt(file_name: str, text: str):
        """Удаляет содержимое файла и сохраняет в нём новый текст.
        Если файла не существует, создаёт его.

        Args:
            file_name (str): Путь к файлу
            text (str): Текст, который необходимо сохранить
        """
        with open(file_name, 'w', encoding="utf-8") as f:
            f.write(text)
    
    @staticmethod
    def save_txt_binary(file_name: str, text: bytes):
        """Удаляет содержимое файла и сохраняет в нём новый текст.
        Если файла не существует, создаёт его.

        Args:
            file_name (str): Путь к файлу
            text (str): Текст, который необходимо сохранить
        """
        with open(file_name, 'wb') as f:
            f.write(text)

    @staticmethod       
    def read_json(file_name: str) -> Dict[str, Any]:
        """Считывает данные из .json файла

        Args:
            file_name (str): Путь к файлу

        Returns:
            Dict[str, Any]: Словарь объектов, содеражавшихся в .json файле
        """
        with open(file_name, 'r', encoding='utf-8') as f:
            return(json.load(f))
        
    @staticmethod
    def is_file_exists(file_path: str):
        """Проверяет, существует ли файл
        Args:
            file_path (str): Путь к файлу
        Raises:
            FileNotFoundError: Если файл не существует
            ValueError: Не является файлом
            PermissionError: Нету доступа к файлу
        """
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл не найден: {file_path}")
        if not path.is_file():
            raise ValueError(f"Не является файлом: {file_path}")
        if not os.access(file_path, os.R_OK):
            raise PermissionError(f"Нету доступа к файлу: {file_path}")