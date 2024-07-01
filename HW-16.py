#HW16

def have_common_elements(list1, list2):
    return any(elem in list2 for elem in list1)

# Example usage
list1 = [1, 2, 3, 4]  # You can change the lists
list2 = [3, 4, 5, 6]
if have_common_elements(list1, list2):
    print("The lists have common elements.")
else:
    print("The lists do not have common elements.")
