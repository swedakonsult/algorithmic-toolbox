# Uses python3
import sys


def invalid_input(message):
    print("Error when executing script:", message, "\npython3", sys.argv[0], """
    n
    a(0) ... a(n)
    b(0) ... b(n)""")


def shift_list(l):
    first = l.pop(0)
    l.append(first)

def max_dot_product(a, b, debug=False):
    # write your code here
    res = [0 for q in range(len(a))]
    a = sorted(a, reverse=True)
    if debug:
        print('sorted a', a)
    b = sorted(b, reverse=True)
    if debug:
        print('sorted b', b)
    for n in range(len(a)):
        for i in range(len(a)):
            res[n] += a[i] * b[i]
        shift_list(a)
    if debug:
        print('greedy results', res)
    res = sorted(res, reverse=True)
    if debug:
        print('sorted', res)
    return res[0]


def max_dot_product_fast(a, b, debug=False):
    return 0


def main(input_m, naive=True, debug=False):
    data = list(map(int, input_m.split()))
    if debug:
        print(data)
    try:
        n = data[0]
        a = data[1:(n + 1)]
        b = data[(n + 1):]
    except IndexError:
        invalid_input('')
        sys.exit(1)

    if naive:
        opt_value = max_dot_product(a, b, debug)
    else:
        opt_value = max_dot_product_fast(a, b, debug)

    print(opt_value)

if __name__ == '__main__':
    input_m = sys.stdin.read()
    if 'debug' in input_m:
        if len(input_m) < 7:
            invalid_input('debug without values')
        else:
            # stress_test(input_r[6:], True)
            main(input_m[6:], True, True)
    else:
        main(input_m)
