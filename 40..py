import random
while True:
    def determinant(matrix):
        det=matrix[0]*matrix[3]-matrix[1]*matrix[2]
        return det
    mat0=random.randint(-1000,1000)
    mat1=random.randint(-1000,1000)
    mat2=random.randint(-1000,1000)
    mat3=random.randint(-1000,1000)
    lst=[mat0,mat1,mat2,mat3]
    if 10<=determinant(lst)<=20:
        print(lst[0],lst[1])
        print(lst[2],lst[3])
        print(determinant(lst))
        break