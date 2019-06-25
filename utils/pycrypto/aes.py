
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Variables
msg = input('Message: ')
key = 'password'

# Generating a Key
key = md5(key.encode('utf8')).digest()
print ('key: ', key)
# Initialization Vector
iv = get_random_bytes(AES.block_size)
print ('iv: ', iv)
# Create AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)
# Encrypting
crypted_msg = b64encode(iv + cipher.encrypt(pad(msg.encode('utf-8'), AES.block_size)))
print('Crypted message:', crypted_msg.decode('utf-8'))

# Get raw message
raw = b64decode(crypted_msg)
print ('raw: ', raw)
# Create AES cipher
cipher = AES.new(key, AES.MODE_CBC, raw[:AES.block_size])
# Decrypting
decrypted_msg = unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)
print('Decrypted message:', decrypted_msg.decode('utf-8'))
