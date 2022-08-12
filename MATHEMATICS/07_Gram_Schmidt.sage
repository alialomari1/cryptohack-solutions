A = matrix([[4,1,3,-1], [2,1,-3,4], [1,0,-2,7], [6, 2, 9, -5]])
x = A.gram_schmidt()[0][3][1]
print(round(x, 5))
