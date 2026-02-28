class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species




# Do not modify below this line
my_pet = Pet("Fluffy", "cat")
print(f"My pet is a {my_pet.species} named {my_pet.name}")


class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

# Don't modify the above code

# TODO: Create a pet named "Whiskers" that is a species of 'cat' with hunger level 6 and energy level 8
whiskers = Pet("Whiskers", "cat", 6, 8)

# Don't modify the following code
print(f"{whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}") 


class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2
whiskers.hunger -= 3
whiskers.energy += 2

# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()


class SuperHero:
    def __init__(self, name: str, power: str, strength: int):
        self.name = name
        self.power = power
        self.strength = strength
    
    def power_boost(self, strength_increase) -> None:
        self.strength += strength_increase
        print(f"{self.name}'s strength increased to {self.strength}!")



# Don't modify the following code
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

ironman.power_boost(15)


class Pet:
    # TODO: Implement the __init__ method here
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age



# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")


class Pet:
    """A class to represent a pet.

    Attributes:
        name (str): The pet's name
        animal_type (str): The pet's type
    """
    def __init__(self, name: str, animal_type: str):
        """Initialize a new Pet instance."""
        self.name = name
        self.animal_type = animal_type

    def make_sound(self) -> str:
        """Return the sound the pet makes based on its type."""
        if self.animal_type == "dog":
            return "Woof!"
        elif self.animal_type == "cat":
            return "Meow!"
        else:
            return "Unknown sound"

# Don't change the following code
print(Pet.__doc__)
print(Pet.__init__.__doc__)
print(Pet.make_sound.__doc__)

class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
        


# TODO: Create Superhero instances
hero1 = SuperHero("Batman", "Intelligence", 100)
hero2 = SuperHero("Superman", "Strength", 150)


# TODO: Print out the attributes of each superhero
print(f"{hero1.name}\n{hero1.power}\n{hero1.health}")
print(f"{hero2.name}\n{hero2.power}\n{hero2.health}")

class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    

    # TODO: Define attack method and implement it
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    # TODO: Define heal method and implment it
    def heal(self):
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")

# TODO: Create superhero instance
hero1 = SuperHero("Catwoman", "Agility", 120)

# TODO: Use the attack() and heal() method
hero1.attack()
hero1.heal()

