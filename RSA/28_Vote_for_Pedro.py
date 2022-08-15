from pwn import *
from json import loads, dumps

io = remote("socket.cryptohack.org", 13375)
io.recvline()
io.sendline(dumps({"option":"vote","vote":"a4c46bfb65e7eccc4e76a1ce2afc6f"}).encode())
print(loads(io.readline())["flag"])
