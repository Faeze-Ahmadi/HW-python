# HW4
def get_integer():
    while True:
        user_input = input("Enter an integer: ")
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("That's not an integer. Please try again.")

def sum_of_digits(number):
    return sum(int(digit) for digit in str(abs(number)))

number = get_integer()
digit_sum = sum_of_digits(number)
print(f"Sum of the digits: {digit_sum}")
