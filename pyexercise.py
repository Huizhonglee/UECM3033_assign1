import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.sqrt(x)*(sy.exp(-x)), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [ [1,1,2,3,4,5,6,3,4,5], 
                    [2,2,3,4,5,6,7,8,9,5],
                    [3,4,5,3,2,1,4,5,6,4],
                    [4,1,4,6,4,6,7,8,4,5],
                    [5,5,6,7,6,9,1,3,4,5],
                    [6,3,4,5,1,6,3,8,3,5],
                    [7,2,4,6,6,4,6,3,6,8],
                    [8,2,4,6,7,9,4,6,3,4],
                    [9,4,5,7,3,8,5,2,5,6],
                    [10,4,5,3,7,7,9,4,6,2]] )
    b = np.array([9,8,7,6,5,4,3,2,1,3])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1302944
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
