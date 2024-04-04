import pandas

data = pandas.read_csv("Base/Projects/Day 26/nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for (index,row) in data.iterrows()}

user = input("Enter a word: ").upper()

output_list = [new_dict[char] for char in user]
print(output_list)