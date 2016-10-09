# Uses python3

def pairwiseProduct(size, numbers):
    result = 0

    for i in range(0, size):
        for j in range(i+1, size):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]

    return result


def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    result = pairwiseProduct(n, a)
    print(result)

main()
