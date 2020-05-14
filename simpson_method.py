import math

# an increment of the integration step
w = 1
# a degree of the method
p = 4
# a range of the integration
a = 1
b = 2

# a step
h = 0.0625 * w
# a number of steps
n = 16

m = n // (2 * w)

expression = lambda x: x ** 4 * (1 + x ** 2) ** (-1)


def integrate():
    sum = 0
    x = a + h
    even = False
    while x < b:
        if even:
            sum += expression(x)
            print("even member: x = {}, y = {}".format(x, expression(x)))
        else:
            sum += 2 * expression(x)
            print("uneven member: x = {}, y = {}".format(x, expression(x)))

        x += h
        even = not even
    sum += (expression(a) + expression(b)) / 2
    return (2 * h / 3) * sum


def main():
    # a result with a unchanged step
    res1 = integrate()
    print("a result with the unchanged step is ", res1)
    print(
        "************************************************************************************************************")
    global h, p
    h = h * 2
    res2 = integrate()
    print("a result with the unchanged step is ", res1)
    print("a result with the doubled step is   ", res2)
    inaccuracy = (res1 - res2) / (2 ** p - 1)
    # get a degree of the first non zero digital
    degree = abs(int(math.log10(abs(inaccuracy))))
    # make a format string to output
    format_str = "%." + str(degree + 1) + "f"
    print("a result is {} ± {}".format(round(res1, degree + 1), format_str % (inaccuracy)))


if __name__ == '__main__':
    main()
