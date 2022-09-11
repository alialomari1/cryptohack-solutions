from Crypto.Util.Padding import unpad
from Crypto.Cipher import AES

key = bytes.fromhex(hex(32868722058267583893568745879285086202256179377510509278858008079221735833947)[2:])
iv = "43f14157442d75142d0d4993e99a9582"
ciphertext = "22abc3b347ffef55ec82488e5b4a338da5af7ef1918ac46f95029a4d94ace4cb2700fa9aeb31e6a4facee2601e99dabd6f9a81494c55f011e9227c9a6ae8d802"
cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(iv))
flag = cipher.decrypt(bytes.fromhex(ciphertext))
print(unpad(flag, 16).decode())
