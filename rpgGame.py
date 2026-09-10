import random


#Start the game by printing a welcome message
print("Hello! Welcome to the RPG Game!")

#Ask the player for their name and welcome them to the game
name = input("Please enter your character's name: ")
print(f"\nWelcome, {name}! Your adventure begins now.")

# make the player a dictionary to hold their stats and position
player = {
    "name": name,
    "level": 1,
    "health": 10,
    "x": 0,
    "y": 0,
    "gold": 0,
    "damage": 0
}

player["damage"] = random.randint(1, 3)


#add an enemy to the game
enemy = {
    "name": "Goblin",
    "level": 1,
    "health": 5,
    "x": 2,
    "y": 2,
    "gold": 5
}


#npc the player can buy sowrds from 
npc = {
    "name": "Blacksmith",
    "x": 1,
    "y": 1,
    "sword_price": 10,
    "sword_damage": 5
}

#Set the game to running
running = True


if __name__ == "__main__":
    while running:
          
         #Display the player's current stats and position
        print(f"\n{name}'s Stats: Level {player['level']}, Health {player['health']}, Gold {player['gold']}, Position ({player['x']}, {player['y']})")

        #upgrade the player's level if they have enough gold
        if player["gold"] >= 5:
            print(f"\n{name} has enough gold to upgrade their level!")
            print(f"\nwould you like to upgrade your level? (yes/no) upgrading will cost 5 gold and increase your Max health and damage by 5 points.")
            upgrade = input().lower()

            if upgrade == "yes":
                player["level"] += 1
                player["gold"] -= 5
                player["health"] += 5
                player["damage"] += 5
                print(f"\n{name} upgrades their level to {player['level']} and gained 5 max health and damage points! Current health: {player['health']}, Gold: {player['gold']}")
            elif upgrade == "no":
                print(f"{name} decides not to upgrade their level. Current health: {player['health']}, Gold: {player['gold']}")
            else:
                print(f"Invalid input. Please choose yes or no. Current health: {player['health']}, Gold: {player['gold']}")

        #Ask the player for their next action
        action = input(f"\nWhat would you like to do? (move, rest, exit): ").lower()
        
        if action == "move":
            direction = input("Which direction would you like to move? (north, south, east, west): ").lower()
            if direction == "north":
                northText = random.choice([f"\nYou move north and find a peaceful meadow.", f"\nYou move north and encounter a wild animal.", f"\nYou move north and discover a hidden treasure."])
                print(northText)
                player["y"] += 1
            elif direction == "south":
                southText = random.choice([f"\nYou move south and find a dark cave.", f"\nYou move south and encounter a band of thieves.", f"\nYou move south and discover an ancient ruin."])
                print(southText)
                player["y"] -= 1
            elif direction == "east":
                eastText = random.choice([f"\nYou move east and find a sparkling river.", f"\nYou move east and encounter a wandering merchant.", f"\nYou move east and discover a hidden village."])
                print(eastText)
                player["x"] += 1
            elif direction == "west":
                westText = random.choice([f"\nYou move west and find a mysterious forest.", f"\nYou move west and encounter a friendly traveler.", f"\nYou move west and discover a abandoned cabin."])
                print(westText)
                player["x"] -= 1
            else:
                print("Invalid direction. Please choose north, south, east, or west.")
        elif action == "rest":
            player["health"] += 1
            print(f"{name} rests and recovers some health. Current health: {player['health']}")
        elif action == "exit":
            running = False
            print("Exiting the game. Goodbye!")
        else:
            print("Invalid action. Please choose move, rest, or exit.")



        #Check if the player has encountered the enemy
    

        if player["x"] == enemy["x"] and player["y"] == enemy["y"] and enemy["health"] > 0 and running == True:
            print(f"\nA wild {enemy['name']} appears!")
            while enemy["health"] > 0 and player["health"] > 0:
                attack = input(f"\nDo you want to attack or run? (attack, run): ").lower()
                if attack == "attack":
                    damage = random.randint(1, player["damage"])
                    enemy["health"] -= damage
                    print(f"\nYou attack the {enemy['name']} for {damage} damage. Enemy health: {enemy['health']}")
                    if enemy["health"] <= 0:
                        print(f"\nYou have defeated the {enemy['name']}!")
                        print(f"You found {enemy['gold']} Gold on the {enemy['name']}.")
                        player["gold"] += enemy["gold"]
                        break
                    enemy_damage = random.randint(1, 2)
                    player["health"] -= enemy_damage
                    print(f"The {enemy['name']} attacks you for {enemy_damage} damage. Your health: {player['health']}")
                    if player["health"] <= 0:
                        print(f"\nYou have been defeated! Game over.")
                        running = False
                        break
                elif attack == "run":
                    print(f"\nYou run away from the battle.")
                    break
                else:
                    print("Invalid action. Please choose attack or run.")
        

        #Check if the player has encountered the npc
        if player["x"] == npc["x"] and player["y"] == npc["y"] and running == True:
            print(f"\nYou encounter the {npc['name']}.")
            print(f"The {npc['name']} offers to sell you a sword for {npc['sword_price']} Gold. The sword will increase your damage by {npc['sword_damage']} points.")
            buy_sword = input("Would you like to buy the sword? (yes/no): ").lower()
            if buy_sword == "yes":
                if player["gold"] >= npc["sword_price"]:
                    player["gold"] -= npc["sword_price"]
                    player["damage"] += npc["sword_damage"]
                    print(f"\nYou bought the sword! Your damage has increased to {player['damage']}. Current gold: {player['gold']}")
                else:
                    print(f"\nYou don't have enough gold to buy the sword. Current gold: {player['gold']}")
            elif buy_sword == "no":
                print(f"\nYou decide not to buy the sword. Current gold: {player['gold']}")
            else:
                print("Invalid input. Please choose yes or no.")
        


     
            

