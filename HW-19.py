# HW19
def calculate_series_sum(n):
    s = sum(k / (k**2 + k) for k in range(1, n + 1))
    return s

# Example usage
numbers = [10, 20, 100]  # You can change the numbers
for n in numbers:
    result = calculate_series_sum(n)
    print(f"Sum of series for n = {n} is {result} (HW19)")
