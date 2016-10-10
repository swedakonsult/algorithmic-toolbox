# Uses python3

def pairwiseProduct(size, numbers):
    result = 0

    for i in range(0, size):
        for j in range(i+1, size):
            if numbers[i]*numbers[j] > result:
                result = numbers[i]*numbers[j]

    return result

def pairwiseProductFast1(size, numbers):
    max_index = -1
    for i in range(0, size):
        if max_index == -1 or numbers[i] > numbers[max_index]:
            max_index = i

    max_index2 = -1
    for j in range(0, size):
        if (numbers[j] != numbers[max_index]) and (max_index2 == -1 or numbers[j] > numbers[max_index2]):
            max_index2 = j

    return numbers[max_index] * numbers[max_index2]

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    assert(len(a) == n)

    #result = pairwiseProduct(n, a)
    #print(result)
    result = pairwiseProductFast1(n, a)
    print(result)

main()
