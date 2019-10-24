# andrei_shvedau
# var 5


def compr():
    '''
     You are given three integers x,y,z representing the dimensions of
    a cuboid along with an integer N.
     You have to print a list of all possible coordinates (i,j,k) given by
    on a 3D grid where the sum of is not equal to N.
    '''

    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i, j, k] for i in range(0, x + 1) for j in range(0, y + 1)
           for k in range(0, z + 1) if (i + j + k) != n])


if __name__ == '__main__':
    compr()
