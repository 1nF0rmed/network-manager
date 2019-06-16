import base64
import hashlib

from Crypto import Random
from Crypto.Cipher import AES

class AESCipher:
    
    def __init__(self, key):
        self.block_size = AES.block_size    # The block size for the padding data
        self.key = hashlib.sha256(key.encode()).digest()    # Generate a hash for the key

    # Lambda help functions
    def _pad(self, s): 
        return s + (self.block_size - len(s)%self.block_size) * chr(self.block_size - len(s)%self.block_size)
    
    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]

    # Misc help functions
    def getKey(self):
        pass

    def setKey(self):
        pass

    def setBlockSize(self):
        pass


    # Main functions for AES

    def encrypt(self, raw):
        """
        1. Pad the text to the block size
        2. Generate IV for the given block size using Random
        3. Create a cipher using the IV and the Key in AES CBC Mode

        """
        padded_text = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        cipher_text = iv + cipher.encrypt(padded_text)

        # Return the cipher text with base64 encoding
        return base64.b64encode( cipher_text )

    def decrypt(self, r_data):
        """
        1. Decode the base64 encoded string
        2. Extract IV from decoded string
        3. Unpad the cipher text
        4. Return the raw text
        """
        enc_text = base64.b64decode(r_data)
        iv = enc_text[:self.block_size]
        
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        raw_text = cipher.decrypt(enc_text[self.block_size:])

        # Unpad and return the message in UTF-8 text
        return self._unpad(raw_text).decode("utf-8")

