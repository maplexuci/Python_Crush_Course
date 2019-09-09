print("This is an anonymous poll for the reasons people"
      "like programming.\nEnter 'q' at any time to quite")
filename = 'programming_poll.txt'
while True:
    answers = input("\nPlease provide your reasons why you like programming:"
                    "\n")
    if answers == 'q':
        break
    print("\nThanks for taking this poll!\n")

    with open(filename, 'a') as file_object:
        file_object.write(answers.capitalize() + "\n")
