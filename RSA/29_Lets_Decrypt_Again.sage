from pkcs1 import emsa_pkcs1_v15
from json import loads, dumps
from pwn import remote, xor

def solve(msg, idx):
    digest = int(bytes.hex(emsa_pkcs1_v15.encode((msg+suffix).encode(), 768 // 8)), 16)
    e = discrete_log(Mod(digest, n), Mod(s, n))
    io.sendline(dumps({'option':'claim', 'msg': msg + suffix, 'e':hex(e), 'index':int(idx)}).encode())
    return (loads(io.recvline()))['secret']

s = 0x910f5f4fd7f0f5408711f577ac68bd24ede89d948681298a29d3d2094d13dbc24872bcaa37ccce91c35366ee2f3dd5324f68d33be48a7f0f10beb280f326fbabe2cc7c2fd343c57212f9aae481192144592338ecd2de2351289c383c1490f0d2
n = 1000120007020266767402749898742219793970297020432528956049530793865219680313442335799796740977248798869240976808292142421700982073722069461150446330334899583118911948842763629030864693933380584918689773987802449535745833592107844509736928801

io = remote('socket.cryptohack.org', 13394)
io.recvline()
io.sendline(dumps({'option': 'set_pubkey', 'pubkey': hex(n)}).encode())
suffix = loads(io.recvline())['suffix']

s1 = bytes.fromhex(solve('This is a test for a fake signature.', 0))
s2 = bytes.fromhex(solve('My name is kenny and I own CryptoHack.org', 1))
s3 = bytes.fromhex(solve('Please send all my money to 1BoatSLRHtKNngkdXEeobR76b53LETtpyT', 2))
print(xor(xor(s1, s2), s3).decode())
