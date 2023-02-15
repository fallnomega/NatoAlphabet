import pandas

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
with open("nato_phonetic_alphabet.csv") as file:
    temp = pandas.read_csv(file)
    phonetic_alphabet = {row.letter: row.code for (index, row) in temp.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.

player_word = input("Enter a word: ")
letters = [letter.upper() for letter in player_word]
new_list = [phonetic_alphabet[letter] for letter in letters]
print(new_list)

exit()
