# increment of the integration step
w = 1

# range of the integration
a = 1
b = 2

# step
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
    sum += (expression(a)+expression(b))/2
    return (2*h/3) * sum


def main():
    print("result is", integrate())

if __name__ == '__main__':
    main()
