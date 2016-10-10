# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def calc_fibFast(n, lst):
    if n <= 1:
        return n

    if lst[n] > 0:
        #print('hit:', n)
        return lst[n]

    r = calc_fibFast(n - 1, lst) + calc_fibFast(n - 2, lst)
    lst[n] = r
    return r


def main():
    n = int(input())

    # expecting range of n: 0 <= n <= 45
    lst = [0 for i in range(46)]
    print(calc_fibFast(n, lst))

main()
