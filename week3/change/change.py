# Uses python3
import sys


def get_change_naive(m, debug=False):
    # write your code here
    coins = 0
    # safe first move: remove largest possible from m
    while True:
        if m == 0:
            if debug:
                print("done")
            return coins
        if m >= 10:
            coins += 1
            m -= 10
            if debug:
                print("[10]", m, coins)
            continue
        if m >= 5:
            coins += 1
            m -= 5
            if debug:
                print("[5]", m, coins)
            continue
        if m >= 1:
            coins += 1
            m -= 1
            if debug:
                print("[1]", m, coins)
            continue

    if debug:
        print("Error", m, coins)
    return coins


def get_change_fast(m, debug=False):
    # write your code here
    return get_change_naive(m, debug)


def compare_change(m, debug=False):
    print(m)

    result = get_change_naive(m, debug)
    result2 = get_change_fast(m, debug)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_m='', debug=False):
    if input_m != '':
        m_ = int(input_m)
        compare_change(m_, debug)
        return

    import random

    while True:
        m_ = random.randint(0, 1000)
        if not compare_change(m_, debug):
            break


def main(input_m, naive=True, debug=False):
    m_ = int(input_m)
    if naive:
        print(get_change_naive(m_, debug))
    else:
        print(get_change_fast(m_, debug))


if __name__ == '__main__':
    input_m = sys.stdin.read()
    if 'stress' in input_m:
        if len(input_m) < 8:
            stress_test()
        else:
            stress_test(input_m[7:], True)
    elif 'debug' in input_m:
        if len(input_m) < 7:
            stress_test('', True)
        else:
            # stress_test(input_r[6:], True)
            main(input_m[6:], True, True)
    else:
        main(input_m)
