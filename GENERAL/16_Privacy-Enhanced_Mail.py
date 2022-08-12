from Crypto.PublicKey import RSA
key = RSA.importKey(open('privacy_enhanced_mail.pem').read())
print(key.d)
