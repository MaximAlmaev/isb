import os 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key
import tools
import json

class SerelizationKey:

    def deser_key_public(public_pem):
        with open(public_pem, 'rb') as pem_in:
            public_bytes = pem_in.read()
            d_public_key = load_pem_public_key(public_bytes)
        return d_public_key

    def deser_key_private(private_pem):
        with open(private_pem, 'rb') as pem_in:
            private_bytes = pem_in.read()
            d_private_key = load_pem_private_key(private_bytes,password=None,)
        return d_private_key

    def ser_public_key(public_key , public_pem):
        with open(public_pem, 'wb') as public_out:
                public_out.write(public_key.public_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo))
                
    def ser_private_key(private_key, private_pem):
        with open(private_pem, 'wb') as private_out:
                private_out.write(private_key.private_bytes(encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()))

class GenerationKey:

    def gen_key_sym(num_of_bit: int):
        settings = tools.read_json("settings.json")
        key = os.urandom(num_of_bit//8) # это байты
        tools.save_txt(settings["path_sym_key"], str(key))

    def gen_key_asym():
        keys = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
        )
        private_key = keys
        public_key = keys.public_key()
        return private_key, public_key

class Crypt:                
    def ass_crypt(public_key, path_sym_key):
        text = tools.read_txt(path_sym_key)
        c_text = public_key.encrypt(bytes(text, encoding="UTF-8"), padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        file_name = path_sym_key
        with open(file_name, 'wb') as key_file:
            key_file.write(c_text)

    def ass_decrtpt(private_key, path_sym_key):
        text = tools.read_txt(path_sym_key)
        dc_text = private_key.decrypt(bytes(text),padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),algorithm=hashes.SHA256(),label=None))
        print(dc_text.decode('UTF-8'))

class Modes:
    def hybrid_sys_key_gen(path_sym_key, path_private_key, path_public_key):
        with open('settings.json') as json_file:
            settings = json.load(json_file)
        GenerationKey.gen_key_sym(settings["num_of_bit"])
        private_key, public_key = GenerationKey.gen_key_asym()
        SerelizationKey.ser_private_key(private_key, path_private_key)
        SerelizationKey.ser_public_key(public_key, path_public_key)
        Crypt.ass_crypt(public_key, path_sym_key)

    def data_encryption(path_sym_key, path_public_key):
        Crypt.ass_decrtpt(path_public_key, path_sym_key)
        