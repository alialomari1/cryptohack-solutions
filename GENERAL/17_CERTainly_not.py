from Crypto.PublicKey import RSA
key = RSA.importKey(open('2048b-rsa-example-cert.der', 'rb').read())
print(key.n)
