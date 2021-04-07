import pandas


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
_alpha = {row.letter:row.code for (index, row) in alphabet.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Provide a word: ")
output = [_alpha[letter] for letter in user_input.upper()]
print(output)