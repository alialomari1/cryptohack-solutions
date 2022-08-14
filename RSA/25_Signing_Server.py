from pwn import *
from json import dumps, loads

io = remote("socket.cryptohack.org", 13374)
io.recvline()
io.sendline(dumps({"option": "get_secret"}).encode())
io.sendline(dumps({"option": "sign", "msg": loads(io.recvline())["secret"] }).encode()) 
print(bytes.fromhex(loads(io.recvline())["signature"][2:]).decode()) 
