#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Names/invited_names.txt") as name_list:
    names = name_list.readlines()

with open("./input/letters/starting_letter.txt") as letter:
    starting_letter_template = letter.read()


for name in names:
    new_name = name.strip()
    new_letter = starting_letter_template.replace("[name]", new_name)
    with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as sent_letter:
        sent_letter.write(new_letter)