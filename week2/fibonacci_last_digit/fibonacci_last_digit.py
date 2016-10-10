# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def calc_fibFast(n, lst):
    if n <= 1:
        return n

    if lst[n] > 0:
        #print('hit:', n)
        return lst[n]

    r = calc_fibFast(n - 1, lst) + calc_fibFast(n - 2, lst)
    lst[n] = r
    return r


def get_fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    #lst = [0 for i in range(10000000)]
    #return (calc_fibFast(n-2, lst) + calc_fibFast(n-1, lst)) % 10
    minusone = 1
    minustwo = 0

    for _ in range(n - 2):
        minustwo, minusone = minusone, (minustwo + minusone) % 10

    return (minusone + minustwo) % 10


def stressTest():
    import random

    while True:
        n = random.randint(0, 100000)
        print(n)

        result = get_fibonacci_last_digit_naive(n)
        result2 = get_fibonacci_last_digit_fast(n)
        if result != result2:
            print("Wrong answer:", result, " ", result2)
            break;
        else:
            print('OK')


def main():
    input_n = input()
    if 'stress' in input_n:
        stressTest()
        return

    n = int(input_n)
    #print(get_fibonacci_last_digit_naive(n))
    print(get_fibonacci_last_digit_fast(n))

main()
