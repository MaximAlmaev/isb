from files_work import *


def encrypt(text: str, gamma: str, alphabeth: str) -> str:
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
    return result


def decrypt(encrypt_text: str, gamma: str, alphabeth: str) -> str:
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
    return result;


def main() -> None:
    settings = read_json_file('settings.json')
    text = read_txt_file(settings['original_text_path'])
    gamma = read_txt_file(settings['gamma_path'])
    alphabeth = read_txt_file(settings['alphabeth_path'])
    result = encrypt(text, gamma, alphabeth)
    write_txt_file(settings['encrypted_text_path'], result)
    encrypt_text = read_txt_file(settings['encrypted_text_path'])
    result2 = decrypt(encrypt_text, gamma, alphabeth)
    write_txt_file(settings['decrypted_text_path'], result2)



if __name__ == "__main__":
    main()
