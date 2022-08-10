#FileNOtFound
# with open("a_file.txt") as file:
#     file.read()
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError: #You want to put the exception that you are trying to find just incase there is
                         # more then one exception that could be thrown by the try block
    file = open("a_file.txt", "w")
    file.write("Print something in file")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else: #this code will excecute if there is no exceptions
    content = file.read()
    print(content)
finally:# This code will run no matter what happens
    file.close()
    print("File was closed")


#keyError
# a_dictionary = {"key":"value"}
# value = a_dictionary["non_existent_key"]

#IndexError
# fruit_list = ["Apple", "Banana", "Orange"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text + 5)