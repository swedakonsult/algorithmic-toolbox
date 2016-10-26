# Uses python3
# Input Format: The first line of the input contains an integer 𝑛. The second line contains integers 𝑎1,𝑎2,...,𝑎𝑛.
# Constraints: 1 ≤ 𝑛 ≤ 100;1 ≤ 𝑎𝑖 ≤ 103 for all 1 ≤ 𝑖 ≤ 𝑛
import sys
import math

'''LargestNumber(Digits): answer ← empty string while Digits is not empty:
maxDigit ← −∞ for digit in Digits:
if digit ≥ maxDigit: maxDigit ← digit
append maxDigit to answer
remove maxDigit from Digits return answer'''


def largest_number(a):
    # write your code here
    maxDigit = 0
    res = sorted(a, reverse=True,
                 key=lambda number: math.floor(int(number) / 100) if int(number) >= 100 else math.floor(
                     int(number) / 10) if int(number) >= 10 else int(number))
    # TODO: doesn't work for single digit comparing to integers with a smaller second digit
    # TODO: if(current.len > 1 && next.len == 1)

    # print(res)
    return "".join(res)


def main(input_m):
    data = input_m.split()
    a = data[1:]
    return largest_number(a)


if __name__ == '__main__':
    input_m = sys.stdin.read()
    print(main(input_m))
