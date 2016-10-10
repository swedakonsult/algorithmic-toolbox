# Uses python3
import sys


# 1 <= a, b <= 2 x 10^9
def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_euclidean(a, b):
    if b == 0:
        return a
    a_prime = a % b
    return gcd_euclidean(b, a_prime)


def stress_test():
    import random

    while True:
        a = random.randint(0, 100000)
        b = random.randint(0, 100000000)
        print(a, b)

        result = gcd_naive(a, b)
        result2 = gcd_euclidean(a, b)
        if result != result2:
            print("Wrong answer:", result, " ", result2)
            break
        else:
            print('OK')


def main(input_n):
    a, b = map(int, input_n.split())
    # print(gcd_naive(a, b))
    print(gcd_euclidean(a, b))

if __name__ == "__main__":
    input_r = sys.stdin.read()
    if 'stress' in input_r:
        stress_test()
    else:
        main(input_r)
