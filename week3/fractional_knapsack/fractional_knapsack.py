# Uses python3
import sys


def invalid_input(message):
    print("Error when executing script:", message, "\npython3", sys.argv[0], """
    n capacity
    v(0) w(0)
    .
    .
    v(n) w(n)""")


def sort(weights, values, debug):
    if len(weights) < 1:
        return []
    weight_index = 1
    value_index = 0
    items = list(zip(values, weights))
    if debug:
        print('sorting', items)
    if len(weights) == 1:
        return items;

    return sorted(items, key=lambda weight_value: weight_value[value_index]/weight_value[weight_index], reverse=True)


def get_optimal_value(capacity, weights, values, debug=False):
    value = 0.
    # write your code here
    # safe first move: use the highest value / weight item first
    if capacity == 0 or len(weights) == 0:
        return value
    items = sort(weights, values, debug)
    if debug:
        print('sorted', items)

    # TODO: use the highest weighted item and start iterating
    for t in items:
        if capacity == 0:
            break
        t_weight = t[1]
        t_value = t[0]
        if t_weight <= capacity:
            value += t_value
            capacity -= t_weight
            if debug:
                print('full', t, 'value', value, 'capacity', capacity)
        else:
            fraction = capacity/t_weight
            value += t_value*fraction
            capacity = 0
            if debug:
                print('fraction', "{:.4f}".format(fraction), t, 'value', "{:.4f}".format(value), 'capacity', capacity)
            break

    return value


def get_optimal_value_fast(capacity, weights, values):
    value = 0.
    # write your code here

    return value


def compare_functions(m, debug=False):
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
        compare_functions(m_, debug)
        return

    import random

    while True:
        m_ = random.randint(0, 1000)
        if not compare_functions(m_, debug):
            break


def main(input_m, naive=True, debug=False):
    data = list(map(int, input_m.split()))
    if debug:
        print(data)

    try:
        n, capacity = data[0:2]
    except ValueError:
        invalid_input('"n capacity" are required on the first input line')
        sys.exit(1)
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    if naive:
        opt_value = get_optimal_value(capacity, weights, values, debug)
    else:
        opt_value = get_optimal_value_fast(capacity, weights, values, debug)

    print("{:.4f}".format(opt_value))

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
