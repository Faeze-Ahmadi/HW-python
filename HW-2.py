# HW2
def celsius_to_fahrenheit(C):
    F = 1.8 * C + 32
    return F

C = float(input("Enter temperature in Celsius: "))
F = celsius_to_fahrenheit(C)
print(f"Temperature in Fahrenheit: {F}")

#HW3
def calculate_commission(store, sales):
    if store == 'A':
        if sales < 9:
            commission = 0
        elif 9 <= sales <= 15:
            commission = 0.05 * sales
        else:
            commission = 0.08 * sales
    elif store == 'B':
        if sales <= 7:
            commission = 0.04 * sales
        else:
            commission = 0.07 * sales
    else:
        commission = 0
    return commission

store = input("Enter the name of the store (A or B): ")
sales = float(input("Enter the sales amount: "))
commission = calculate_commission(store, sales)
print(f"Commission for store {store}: {commission}")
