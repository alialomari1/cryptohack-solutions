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
    return unpad(plaintext, 16).decode()

io = remote("socket.cryptohack.org", 13380)
io.readuntil(b"from Alice: ")
recv = loads(io.readline())
p = int(recv["p"], 16)
g = int(recv["g"], 16)
A = int(recv["A"], 16)

io.readuntil(b"from Bob: ")
recv = loads(io.readline())
B = int(recv["B"], 16)

io.readuntil(b"from Alice: ")
recv = loads(io.readline())
iv, ciphertext = recv["iv"], recv["encrypted"]

a = A * pow(g, -1, p)
shared_secret = (a * B) % p
print(decrypt_flag(shared_secret, iv, ciphertext))
