from Crypto.PublicKey import RSA
key = RSA.importKey(open('bruce_rsa.pub').read())
print(key.n)
