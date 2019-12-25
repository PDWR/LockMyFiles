import json
from cryptography.hazmat.primitives.asymmetric import rsa  
from cryptography.hazmat.primitives import serialization 
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding  
from cryptography.hazmat.primitives import hashes  

class RSA_Class:

    @staticmethod
    def generate_pri():
        private_key = rsa.generate_private_key(  
                public_exponent=65537,  
                key_size=2048,  
                backend=default_backend()  
            )  
        return private_key

    @staticmethod
    def generate_pub(private_key):
        public_key = private_key.public_key()
        return public_key
      
    # Save the Private key in PEM format
    @staticmethod
    def save_pri(pri_path, private_key):
        with open(pri_path, "wb") as f:  
            f.write(private_key.private_bytes(  
                encoding=serialization.Encoding.PEM,  
                format=serialization.PrivateFormat.TraditionalOpenSSL,  
                encryption_algorithm=serialization.NoEncryption(),  
                )  
            )  
        
    # Save the Public key in PEM format
    @staticmethod
    def save_pub(pub_path, public_key):
        with open(pub_path, "wb") as f:  
            f.write(public_key.public_bytes(  
                encoding=serialization.Encoding.PEM,  
                format=serialization.PublicFormat.SubjectPublicKeyInfo,  
                )  
            )

    @staticmethod
    def load_pri(pri_path):
        private_key = serialization.load_pem_private_key(
            open(pri_path, 'rb').read(), password=None, backend=default_backend())
        return private_key

    @staticmethod
    def load_pub(pub_path):
        public_key = serialization.load_pem_public_key(
            open(pub_path, 'rb').read(), backend=default_backend())
        return public_key

    @staticmethod
    def encryption(public_key, plaintext):
        ciphertext = public_key.encrypt(  
            plaintext,  
            padding.OAEP(  
                mgf=padding.MGF1(algorithm=hashes.SHA256()),  
                algorithm=hashes.SHA256(),  
                label=None  
            )  
        )  
        return ciphertext

    @staticmethod
    def decryption(private_key, ciphertext):
        plaintext = private_key.decrypt(  
            ciphertext,  
            padding.OAEP(  
                mgf=padding.MGF1(algorithm=hashes.SHA256()),  
                algorithm=hashes.SHA256(),  
                label=None  
            )  
        ) 
        return plaintext

    @staticmethod
    def save(path, text):

        data = {"aes_ciphered_password": text}
        with open(path, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def load(path):
        with open(path, "r") as json_file:
            data = json.load(json_file)
        return data
            


    

    