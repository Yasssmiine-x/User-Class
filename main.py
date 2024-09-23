class User:
    def _init_(self, name, age, location):
        
        self.__name = name
        self.__age = age
        self.__location = location

    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_location(self):
        return self.__location

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_location(self, location):
        self.__location = location

user1 = User("Bello", 10, "Spain")
user2 = User("Nike", 30, "Itlay")
user3 = User("Zee", 22, "Canada")

print(f"User1: Name = {user1.get_name()}, Age = {user1.get_age()}, Location = {user1.get_location()}")
print(f"User2: Name = {user2.get_name()}, Age = {user2.get_age()}, Location = {user2.get_location()}")
print(f"User3: Name = {user3.get_name()}, Age = {user3.get_age()}, Location = {user3.get_location()}")

# Changing the values
user1.set_name("Zeezy")
user1.set_age(21)
user1.set_location("Edo")

user2.set_name("Yasss")
user2.set_age(15)
user2.set_location("Kano")

user3.set_name("Yasssmiine")
user3.set_age(23)
user3.set_location("Zaria")


print(f"Updated User1: Name = {user1.get_name()}, Age = {user1.get_age()}, Location = {user1.get_location()}")
print(f"Updated User2: Name = {user2.get_name()}, Age = {user2.get_age()}, Location = {user2.get_location()}")
print(f"Updated User3: Name = {user3.get_name()}, Age = {user3.get_age()}, Location = {user3.get_location()}")
