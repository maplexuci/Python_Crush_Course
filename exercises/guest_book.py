filename = 'guest_book.txt'
print("Enter 'q' at anytime when you want to quit.")

while True:
    guest_name = input(
        "\nPlease input your name, in a 'FirstName LastName' format: ")
    if guest_name == 'q':
        break
    print("Welcome here, " + guest_name.title())

    with open(filename, 'a') as file_object:
        file_object.write(guest_name.title() + "\n")
