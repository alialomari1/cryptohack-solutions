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
    return unpad(plaintext, 16).decode()

io = remote("socket.cryptohack.org", 13378)
io.readuntil(b"from Alice: ")
recv = loads(io.readline())
A = int(recv["A"], 16)
g = int(recv["g"], 16)
p = int(recv["p"], 16)

io.readuntil(b"from Alice: ")
recv = loads(io.readline())
iv = recv["iv"]
ciphertext = recv["encrypted"]

smooth_p = 0x72b20ce22e5616f923901a946b02b2ad0417882d9172d88c1940fec763b0cdf02ca5862cfa70e47fb8fd10615bf61187cd564a017355802212a526453e1fb9791014f070d77f8ff4dd54a6d1d58969293734e0b6bc22f3ceea788aa33be35eed4bdc1c8ceb94084399d98e13e69a2b9fa6c5583836a15798ba1a10edd81160a15662cdf587df6b816c570f9b11a466d1b4c328180f614e964f3a5ec61c3f2b759b21687a122f9faefc86fe69a3efd14829639596eb7f2de6eab6b444d06233d34d0651e6fed17db4d0025e58db7cad8824c3e93ed24df588a0a4530be2676e995f870172b9e765ec2886bce140000000000000000000000000000000000000000000000000000000000000000000000000000001
io.sendline(dumps({"g":hex(g),"A": hex(A),"p": hex(smooth_p)}).encode())
io.readuntil(b"Bob says to you: ")
B = int(loads(io.readline())["B"], 16)

b = discrete_log(smooth_p, B, 2)
shared_secret = pow(A, b, p)
print(decrypt_flag(shared_secret, iv, ciphertext))
