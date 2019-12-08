
from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

from PIL import Image
import numpy as np

image_name = input("Input image name:")
#image_name = 'crypted_picture.png'
key = input("Input key:")
#key = 'andres'
#iv = input("Input initialization vector:")
iv = b'\xf1\x99M6\x0fP\xf8\xba\xb0\\\xde\xb9^\xb4\xb9\\'

# Load image
img = Image.open(image_name)
array = np.array(img)	# contains the pixel data in format (R G B A) -> array[0][149] is top right for example

bytes_img = array.tobytes()	# I think is not really necessary

# Create key and init vector
enc_key = md5(key.encode('utf8')).digest()
cipher = AES.new(enc_key, AES.MODE_CBC, iv)

### Decrypting
decrypted_img = cipher.decrypt(bytes_img)
#decrypted_img = list(decrypted_img) # This converts the bytes array into list (Human readable in RGBA)

# Save image
imgs = Image.frombytes('RGBA', (150, 150), decrypted_img)
imgs.save('decrypted_' + image_name)

print (' --- Output information: ---	')
print (' - Encryption key:', key)
print (' - Initialization vector:', iv)
print (' - Output name: decrypted_' + image_name)


