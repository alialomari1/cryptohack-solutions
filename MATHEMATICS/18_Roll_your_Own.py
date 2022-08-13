from pwn import remote
from json import loads, dumps

io = remote('socket.cryptohack.org', 13403)
io.readuntil(b'Prime generated: "')
q = int(io.readline()[:-2], 16)
io.sendline(dumps({"g":hex(q+1), "n":hex(q**2)}).encode())
io.readuntil(b'Generated my public key: "')
pub = int(io.readline()[:-2], 16)
io.sendline(dumps({"x":hex((pub-1)//q)}).encode())
io.readuntil(b'What is my private key: ')
print(loads(io.readline().decode())['flag'])
