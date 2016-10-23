# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')


def find_matches(segments, points, debug=True):
    if debug:
        print('segments', segments)
    min_right = segments[0]
    if debug:
        print('minimum right', min_right)
    if len(segments) <= 1:
        points.append(min_right.start)
        return
    else:
        points.append(min_right.end)
    segs = segments[1:]
    for i, s in enumerate(segs):
        if debug:
            print('compare', min_right, 's:', s.start)
        if s.start <= min_right.end:
            continue
        if debug:
            print(min_right.end, '<', s.start)
        find_matches(segs[i:], points, debug)
        break


def optimal_points(segments, debug=False):
    points = []
    # write your code here
    sorted_segs = sorted(segments, key=lambda seg: seg.end)
    if debug:
        print('sorted', sorted_segs)
    # find the minimum right endpoint
    find_matches(sorted_segs, points, debug)
    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
