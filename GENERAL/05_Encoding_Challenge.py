from pwn import remote
from json import loads, dumps
from base64 import b64decode
from codecs import encode

io = remote('socket.cryptohack.org', 13377)
while True:
    enc = loads(io.recvline().decode())
    print(enc)
    if 'flag' in enc: 
        break
    io.sendline(dumps({"decoded": {
        'base64': lambda e: b64decode(e).decode(),
        'hex'   : lambda e: bytes.fromhex(e).decode(),
        'rot13' : lambda e: encode(e, 'rot_13'),
        'bigint': lambda e: bytes.fromhex(e[2:]).decode(),
        'utf-8' : lambda e: ''.join([chr(c) for c in e])
    }[enc['type']](enc['encoded'])}).encode())
