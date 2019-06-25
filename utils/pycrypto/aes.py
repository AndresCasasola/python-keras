
import random
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os
from hashlib import md5

# Generating a Key
#key = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
key = get_random_bytes(AES.block_size)
key = md5(key.encode('utf8')).digest()
print ('key', [x for x in key])
print ('Size', len(key) )

# Initialization Vector
#iv = ''.join([chr(random.randint(0, 0xFF)) for i in range(16)])
iv = get_random_bytes(AES.block_size)
print ('iv', [x for x in iv])
print ('Size', len(iv) )

# Create AES encrypter object
aes = AES.new(key, AES.MODE_CBC, iv)

# Encrypting with AES
data = 'Hello world 1234' # Must be 16 bytes
encrypted_data = aes.encrypt(data)

# Decrypting with AES
decrypted_data = aes.decrypt(encrypted_data)
print (decrypted_data.decode('utf-8'))
