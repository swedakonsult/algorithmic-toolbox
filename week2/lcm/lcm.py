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
    lcm = (a * b) / gcd

    return int(lcm)


def main(input_n):
    a, b = map(int, input_n.split())
    #print(lcm_naive(a, b))
    print(lcm_fast(a, b))

if __name__ == '__main__':
    input_r = sys.stdin.read()
    main(input_r)

