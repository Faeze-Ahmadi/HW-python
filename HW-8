#HW8 (قسمت اول)


def approximate_pi(n_terms):
    pi = 0
    for i in range(n_terms):
        term = 4 / (1 + 2 * i)
        if i % 2 == 0:
            pi += term
        else:
            pi -= term
    return pi

# Example: n_terms = 100000
print(f"Approximation of pi is {approximate_pi(100000):.10f}")

#HW8 (قسمت دوم)


grades = [14, 13, 17, 16, 12, 15, 10, 11, 9, 16, 14, 17, 16, 4, 7, 12, 14, 18]

def calculate_average(grades):
    return sum(grades) / len(grades)

def first_above_average(grades, average):
    for index, grade in enumerate(grades):
        if grade > average:
            return index
    return None

average_grade = calculate_average(grades)
print(f"Class average is {average_grade:.2f}")
first_index = first_above_average(grades, average_grade)
if first_index is not None:
    print(f"First student scoring above average is at index {first_index} with grade {grades[first_index]}")
else:
    print("No student scored above average")