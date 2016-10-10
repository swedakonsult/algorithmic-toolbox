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
def lcm_fast(a, b):
    gcd = gcd_euclidean(a, b)
    ab = a * b
    if gcd == 0:
        return ab
    lcm = ab / gcd

    return int(lcm)


def stress_test():
    import random

    while True:
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        print(a, b)

        result = lcm_naive(a, b)
        result2 = lcm_fast(a, b)
        if result != result2:
            print("Wrong answer:", result, " ", result2)
            break
        else:
            print('OK')


def main(input_n):
    a, b = map(int, input_n.split())
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))

if __name__ == '__main__':
    input_r = sys.stdin.read()
    if 'stress' in input_r:
        stress_test()
    else:
        main(input_r)

