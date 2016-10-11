# Uses python3
import sys


# 1≤𝑛≤1018, 2≤𝑚≤105
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def compare_n_m(n, m):
    print(n, m)

    result = get_fibonacci_huge_naive(n, m)
    result2 = 0 # lcm_fast(a, b)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_n=''):
    if input_n != '':
        n, m = map(int, input_n.split())
        compare_n_m(n, m)
        return

    import random

    while True:
        n = random.randint(0, 1000)
        m = random.randint(0, 1000)
        if not compare_n_m(n, m):
            break


def main(input_n, naive=False, debug=False):
    n, m = map(int, input_n.split())
    if naive:
        print(get_fibonacci_huge_naive(n, m))
    else:
        print('none', debug) # print(lcm_fast(n, m, debug))


if __name__ == '__main__':
    input_r = sys.stdin.read()
    if 'stress' in input_r:
        if len(input_r) < 8:
            stress_test()
        else:
            stress_test(input_r[7:])
    elif 'debug' in input_r:
        main(input_r[:-6], False, True)
    else:
        main(input_r, True)
