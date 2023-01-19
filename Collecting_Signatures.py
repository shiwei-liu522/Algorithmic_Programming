# Covering Segments by Points Problem
# Find the minimum number of points needed to cover all given segments on a line.
# Input: A sequence of n segments[l1, r1], . . . , [ln, rn] on a line.
# Output: A set of points of minimum size such that each segment[li , ri ] contains a point, i.e., there exists a point x from this set such that li ≤ x ≤ ri .

num_segments = int(input())
segments = []
for _ in range(num_segments):
    segments.append(list(map(int, input().split())))
segments = sorted(segments, key=lambda x: x[1])
points = []
for segment in segments:
    if not points or segment[0] > points[-1]:
        points.append(segment[1])
print(len(points))
print(' '.join(map(str, points)))
