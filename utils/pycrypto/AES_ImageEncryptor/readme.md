

## Commands in order to execute ImageEncryptor

### Install Python3, pip3 and needed (not default) packages
sudo apt install python3
sudo apt install python3-pip
pip3 install pycryptodome
pip3 install Pillow
pip3 install numpy

### Run Encryptor
python3 image_aes_encryptor.py
Input image name: *picture.png* (and ENTER)
Input key: *Your key* (and ENTER)

crypted_picture.png will be generated.

### Run Decryptor
python3 image_aes_decryptor.py
Input image name: *crypted_picture.png* (and ENTER)
Input key: *Your key* (and ENTER)

decrypted_crypted_picture.png will be generated.
