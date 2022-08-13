from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha1

shared_secret = 83201481069630956436480435779471169630605662777874697301601848920266492

key = sha1(str(shared_secret).encode('ascii')).digest()[:16]
iv = bytes.fromhex('64bc75c8b38017e1397c46f85d4e332b')
encrypted_flag = bytes.fromhex('13e4d200708b786d8f7c3bd2dc5de0201f0d7879192e6603d7c5d6b963e1df2943e3ff75f7fda9c30a92171bbbc5acbf')
cipher = AES.new(key, AES.MODE_CBC, iv)
print(unpad(cipher.decrypt(encrypted_flag), 16).decode())
