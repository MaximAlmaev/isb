from files_work import *
alphabeth = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def write_txt_files(filename: str, text: str) -> None:
    """
    Записывает данные в txt файл
    :param filename: название файла в формате txt
    :param text: данные для записи в файл
    """
    try:
        with open(filename, "w") as file:
            file.write(text)
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def read_txt_files(filename: str) -> str:
    """
    Считывает данные из txt файла
    :param filename: название файла в формате txt
    :return: считанные данные из файла
    """
    try:
        with open(filename, "r") as file:
            return file.read()
    except FileNotFoundError as exc:
        print("File not found, ", exc)
    except PermissionError as exc:
        print("File access denied, ", exc)
    except Exception as exc:
        print("Error reading from file, ", exc)


def encrypt(text: str, gamma: str) -> None:
    """
    Шифрует текст с помощью метода гамма-шифрования
    :param text: текст, которы требуется
    :param gamma: ключ шифрования
    """

    text_len = len(text)
    gamma_len = len(gamma)
    key_text = (gamma * (text_len // gamma_len)) + gamma[:text_len % gamma_len]
    code = []
    for i in range(text_len):
        text_index = alphabeth.find(text[i])
        gamma_index = alphabeth.find(key_text[i])

        if text_index == -1:
            code.append(text[i])
        else:
            code.append(alphabeth[(text_index + gamma_index) % len(alphabeth)])

    result = ''.join(code)
    write_txt_files("encrypt_text.txt", result)


def decrypt(encrypt_text: str, gamma: str) -> None:
    text_len = len(encrypt_text)
    gamma_len = len(gamma)

    key_text = (gamma * (text_len // gamma_len)) + gamma[:text_len % gamma_len]

    code = []
    for i in range(text_len):
        text_index = alphabeth.find(encrypt_text[i])
        gamma_index = alphabeth.find(key_text[i])

        if text_index == -1:
            code.append(encrypt_text[i])
        else:

            code.append(alphabeth[(text_index - gamma_index) % len(alphabeth)])
    result = ''.join(code)
    write_txt_files("decrypt_file.txt", result)


def main() -> None:
    text = read_txt_files("original_text.txt")
    gamma = read_txt_file("gamma.txt")
    encrypt(text, gamma)
    encrypt_text = read_txt_files("encrypt_text.txt")
    decrypt(encrypt_text, gamma)


if __name__ == "__main__":
    main()
