# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)
#

#have to open in write since it is automatically read only when opened
#w is write and a would be append
with open("../../../desktop/my_file.txt", mode="w") as file:
    file.write("I found the file and wrote this in it.")