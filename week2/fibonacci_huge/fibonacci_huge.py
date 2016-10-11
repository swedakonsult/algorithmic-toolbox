# Uses python3
import sys


# 1≤𝑛≤1018, 2≤𝑚≤105
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def find_pisano_period(n, m, debug=False):
    if m == 2:
        return 3, 0
    elif m == 3:
        return 8, 0
    elif m == 4:
        return 6, 0
    elif m == 5:
        return 20, 0

# find the '01' pattern, iterating from n = 0
    previous = 0
    current = 1

    for i in range(n - 1):
        previous, current = current, previous + current
        mod_p = previous % m
        mod_c = current % m
        if debug:
            print(i, end=',')
        if mod_p == 0 and mod_c == 1:
            # found the period of Pisano
            print('')
            return i + 1, 0

    print('')
    return 0, mod_c


def get_fibonacci_huge_fast(n, m, debug=False):
    if n <= 1:
        return n

    m_period, res = find_pisano_period(n, m, debug)
    if debug:
        print('period', m_period)
    if m_period == 0:
        if debug:
            print('full iteration')
        return res
    n_snubbed = n % m_period
    if debug:
        print('period remainder', n_snubbed)
    if n_snubbed == 0:
        return 0
    elif n_snubbed == 1:
        return 1

    previous = 0
    current = 1

    for _ in range(n_snubbed - 1):
        previous, current = current, previous + current

    return current % m


def compare_n_m(n, m, debug=False):
    print(n, m)

    result = get_fibonacci_huge_naive(n, m)
    result2 = get_fibonacci_huge_fast(n, m, debug)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_n='', debug=False):
    if input_n != '':
        n, m = map(int, input_n.split())
        compare_n_m(n, m, debug)
        return

    import random

    while True:
        n = random.randint(1, 1000)
        m = random.randint(2, 1000)
        if not compare_n_m(n, m, debug):
            break


def main(input_n, naive=False, debug=False):
    n, m = map(int, input_n.split())
    if naive:
        print(get_fibonacci_huge_naive(n, m))
    else:
        print(get_fibonacci_huge_fast(n, m, debug))


if __name__ == '__main__':
    input_r = sys.stdin.read()
    if 'stress' in input_r:
        if len(input_r) < 8:
            stress_test()
        else:
            stress_test(input_r[7:])
    elif 'debug' in input_r:
        if len(input_r) < 7:
            stress_test('', True)
        else:
            stress_test(input_r[6:], True)
        # main(input_r[:-6], False, True)
    else:
        main(input_r)
