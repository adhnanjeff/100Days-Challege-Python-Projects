PLACEHOLDER = "[name]"

with open("Base/Projects/Day 24/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("Base/Projects/Day 24/Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"Base/Projects/Day 24/Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

