
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

### Variables
#msg = input('Message: ')
msg = 'hello'
key = 'password'

### Generating a Key
# 1) Converts the string into bytes (utf8) to be acceptable by hash (md5) function
# 2) Create md5 object and use digest to get the key in byte format
key = md5(key.encode('utf8')).digest()
#print ('key:', key, 'Size:', len(key))

### Initialization Vector
# Get 16 bytes
iv = get_random_bytes(AES.block_size) # AES.block_size = 16
#print ('iv:', iv, 'Size:', len(iv))
# Create AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

### Encrypting
# Pad message into blocks of AES.block_size (16 bytes) size
# Pad(data, size) function joints/stores the data contained in 'data' in block of 'size' size
# Example -> pad ('hello', 8) -> |h e l l o \n \n \n| -> fills empty slots with '\n'
padded_msg = pad(msg.encode('utf-8'), AES.block_size)
# Encode crypted_msg into base 64 format
crypted_msg = b64encode(cipher.encrypt(padded_msg))
#print('Crypted message:', crypted_msg.decode('utf-8'))

### Get raw message
# Decode base64 to byte format
rec_msg = b64decode(crypted_msg)
#print ('raw:', raw)
# Create AES cipher
cipher = AES.new(key, AES.MODE_CBC, iv)

### Decrypting
decrypted_msg = unpad(cipher.decrypt(rec_msg), AES.block_size)
print('Decrypted message:', decrypted_msg.decode('utf-8'))



