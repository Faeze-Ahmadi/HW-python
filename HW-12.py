#HW12

def is_valid_number(number):
    if 10000 <= number <= 200000:
        return True
    return False

# Example usage
number = 157  # You can change the number to test
if is_valid_number(number):
    print(f"{number} is a valid number.")
else:
    print(f"{number} is not a valid number.")
