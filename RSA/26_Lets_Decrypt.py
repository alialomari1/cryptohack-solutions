from pwn import *
from json import dumps, loads
from pkcs1 import emsa_pkcs1_v15

msg = "I am Mallory.*own CryptoHack.org"
sig = 0x55c231eebc642cd1e44199e10937ee8b9e93c0c2d10a18b7b53a207fb1ddd4e6c2e08368a1943187bb1efe0378567340a0851710c426f609aa79d3b5bb3f8efe7f531cfdb54a9fba9e77e3ca2adcecdc299ebf601bd8926dd6ed4e7e71f96ef61cc041159eb0584ff4ce9f0d9e5cb49a91ba15226740f378340e40805aff2e20e275b783aa43a0ac670ec1af2d4e834acceda189add6ed7daf64ed8f9f9718f030c8a7d64afee7cf33beef5f790611eaef40e7c978e2355f3039a6df4f38113ce83ed669a733ce6a93e1fb04fdd6c28815beb6b62f886a47150fbdd34668aa7ff55787874a7b6787a5942da4d73b3197eb792b39d0e338f48fc5f4c01a16a178
m = int(bytes.hex(emsa_pkcs1_v15.encode(msg.encode(), 256)), 16)

io = remote("socket.cryptohack.org", 13391)
io.recvline()
io.sendline(dumps({"option": "verify","msg": msg,"N": hex(sig-m),"e": "0x01"}).encode())
print(loads(io.recvline())["msg"])
