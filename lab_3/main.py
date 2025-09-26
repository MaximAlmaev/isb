import argparse
from hybrid_cryptosystem import Modes
from cryptography.exceptions import InvalidKey, UnsupportedAlgorithm
from tools import Tools

def main():

    """ Точка входа в приложение """
    try:
        settings_file = 'settings.json'
        Tools.is_file_exists(settings_file)
        settings = Tools.read_json(settings_file)
        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required = True)
        group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
        group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
        group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')

        args = parser.parse_args()
        if args.generation is not None:

            Modes.hybrid_sys_key_gen(settings["path_sym_key"], settings["path_private_key"], settings["path_public_key"])

        elif args.encryption is not None:
            
            Modes.data_encryption(settings["path_sym_key"], settings["path_private_key"], settings["path_text"], settings["path_ctext"], settings["path_iv"])

        else:
            Modes.data_decryption(settings["path_sym_key"], settings["path_private_key"], settings["path_ctext"], settings["path_dctext"], settings["path_iv"])
    except UnsupportedAlgorithm as e:
        print(f"Cryptographic algorithm not supported: {e}")
    except InvalidKey as e:
        print(f"Key serialization error: {e}")
    except PermissionError as e:
        print(f"PermissionError: {e}") 
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}") 
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyError as e:
        print(f"Missing setting: {e}")
    except Exception as e:
        print(f"Error: {e}")                

if __name__ == "__main__":
    main()