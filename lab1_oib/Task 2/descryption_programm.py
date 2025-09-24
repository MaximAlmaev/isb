from files_work import *


def char_frequency(text: str) -> None:
    """
    Составляет частотный анализ текста
    :param text: текст, частотный анализ которого нужно составить
    :return: множество, где ключ - это символ, а значение его частота в данном тексте
    """
    quantity = {}
    for i in text:
        if i in quantity:
            quantity[i] += 1
        else:
            quantity[i] = 1
    if '\n' in quantity:
        del quantity['\n']
    for i in quantity:
        quantity[i] /= len(text)
    quantity = sorted(quantity.items(), key=lambda item: item[1], reverse=True)
    print(quantity)


def decrypt(key: dict, text: str) -> str:
    """
    Расшифровывает текст согласно переданному ключу.

    :param key: Словарь, где ключи — символы, подлежащие замене, а значения — новые символы.
    :param text: Исходная строка, которую нужно преобразовать.
    :return: Преобразованная строка.
    """
    new_text = text
    for original_char, replacement_char in key.items():
        new_text = new_text.replace(original_char, replacement_char)
    return new_text


def main() -> None:
    settings = read_json_file("settings.json")
    text = read_txt_file(settings["code_text"])
    char_frequency(text)
    key = read_json_file("decrypt_key.json")
    new_text = decrypt(key, text)
    write_txt_file(settings["new_text"], new_text)


if __name__ == "__main__":
    main()
