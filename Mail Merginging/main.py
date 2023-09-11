# PLACEHOLDER = "[name]"
#
# with open("../Mail Merginging/Input/Names/invited_names.txt", mode="r") as Name:
#     content = Name.readlines()
#
# actual_name_list = []
# for name in content:
#     # strip() method is used on each name read from the file to remove leading and trailing whitespace characters, including the newline character.
#     actual_name_list.append(name.strip())
# #FILE Paths👇
# """
# to starting letters
# ../Mail Merginging/Input/Letters/starting_letter.txt
#
# to invited names
# ../Mail Merginging/Input/Names/invited_names.txt
#
# to ready to send
# ../Mail Merginging/Output/ReadyToSend/example.txt
#
# to main
#
# main.py
#
# """
#
# ID = 1
# for name in actual_name_list:
#     #This will name every file letter with a unique ID
#     future_file_name = f"letter {ID}.txt"
#
#     with open("../Mail Merginging/Input/Letters/starting_letter.txt", mode="r") as starting_letter:
#         #['Dear [name],\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can mak…
#         letter_content_lists = starting_letter.readlines()
#
#     letter_content = ""
#     for word in letter_content_lists:
#         sentence = word.strip()
#         letter_content += sentence
#     #'Dear [name],You are invited to my birthday this Saturday.Hope you can make it!Angela'
#     final_sentence = letter_content.replace(PLACEHOLDER, f"{name}")
#
#     with open(f"../Mail Merginging/Output/ReadyToSend/letter_for_{name}", mode="w") as Ready_to_Send:
#         Ready_to_Send.write(final_sentence)
#
#     ID += 1

PLACEHOLDER = "[name]"


with open("../Mail Merginging/Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("../Mail Merginging/Input/Letters/starting_letter.txt", mode="r") as  letter_file:
    # ['Dear [name],\n', '\n', 'You are invited to my birthday this Saturday.\n', '\n', 'Hope you can mak…
    letter_contents = letter_file.read()
    # Aang
    for name in names: #For each name and length of names do this
        # strip() method is used on each name read from the file to remove leading and trailing whitespace characters, including the newline character.
        stripped_name = name.strip()
        #                                    [name]        Aang
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)

