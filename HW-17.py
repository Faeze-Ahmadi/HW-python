# HW17
def process_string(s):
    upper_s = s.upper()
    lower_s = s.lower()
    length = len(s)
    joined_s = '***'.join(s)

    return upper_s, lower_s, length, joined_s

# Example usage
sentence = "Hello World!"  # You can change the sentence
upper_s, lower_s, length, joined_s = process_string(sentence)
print(f"Upper case: {upper_s} (HW17)")
print(f"Lower case: {lower_s} (HW17)")
print(f"Length: {length} (HW17)")
print(f"Joined with ***: {joined_s} (HW17)")
