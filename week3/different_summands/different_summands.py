# Uses python3
import sys


def optimal_summands(n, debug=False):
    if n == 0:
        return 0
    if n == 1:
        return [1]
    if n == 2:
        return [2]
    summands = []
    sum = 0
    rem = n
    current = 1
    summands.append(current)
    sum += current
    rem -= current
    # iterate
    while rem > 0:
        current += 1
        next_value = current + 1
        if rem == current:
            summands.append(current)
            break
        if rem - current < next_value:
            if debug:
                print('continue', ['rem', rem], ['current', current], ['next', next])
            continue
        if debug:
            print('iteration', ['rem', rem], ['current', current], ['next', next_value], summands)
        sum += current
        if rem - current < next_value:
            continue
        rem -= current
        summands.append(current)
        if sum == n:
            break

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
