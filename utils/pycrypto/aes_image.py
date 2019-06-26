
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from PIL import Image
import numpy as np

key = 'password'

# Load image
img = Image.open('picture.png')
array = np.array(img)	# contains the pixel data in format (R G B A) -> array[0][149] is top right for example
#print(array[0][149], 'Size:', len(array[0][0]))

enc_array = array.tobytes()
print(array[:30])

# Create key and init vector
key = md5(key.encode('utf8')).digest()
iv = get_random_bytes(AES.block_size) # AES.block_size = 16
cipher = AES.new(key, AES.MODE_CBC, iv)

### Crypting
padded_img = pad(enc_array, AES.block_size)
crypted_img = b64encode(iv + cipher.encrypt(padded_img))
# Save crypted image
# Save image
imgs = Image.frombytes('RGBA', (150, 150), b64decode(crypted_img))
imgs.save('crypted.png')

raw = b64decode(crypted_img)
iv = raw[:AES.block_size]
cipher = AES.new(key, AES.MODE_CBC, iv)

### Decrypting
decrypted_img = unpad(cipher.decrypt(raw[AES.block_size:]), AES.block_size)

#decrypted_img = list(decrypted_img) # This converts the bytes array into list (Human readable in RGBA)

# Save image
imgs = Image.frombytes('RGBA', (150, 150), decrypted_img)
imgs.save('output.png')

