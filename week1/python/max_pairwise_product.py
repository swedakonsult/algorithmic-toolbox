# Uses python3

def pairwiseProduct(size, numbers, debug = False):
    result = 0

    for i in range(0, size):
        for j in range(i+1, size):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]

    if debug:
        print("[", numbers[i], "*", numbers[j], "=", result, end = ']')
    return result

def pairwiseProductFast1(size, numbers, debug = False):
    max_index = -1
    for i in range(0, size):
        if max_index == -1 or numbers[i] > numbers[max_index]:
            max_index = i

    max_index2 = -1
    for j in range(0, size):
        if (j != max_index) and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    result = numbers[max_index] * numbers[max_index2]

    if debug:
        print("[", numbers[max_index], "*", numbers[max_index2], "=", result, end = ']')
    return result

def stressTest():
    import random

    while True:
        n = random.randint(2,12)
        print(n)
        a = [random.randint(0, 100000) for i in range(0, n)]
        for i in range(0, n):
            print(a[i], end = ' ')

        print('')
        result = pairwiseProduct(n, a)
        result2 = pairwiseProductFast1(n, a)
        if result != result2:
            print("Wrong answer:", result, " ", result2)
            break;
        else:
            print('OK')

def main():
    input_n = input()
    assert(len(input_n) != 0)
    assert(' ' not in input_n)

    if 'stress' in input_n:
        stressTest()
        return

    n = int(input_n)
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    #result = pairwiseProduct(n, a)
    #print(result)
    result = pairwiseProductFast1(n, a)
    print(result)

main()
