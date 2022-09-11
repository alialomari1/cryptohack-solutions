from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES
from hashlib import sha256

def decrypt_flag(shared_secret, iv, ciphertext):
    key = sha256(str(shared_secret).encode()).digest()[:128]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return unpad(plaintext, 16).decode()

e = 5959805911241109643914928800631944794321671043586961836890946136294554770507810148857251869110638484873235200204605081157845088692257708370810040562721345
iv = "334b1ceb2ce0d1bef2af9937cf82aad6"
ciphertext = "543e29415bdb1f694a705b2532a5beb7ebd7009591503ef3c4fbcebf9e62fe91307e5d98efcd49f9f3b1985956cafc89"
print(decrypt_flag(e, iv, ciphertext))
