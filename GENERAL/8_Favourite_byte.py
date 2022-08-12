enc = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
key = enc[0] ^ ord('c')
print('FLAG:', ''.join(chr(c ^ key) for c in enc))
