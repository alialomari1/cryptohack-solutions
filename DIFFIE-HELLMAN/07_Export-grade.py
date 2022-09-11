from sympy.ntheory.residue_ntheory import discrete_log
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

io = remote("socket.cryptohack.org", 13379)
io.readline()
io.sendline(dumps({"supported": ["DH64"]}).encode())
io.readline()
io.sendline(dumps({"chosen": "DH64"}).encode())
io.readuntil(b"from Alice: ")
recv = loads(io.readline())

p = int(recv["p"], 16)
g = int(recv["g"], 16)
A = int(recv["A"], 16)
a = discrete_log(p, A, g) #since p is small

io.readuntil(b"from Bob: ")
recv = loads(io.readline())
B = int(recv["B"], 16)

io.readuntil(b"from Alice: ")
recv = loads(io.readline())
iv = recv["iv"]
ciphertext = recv["encrypted_flag"]

shared_secret = pow(B, a, p)
print(decrypt_flag(shared_secret, iv, ciphertext))
