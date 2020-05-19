import math
from sys import float_info
# a degree of the method
p = 4

expression = lambda x: x ** 4 * (1 + x ** 2) ** (-1)


def integrate(a, b, h):
    sum = 0
    x = a + h
    even = False
    inaccuracy = 10 ** math.floor(math.log10(h)  )
    while math.fabs(x - b) > inaccuracy:
        if even:
            sum += expression(x)
            # print("even member: x = {}, y = {}".format(x, expression(x)))
        else:
            sum += expression(x) * 2
            # print("uneven member: x = {}, y = {}".format(x, expression(x)))

        x += h
        even = not even
    sum += (expression(b) + expression(a)) / 2
    return (2 * h / 3) * sum


def main():
    # a range of the integration
    a = int(input("Enter a start of a integration segment "))
    b = int(input("Enter a end of a integration segment "))

    n = input("Enter a number of steps ")
    n = int(n)
    if n % 4 != 0:
        while n % 4 != 0:
            n += 1
        print("Your n is not a multiple of 4 number, but the program found one. Now, n is ", n)

    h = (b - a) / n
    print("a step of integration is ", h)
    print("***********************************************************************************************************")
    # a result with a unchanged step
    res1 = integrate(a, b, h)
    print("a result with the unchanged step is ", res1)
    print(
        "************************************************************************************************************")
    h = h * 2
    res2 = integrate(a, b, h)
    print("a result with the unchanged step is ", res1)
    print("a result with the doubled step is   ", res2)
    inaccuracy = math.fabs(res1 - res2) / (2 ** p - 1)
    # get a degree of the first non zero digit
    degree = abs(int(math.log10(abs(inaccuracy))))
    # make a format string to output
    format_str = "%." + str(degree + 1) + "f"
    print("a result is {} ± {}".format(round(res1, degree + 1), format_str % (inaccuracy)))
    print("a step of integration is ", h)


if __name__ == '__main__':
    main()
