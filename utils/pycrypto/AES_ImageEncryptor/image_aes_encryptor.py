
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from PIL import Image
import numpy as np

image_name = input("Input image name:")
key = input("Input key:")

# Load image
img = Image.open(image_name)
array = np.array(img)	# contains the pixel data in format (R G B A) -> array[0][149] is top right for example

bytes_img = array.tobytes()	# I think is not really necessary

# Create key and init vector
enc_key = md5(key.encode('utf8')).digest()
iv = get_random_bytes(AES.block_size) # AES.block_size = 16
cipher = AES.new(enc_key, AES.MODE_CBC, iv)

### Crypting
padded_img = pad(bytes_img, AES.block_size)
crypted_img = b64encode(iv + cipher.encrypt(padded_img))
# Save crypted image
# Save image
imgs = Image.frombytes('RGBA', (150, 150), b64decode(crypted_img))
imgs.save('crypted_' + image_name)

print (' --- Output information: ---	')
print (' - Encryption key:', key)
print (' - Initialization vector:', iv)
print (' - Output name: crypted_' + image_name)


