# 3 * 1 = 3
# 3 * 2 = 3 + 3
# 3 * 3 = 3 + (3 + 3) or 3 + 3 *2
def multiply(x, y):
    # every recursive function has a base case - the condition that causes it to stop
    if y == 1:
        return x
    else:
        # when it's not the base case the function calls itself with a parameter value that approaches the base case
        return x + multiply(x, y - 1)


# 1! =
# 2! = 2 * 1
# 3! = 3 * 2 * 1 or 3 * 2!
def factorial(n):
    # every recursive function has a base case - the condition that causes it to stop
    if n == 1:
        return 1
    else:
        # when it's not the base case the function calls itself with a parameter value that approaches the base case
        return n * factorial(n - 1)


# gcd of 3 and 0 is 3
# gcd of 3 and 3 is gcd of 3 and 3 % 3
# gcd of 3 and 6 is gcd of 6 and 3 is gcd of 3 and 6 % 3 (which is 0) OR
# gcd of n1 and n2 is gcd of n2 and n1 % n2 until n2 is 0 - Euclid's algorithm
def gcd(n1, n2):
    # every recursive function has a base case - the condition that causes it to stop
    if n2 == 0:
        return n1
    else:
        # when it's not the base case the function calls itself with a parameter value that approaches the base case
        return gcd(n2, n1 % n2)


def main():
    print(multiply(5, 3))
    print("Multiply");
    for n in range(1, 11):
        print("5 * {0:2d} is {1:2d}".format(n, multiply(5, n)));
    print();

    print("Factorial");
    for n in range(1, 11):
        print("5 * {0:2d} is {1:10d}".format(n, factorial(n)));
    print();

    print("GCD");
    print(f"3 and 0 should be 3: {gcd(3, 0)}");
    print(f"6 and 9 should be 3: {gcd(6, 9)}");
    print(f"49 and 21 should be 7: {gcd(49, 21)}");
    print();


main()


