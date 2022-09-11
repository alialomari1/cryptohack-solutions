M = Matrix(GF(2), [list(map(int, row)) for row in open("flag.enc").read().splitlines()])
M ^= pow(31337, -1, M.multiplicative_order())
bin_flag = ''.join([str(bit) for col in M.columns()[:(32*8//50)+1] for bit in col])
print(bytes.fromhex(hex(int(bin_flag[:34*8],2))[2:]).decode())
