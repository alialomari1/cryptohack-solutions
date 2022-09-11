from Crypto.Util.Padding import unpad
from json import loads, dumps
from Crypto.Cipher import AES
from hashlib import sha1
from pwn import remote

def decrypt_flag(shared_secret, iv, ciphertext):
    key = sha1(str(shared_secret).encode()).digest()[:16]
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    plaintext = AES.new(key, AES.MODE_CBC, iv).decrypt(ciphertext)
    return plaintext.decode()

# send random info to Bob and ignore answer
io = remote("socket.cryptohack.org", 13371)
io.readline()
io.sendline(dumps({"p":"0x123", "g":"0x123", "A":"0x123"}).encode())
io.readline()

# send B = 1, so then 
# shared secret = pow(B, a, p) = 1 for any a
io.sendline(dumps({"B":"0x01"}).encode())
io.readuntil(b"from Alice: ")
recv = loads(io.readline())
iv, ciphertext = recv["iv"], recv["encrypted_flag"]

shared_secret = 1
print(decrypt_flag(shared_secret, iv, ciphertext))
