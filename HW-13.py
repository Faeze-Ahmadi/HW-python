#HW13

def contains_word_dollar(sentence):
    return 'دلار' in sentence

# Example usage
sentence = "این جمله شامل کلمه دلار است."  # You can change the sentence
if contains_word_dollar(sentence):
    print("The sentence contains the word 'دلار'.")
else:
    print("The sentence does not contain the word 'دلار'.")
