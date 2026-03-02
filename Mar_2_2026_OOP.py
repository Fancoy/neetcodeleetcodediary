class SmartDevice:
    # Add your class attributes here
    total_devices = 0
    active_devices = 0
    def __init__(self, name: str):
        self.name = name
        SmartDevice.total_devices += 1  # Each new device adds to total
        
    # Implement these methods
    def turn_on(self) -> None:
        SmartDevice.active_devices += 1
        
    def turn_off(self) -> None:
        SmartDevice.active_devices -= 1



# Don't change anything below this line
tv = SmartDevice("TV")
lights = SmartDevice("Lights")

# Control devices
tv.turn_on()
lights.turn_on()
tv.turn_off()

print(f"Total Devices: {SmartDevice.total_devices}")    # Shows 2
print(f"Active Devices: {SmartDevice.active_devices}")  # Shows 1


class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0


    
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance


# TODO: Create two accounts
Alice = BankAccount("Alice", 1000)
Bob = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${Alice.balance}")
print(f"Bob's balance: ${Bob.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: {BankAccount.total_balance}")