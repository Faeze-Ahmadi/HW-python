# HW20
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def list_primes_up_to(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return primes

# Example usage
limits = [50, 100, 200]  # You can change the limits
for n in limits:
    primes = list_primes_up_to(n)
    print(f"Prime numbers up to {n}: {primes} (HW20)")
