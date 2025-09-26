import os 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import padding as pd
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric.rsa import (RSAPublicKey, RSAPrivateKey)
from tools import Tools
import json

class SerelizationKey:
    """Класс для сериализации и десериализации ключей"""

    def deser_key_public(public_pem: str) -> RSAPublicKey:
        """
        Десериализация публичного ключа из PEM файла
        
        Args:
            public_pem (str): Путь к файлу с публичным ключом
            
        Returns:
            RSAPublicKey: Десериализованный публичный ключ
        """
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
        return d_public_key

    def deser_key_private(private_pem: str) -> RSAPrivateKey:
        """
        Десериализация приватного ключа из PEM файла
        
        Args:
            private_pem (str): Путь к файлу с приватным ключом
            
        Returns:
            RSAPrivateKey: Десериализованный приватный ключ
        """
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key

    def ser_public_key(public_key: RSAPublicKey, public_pem: str):
        """
        Сериализация публичного ключа в PEM файл
        
        Args:
            public_key (RSAPublicKey): Публичный ключ для сериализации
            public_pem (str): Путь для сохранения публичного ключа
        """
        with open(public_pem, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
                
    def ser_private_key(private_key: RSAPrivateKey, private_pem: str):
        """
        Сериализация приватного ключа в PEM файл
        
        Args:
            private_key (RSAPrivateKey): Приватный ключ для сериализации
            private_pem (str): Путь для сохранения приватного ключа
        """
        with open(private_pem, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))

class GenerationKey:
    """Класс для генерации симметричных и асимметричных ключей"""

    def gen_key_sym(num_of_bit: int):
        """
        Генерация симметричного ключа заданной длины
        
        Args:
            num_of_bit (int): Длина ключа в битах (128, 192, 256)
        """
        settings = Tools.read_json("settings.json")
        key = os.urandom(num_of_bit//8)
        Tools.save_txt_binary(settings["path_sym_key"], key)

    def gen_key_asym() -> tuple[RSAPublicKey, RSAPrivateKey]:
        """
        Генерация пары асимметричных ключей (приватный и публичный)
        
        Returns:
            tuple: (private_key, public_key) - пара RSA ключей
        """
        keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key

class Crypt:
    """Класс для выполнения криптографических операций"""

    def ass_crypt(public_key: RSAPublicKey, path_sym_key: str):
        """
        Асимметричное шифрование симметричного ключа
        
        Args:
            public_key (RSAPublicKey): Публичный ключ для шифрования
            path_sym_key (str): Путь к файлу с симметричным ключом
        """
        text = Tools.read_txt_binary(path_sym_key)
        c_text = public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        file_name = path_sym_key
        with open(file_name, 'wb') as key_file:
            key_file.write(c_text)

    def ass_decrtpt(private_key_path, path_sym_key):
        text = Tools.read_txt_binary(path_sym_key)
        private_key = SerelizationKey.deser_key_private(private_key_path)
        dc_text = private_key.decrypt(bytes(text),padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        return dc_text

    def encrypt_camellia_text(text_path: str, key: bytes, ctext_path: str, iv_path: str):
        """
        Шифрование текста алгоритмом Camellia в режиме CBC
        
        Args:
            text_path (str): Путь до исходного текстового файла
            key (bytes): Симметричный ключ для шифрования
            ctext_path (str): Путь для сохранения зашифрованного текста
            iv_path (str): Путь для сохранения вектора инициализации (IV)

        """

        text = Tools.read_txt(text_path)
        padder = pd.ANSIX923(128).padder()
        text_bytes = text.encode('UTF-8') if isinstance(text, str) else text
        padded_text = padder.update(text_bytes) + padder.finalize()
        iv = os.urandom(16)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(padded_text) + encryptor.finalize()
        Tools.save_txt_binary(ctext_path, cipher_text)
        Tools.save_txt_binary(iv_path, iv)
    
    def decrypt_camellia_text(cipher_text_path: str, key: bytes, iv_path: str, dcipher_text_path: str):
        """
        Дешифрование текста алгоритмом Camellia
        
        Args:
            cipher_text_path (str): Путь к файлу с зашифрованным текстом
            key (bytes): Симметричный ключ для дешифрования
            iv_path (str): Путь к файлу с вектором инициализации
            dcipher_text_path (str): Путь для сохранения расшифрованного текста

        """
        iv = Tools.read_txt_binary(iv_path)
        cipher_text = Tools.read_txt_binary(cipher_text_path)
        cipher = Cipher(algorithms.Camellia(key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        padded_text = decryptor.update(cipher_text) + decryptor.finalize()

        unpadder = pd.ANSIX923(128).unpadder()
        original_text = unpadder.update(padded_text) + unpadder.finalize()
        original_text = original_text.decode('UTF-8')
        Tools.save_txt(dcipher_text_path, original_text)

class Modes:
    
    """Класс для работы с режимами гибридной криптосистемы"""

    def hybrid_sys_key_gen(path_sym_key: str, path_private_key: str, path_public_key: str):
        """
        Генерация ключей для гибридной криптосистемы
        
        Args:
            path_sym_key (str): Путь для сохранения симметричного ключа
            path_private_key (str): Путь для сохранения приватного ключа
            path_public_key (str): Путь для сохранения публичного ключа
        """
        with open('settings.json') as json_file:
            settings = json.load(json_file)
        key_length = settings["num_of_bit"]
        if not key_length in [128, 192, 256]:
            raise ValueError(f"Неверная длина ключа, может быть 128, 192, 256, получено {key_length}")
        GenerationKey.gen_key_sym(key_length)
        private_key, public_key = GenerationKey.gen_key_asym()
        SerelizationKey.ser_private_key(private_key, path_private_key)
        SerelizationKey.ser_public_key(public_key, path_public_key)
        Crypt.ass_crypt(public_key, path_sym_key)

    def data_encryption(path_sym_key: str, path_private_key: str, text_path: str, ctext_path: str, iv_path: str):
        """
        Шифрование данных с использованием гибридной системы
        
        Args:
            path_sym_key (str): Путь к зашифрованному симметричному ключу
            path_private_key (str): Путь к приватному ключу для дешифрования симметричного ключа
            text_path (str): Путь к исходному текстовому файлу
            ctext_path (str): Путь для сохранения зашифрованного текста
            iv_path (str): Путь для сохранения вектора инициализации
        """
        key = Crypt.ass_decrtpt(path_private_key, path_sym_key)
        Crypt.encrypt_camellia_text(text_path, key ,ctext_path, iv_path)

    def data_decryption(path_sym_key: str, path_private_key: str, ctext_path: str, dctext_path: str, iv_path: str):
        """
        Дешифрование данных с использованием гибридной системы
        
        Args:
            path_sym_key (str): Путь к зашифрованному симметричному ключу
            path_private_key (str): Путь к приватному ключу для дешифрования симметричного ключа
            ctext_path (str): Путь к зашифрованному тексту
            dctext_path (str): Путь для сохранения расшифрованного текста
            iv_path (str): Путь к файлу с вектором инициализации
        """
        key = Crypt.ass_decrtpt(path_private_key, path_sym_key)
        Crypt.decrypt_camellia_text(ctext_path, key, iv_path, dctext_path)
    

        