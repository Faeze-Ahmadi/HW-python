#HW6

import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance

# Test cases
test_cases = [
    (10, 11, 25, 35),
    (21, 12, 60, 2),
    (-2.5, 1, 5.5, 4),
    (21, 11, 35, 12),
    (12, 12, 2, 16)
]

for x1, y1, x2, y2 in test_cases:
    print(f"Distance between ({x1}, {y1}) and ({x2}, {y2}) is {calculate_distance(x1, y1, x2, y2):.2f}")
