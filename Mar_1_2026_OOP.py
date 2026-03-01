class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


chips = StoreItem("Chips", 1.99) # Don't modify this line

# TODO: Access the attributes of the chips object and display them
print(chips.name)
print(chips.price)



class Account:
    def __init__(self, title, _balance):
        self.title = title
        self._balance = _balance
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()


class PasswordManager:
    def __init__(self, __password):
        self.__password = __password
    
    # TODO: Implement the verify_password method
    def verify_password(self, password):
        if self.__password == password:
            return True
        return False



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False


class BankAccount:
    def __init__(self, balance: int):
        self.__balance = balance
    
    def get_balance(self) -> int:
        return self.__balance


    # TODO: Add setter method for balance
    def set_balance(self, new_balance: int) -> None:
        if(new_balance < 0):
            print("Cannot set negative balance!")
            return
        self.__balance = new_balance





# Don't modify the code below this line
account = BankAccount(1000)
print(account.get_balance())
account.set_balance(-100)
print(account.get_balance())
account.set_balance(100)
print(account.get_balance())
account.set_balance(0)
print(account.get_balance())


class BankAccount:
    def __init__(self, balance: int): 
        self.__balance = balance # Don't modify this line
        
    @property
    def balance(self) -> int: # TODO: Convert this method to use the @property decorator
        return self.__balance
    
    @balance.setter
    def balance(self, value: int) -> None: # TODO: Convert this method to use the @property decorator
        if value >= 0:
            self.__balance = value
        else:
            print("Balance cannot be negative!")


# Don't modify the code below this line
account = BankAccount(1000)
print(account.balance)
account.balance = -100


class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    # TODO: Add the getter and setter methods
    def get_health(self):
        return self.__health

    def get_power_level(self):
        return self.__power_level

    def set_health(self, health: int) -> None:
        if health > 100:
            print("You can't set the health to more than 100")
            return
        elif health < 0:
            print("You can't set the health to less than 0")
            return
        self.__health = health
    
    def set_power_level(self, power_level):
        if power_level > 10:
            print("You can't set the power level to more than 10")
            return
        elif power_level < 1:
            print("You can't set the power level to less than 1")
            return
        self.__power_level = power_level


super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to less than 100
super_hero.set_health(70)

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7)


# TODO: print the hero's attributes
print(f"{super_hero.name} has {super_hero.get_health()} health and {super_hero.get_power_level()} power level")


class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level
    
    @property
    def health(self):
        return self.__health

    @property
    def power_level(self):
        return self.__power_level
    
    @health.setter
    def health(self, healthNew):
        if healthNew > 100:
            print("You can't set the health to more than 100")
            return
        elif healthNew < 0:
            print("You can't set the health to less than 0")
            return
        self.__health = healthNew

    @power_level.setter
    def power_level(self, new_power):
        if new_power > 10:
            print("You can't set the power level to more than 10")
            return
        elif new_power < 1:
            print("You can't set the power level to less than 1")
            return
        self.__power_level = new_power
    # TODO: Add the getter and setter methods
    # Remember to use the @property decorator for the getter methods
    # Remember to use the @setter decorator for the setter methods


# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health) # this should print 80
super_hero.health = 110 # this should print You can't set the health to more than 100

print(super_hero.power_level) # this should print 9
super_hero.power_level = 100 # this should print You can't set the power level to more than 10
super_hero.power_level = 0 # this should print You can't set the power level to less than 1


# TODO: print the hero's attributes 
print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")

# @property makes both getting and setting look like normal attribute access, while still running your validation logic behind the scenes.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        length = 0
        temp = x
        temp2 = x
        a = 0
        while temp > 0:
            temp = temp // 10
            length += 1
        while length  > 0:
            a = (a) + (x % 10) * (pow(10, length - 1))
            x = x // 10
            length -= 1
        if a == temp2:
            return True
        return False


        