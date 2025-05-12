from files_work import *
alphabeth = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


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
    write_txt_file("encrypt_text.txt", result)


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
    write_txt_file("decrypt_file.txt", result)


def main() -> None:
    text = read_txt_file("original_text.txt")
    gamma = read_txt_file("gamma.txt")
    encrypt(text, gamma)
    encrypt_text = read_txt_file("encrypt_text.txt")
    decrypt(encrypt_text, gamma)


if __name__ == "__main__":
    main()
