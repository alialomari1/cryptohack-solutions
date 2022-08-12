print('crypto{%s}' % ''.join(chr(i^13) for i in b'label'))
