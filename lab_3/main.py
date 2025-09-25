import json
import argparse
from hybrid_cryptosystem import Modes

def main():
    with open('settings.json') as json_file:
        settings = json.load(json_file)
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument('-gen','--generation',help='Запускает режим генерации ключей')
    group.add_argument('-enc','--encryption',help='Запускает режим шифрования')
    group.add_argument('-dec','--decryption',help='Запускает режим дешифрования')

    args = parser.parse_args()
    if args.generation is not None:

        Modes.hybrid_sys_key_gen(settings["path_sym_key"], settings["path_private_key"], settings["path_public_key"])

    elif args.encryption is not None:
        
        Modes.data_encryption(settings["path_sym_key"], settings["path_public_key"])

    else:
        
        Modes.hybrid_sys_key_gen(settings["path_sym_key"], settings["path_private_key"], settings["path_public_key"])
                 

if __name__ == "__main__":
    main()