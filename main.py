PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = letter.replace(PLACEHOLDER,strip_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter for{strip_name}",mode="w") as completed_letter:
            completed_letter.write(new_letter)

