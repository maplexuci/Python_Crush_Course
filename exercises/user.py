class User():

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("\nFirst Name: " + self.first_name.title())
        print("Last Name: " + self.last_name.title())
        print("Gender: " + self.gender.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " +
              self.last_name.title() + ", It's a pleasure to meet you!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        if self.login_attempts == 1:
            print("This is your 1st attempt, you have 4 attempts left!")
        elif self.login_attempts == 2:
            print("This is your 2nd attempt, you have 3 attempts left!")
        elif self.login_attempts == 3:
            print("This is your 3rd attempt, you have 2 attempts left!")
        elif self.login_attempts == 4:
            print("This is your 4th attempt, you have 1 attempts left!")
        elif self.login_attempts == 5:
            print("This is your 5th attempt, you are locked out!")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Your login attempts have been reset. Your login attempt is " +
              str(self.login_attempts) + ", now you have 5 attempts!")


class Admin(User):

    def __init__(self, first_name, last_name, gender, age):
        super().__init__(first_name, last_name, gender, age)
        self.privileges = ['can add post', 'can delete post',
                           'can add user', 'can ban user']

    def show_privileges(self):
        print("The Admin has the following privileges:")
        for privilege in self.privileges:
            print(privilege + "\n")


class Privileges():

    def __init__(self):
        self.privileges = ['can add post', 'can delete post',
                           'can add user', 'can ban user']
        self.admin = Admin('peter', 'parker', 'male', '18')

    def show_privileges(self):
        print("The Admin " + self.admin.first_name.title() + " " +
              self.admin.last_name.title() + " has the following privileges:")
        for privilege in self.privileges:
            print(privilege + "\n")


admin_main = Privileges()
admin_main.show_privileges()

admin = Admin('peter', 'parker', 'male', '18')
admin.show_privileges()

user_1 = User('Alice', 'Mose', 'Female', 23)
user_2 = User('matt', 'armstrong', 'male', 26)
user_3 = User('victoria', 'lesy', 'female', 22)
user_4 = User('John', 'singer', 'male', 25)

user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()
user_3.describe_user()
user_3.greet_user()
user_4.describe_user()
user_4.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
print("Current attempt: " + str(user_1.login_attempts))
