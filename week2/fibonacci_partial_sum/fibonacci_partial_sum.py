# Uses python3
import sys
import math

pisano_mod_ten = [0, 1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1, 7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8,
                  7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3, 0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1]


def sum_list(list):
    if len(list) == 1:
        return list[0]

    return list[0] + sum_list(list[1:])


def fibonacci_partial_sum_naive(from_, to, debug=False):
    if to <= 1:
        return to

    previous = 0
    current = 1

    if debug:
        mods = [previous, current]
    for _ in range(from_ - 1):
        previous, current = current, previous + current
        if debug:
            mods.append(current % 10)

    if debug:
        print(mods, sum_list(mods))
    sum = current

    for _ in range(to - from_):
        previous, current = current, previous + current
        sum += current
        if debug:
            mods.append(current % 10)

    if debug:
        print(mods, sum_list(mods))
    return sum % 10


def fibonacci_partial_sum_fast(from_, to, debug=False):
    if to <= 1:
        return to

    mod_ten_period = 60
    sum_pisano_mod_ten = 280
    fast_sum = 0
    start_periods = 0
    periods = []
    count_to_offset = 2

    if from_ > 0:
        count_from = from_ % mod_ten_period
        from_sum = sum_list(pisano_mod_ten[count_from:])
        fast_sum += from_sum
        start_periods = (60 - count_from) + from_
        count_to_offset = 1
        if debug:
            periods.extend(pisano_mod_ten[count_from:])
            print('from', count_from, from_sum, pisano_mod_ten[count_from])

    count_to = to % mod_ten_period
    to_sum = sum_list(pisano_mod_ten[:count_to + count_to_offset]) # need to add 2 because it's position + exclusive
    fast_sum += to_sum

    end_periods = to - count_to
    iterations = math.floor((end_periods - start_periods) / mod_ten_period)
    if debug:
        print('iterations', iterations, start_periods, end_periods)

    if iterations > 0:
        fast_sum += iterations * sum_pisano_mod_ten
        if debug:
            for _ in range(iterations):
                periods.extend(pisano_mod_ten)

    if debug:
        print('to', count_to, to_sum, pisano_mod_ten[count_to])
        periods.extend(pisano_mod_ten[:count_to + 1])
        print(periods, fast_sum)

    return fast_sum % 10


def compare_partial(from_, to, debug=False):
    print(from_, to)

    result = fibonacci_partial_sum_naive(from_, to, debug)
    result2 = fibonacci_partial_sum_fast(from_, to, debug)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_n='', debug=False):
    if input_n != '':
        from_, to = map(int, input_n.split())
        compare_partial(from_, to, debug)
        return

    import random

    while True:
        from_ = random.randint(0, 1000)
        to = random.randint(from_, from_ + 1000)
        if not compare_partial(from_, to, debug):
            break


def main(input_n, naive=False, debug=False):
    from_, to = map(int, input_n.split())
    if naive:
        print(fibonacci_partial_sum_naive(from_, to))
    else:
        print(fibonacci_partial_sum_fast(from_, to, debug))


if __name__ == '__main__':
    input_r = sys.stdin.read()
    if 'stress' in input_r:
        if len(input_r) < 8:
            stress_test()
        else:
            stress_test(input_r[7:], True)
    elif 'debug' in input_r:
        if len(input_r) < 7:
            stress_test('', True)
        else:
            # stress_test(input_r[6:], True)
            main(input_r[6:], False, True)
    else:
        main(input_r)
