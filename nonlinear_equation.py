from math import (sqrt, log, exp, sin, cos)



def my_equation(x):
    return sqrt(x)-pow(x,-1)*log(x+4)-1.5

epsilon = 0.000001
step = 0.001

def iter_proc(approximation):
    cur_x = approximation
    iterations = 0
    while True:
        cur_y = my_equation(cur_x)
        next_x =  cur_x - (cur_y*step)/(my_equation(cur_x+step)-cur_y)
        iterations += 1
        if abs(cur_x-next_x) <= epsilon:
            print("iterstions:", iterations)
            break
        cur_x = next_x
    return next_x

def main():
    print("Enter a start approximation:")
    print(iter_proc(float(input())))
    # print(iter_proc(4)

if __name__ == '__main__':
    main()