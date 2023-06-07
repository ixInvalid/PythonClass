# fib(0) =          0
# fib(1) =          1
# fib(2) = 1 + 0 or 1
# fib(3) = 1 + 1 or 2
# fib(4) = 2 + 1 or 3
# fib(n)
def fibonacci(n):
    """ this function prints the fibonacci sequence """

    if n <= 1:
        return n
    else:
        # formula: Fn = Fn-1 + Fn-2
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """ this is main and it runs the program """
    print(f'{"[Fibonacci Sequence]":-^28}')
    for i in range(1, 11):
        print(f'F_{i:<2} {fibonacci(i):>23}')


if __name__ == '__main__':
    main()
