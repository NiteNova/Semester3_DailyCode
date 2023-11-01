import random

class LootStack:
    def __init__(self):
        self.lootnames = []
        self.loot = {"Potions": 0, "Weapons": 0, "Misc": 0}
        self.max = 10
    
    def is_empty(self):
        return len(self.loot) == 0 
    
    def push_loot(self, item):
        if len(self.loot) <= self.max:
            print(f"Acquired {item}!")
            self.lootnames.append(item)
            for k in item:
                if "potion" in k:
                    self.loot["Potions"] += 1
                elif "sword" in k or "bow" in k or "dagger" in k:
                    self.loot["Weapons"] += 1
                elif "":
                    self.loot["Misc"] += 1
        else:
            print(f"Sir you are carrying too dang much, GUH!")

    def pop_loot(self, removed_item):
        if not self.is_empty():
            for k in removed_item:
                if "potion" in k:
                    self.loot["Potions"] -= 1
                elif "sword" in k or "bow" in k or "dagger" in k:
                    self.loot["Weapons"] -= 1
                else:
                    print("Either that is misc or does not exist in your bag")
            print(f"Used {removed_item}.")
        else:
            print("Your loot bag is empty!")
    def random_loot(self):
        if not self.is_empty() and len(self.lootnames) <= self.max:
            for i in random.randrange(1, 101):
                if i >= 25:
                    print("Health Potion") 
                    self.lootnames.append("Health Potion")
                    self.loot["Potions"] += 1
                elif i >= 50:
                    print("Iron shield") 
                    self.lootnames.append("Iron Shield")
                    self.loot["Misc"] += 1
                elif i >= 75: 
                    print("Throwing Daggers") 
                    self.lootnames.append("Throwing DAggers")
                    self.loot["Weapons"] += 1
                else:
                    print("Crossbow")
                    self.lootnames.append("Crossbow")
                    self.loot["Weapons"] += 1 
           
    def peek_loot(self):
        if not self.is_empty():
            return self.lootnames[-1]
        else:
            print("Your loot bag is empty!")
    def all_loot(self):
        if not self.is_empty():
            print(self.lootnames)
        else:
            print("You aint nothing in da bag")
    def quantity_loot(self):
        if not self.is_empty():
            print(self.loot)
        else:
            print("You aint nothing in da bag")


# Initialize LootStack object
player_loot = LootStack()

# Simple game loop for interaction
while True:
    print("\n=== Loot Bag Menu ===")
    print("1: Acquire new loot")
    print("2: Use loot")
    print("3: Check top loot item")
    print("4: Get a random item in your inventory")
    print("5: Check your entire loot bag and quantities")
    print("6: Exit")
    choice = input("What would you like to do? ")

    if choice == '1': #Acquire new loot
        new_loot = input("Enter the name of the loot item you acquired: ")
        player_loot.push_loot(new_loot)
    elif choice == '2': #Remove items
        removed = input("What do you want to remove?: ")
        player_loot.pop_loot(removed)
    elif choice == '3': #Check your loot bag
        top_loot = player_loot.peek_loot()
        if top_loot:
            print(f"The top loot item is: {top_loot}")
    elif choice == '4': # Get Random Lot
        player_loot.random_loot
    elif choice == '5': # Check your entire loot bag
        player_loot.all_loot
        player_loot.quantity_loot
    elif choice == '6': #Exit the loop
        print("Exiting. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
