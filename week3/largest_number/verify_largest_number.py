# Using Python3
import sys
import largest_number


def test_case(caseNumber, expectedResult):
    with open('test'+str(caseNumber)+'.txt', 'r') as source:
        content = source.read()
    results = int(largest_number.main(content))
    passed = results == expectedResult
    return passed, results, content if not passed else ''


if __name__ == '__main__':
    input = sys.stdin.read()
    test_results = []
    passed = test_case(1, 221)
    test_results.append(passed)
    passed = test_case(2, 99641)
    test_results.append(passed)
    passed = test_case(3, 923923)
    test_results.append(passed)
    passed = test_case(4, 33823)
    test_results.append(passed)
    print(test_results)
