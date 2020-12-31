class Restaurant():

    def __init__(self, name, type):
        self.restaurant_name = name
        self.cuisine_type = type
        self.number_served = 0

    def describe_restaurant(self):
        print("\nRestaurant " + self.restaurant_name + "'s cuisine type is "
              + self.cuisine_type + "!")

    def open_restaurant(self):
        print("The Restaurant " + self.restaurant_name + " is now opening!")

    def set_number_served(self, serve_number):
        self.number_served = serve_number
        print("The restaurant " + self.restaurant_name + " has served " +
              str(serve_number) + " people!")

    def increment_number_served(self, increase):
        self.number_served += increase
        print("This restaurant currently served " + str(self.number_served) +
              " people!")


class IceCreamStand(Restaurant):

    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.flavors = ['chocolate', 'vanila', 'mint', 'nut', 'strawberry']

    def display_flavors(self):
        print(self.name + "'s icecream has the fowlloing flavors:" + "\n")
        for flavor in self.flavors:
            print(flavor + "\n")


icecreamstand = IceCreamStand('Boat House', 'Icecreame')
icecreamstand.display_flavors()

restaurant = Restaurant('Ancient Flavor', 'Chinese Food')
print("Restaurant's name is: " + restaurant.restaurant_name)
print("Restaurant's cuisine type is: " + restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("This restaurant has served " + str(restaurant.number_served)
      + " people!")
restaurant.set_number_served(43)
restaurant.increment_number_served(28)

restaurant_1 = Restaurant('Skyline', 'Sushi')
restaruant_2 = Restaurant('Great Patsta', 'Italian')

restaurant.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_1.set_number_served(29)
restaruant_2.describe_restaurant()
