# Uses python3
import sys


def gcd_euclidean(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd_euclidean(b, a_prime)


# 1 <= a, b <= 2 x 10^9
def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b


# LCM(a,b) x GCD(a,b) = a x b
def lcm_fast(a, b, debug=False):
    gcd = gcd_euclidean(a, b)
    if debug:
        print('gcd', gcd)
    if gcd == 0:
        return a * b
    if a < b:
        small = int(b / gcd)
        lcm = a * small
    else:
        small = int(a / gcd)
        lcm = b * small

    if debug:
        print('small', small)

    return int(lcm)


def compare_a_b(a, b):
    print(a, b)

    result = lcm_naive(a, b)
    result2 = lcm_fast(a, b)
    if result != result2:
        print("Wrong answer:", result, " ", result2)
        return False
    else:
        print('OK')
        return True


def stress_test(input_n=''):
    if input_n != '':
        a, b = map(int, input_n.split())
        compare_a_b(a, b)
        return

    import random

    while True:
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        if not compare_a_b(a, b):
            break


def main(input_n, naive=False, debug=False):
    a, b = map(int, input_n.split())
    if naive:
        print(lcm_naive(a, b))
    else:
        print(lcm_fast(a, b, debug))

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
        main(input_r)

