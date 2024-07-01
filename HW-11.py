#HW11

import math

def calculate_series_sum(N):
    s = sum(math.sin(10 * i) for i in range(1, N + 1))
    return s

# Example usage
N = 100  # You can change N to any value
result = calculate_series_sum(N)
print(f"Sum of the series: {result}")
