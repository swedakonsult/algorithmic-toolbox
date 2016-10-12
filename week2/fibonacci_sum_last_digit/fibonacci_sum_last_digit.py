# Uses python3
import sys
import math

pisano_mod_ten = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8,
                  7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]


def sum_list(list):
    if len(list) == 1:
        return list[0]

    return list[0] + sum_list(list[1:])


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sum = 1

    # mods = [previous, current]
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
        # mods.append(current % 10)

    # print(mods, sum_list(mods))
    return sum % 10


def fibonacci_sum_fast(n, debug=False):
    if n <= 1:
        return n

    mod_ten_period = 60
    sum = 0
    if n > mod_ten_period:
        iterations = math.floor(n/mod_ten_period)
        sum += iterations * sum_list(pisano_mod_ten)
        n %= mod_ten_period
        if debug:
            print('iterations', iterations, 'sum', sum, 'n', n, pisano_mod_ten[n])

    sum += sum_list(pisano_mod_ten[:n + 1])
    if debug:
        print('final sum', sum)

    return sum % 10


def compare_n(n, debug=False):
    print(n)

    result = fibonacci_sum_naive(n)
    result2 = fibonacci_sum_fast(n, debug)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_n='', debug=False):
    if input_n != '':
        n = int(input_n)
        compare_n(n, debug)
        return

    import random

    while True:
        n = random.randint(0, 1000)
        if not compare_n(n, debug):
            break


def main(input_n, naive=False, debug=False):
    n = int(input_n)
    if naive:
        print(fibonacci_sum_naive(n))
    else:
        print(fibonacci_sum_fast(n, debug))


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
            # stress_test(input_r[6:], True)
            main(input_r[6:], False, True)
    else:
        main(input_r)
