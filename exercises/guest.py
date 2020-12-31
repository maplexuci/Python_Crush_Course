filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(input(
        "Please input your name, in a 'Last Name, First Name' format: ")
        + "\n")

with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
