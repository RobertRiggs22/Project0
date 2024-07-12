import os
import json
import Player as pl
import Enemy as en

#user input
#name = input("What is your name?\n")
#print("Your name is " + name)

player = pl.Player(5, 10, ["fire", "water", "earth"])
player.inventory.append(["Potion", 3])
enemy1 = en.Enemy(2, 10, "left")
enemy2 = en.Enemy(2, 10, "middle")
enemy3 = en.Enemy(2, 10, "right")

print("As you embark on your journey, you recall that fire beats earth, earth beats water, and water beats fire.")

while enemy1.health > 0 or enemy2.health > 0 or enemy3.health > 0:
    
    #writing to file
    with open("player.json", "w") as file:
        json.dump(player.giveDict(), file)
    with open("enemy1.json", "w") as file:
        json.dump(enemy1.giveDict(), file)
    with open("enemy2.json", "w") as file:
        json.dump(enemy2.giveDict(), file)
    with open("enemy3.json", "w") as file:
        json.dump(enemy3.giveDict(), file)

    #read from file
    with open("player.json", "r") as file:
        playerJsonObj = json.load(file)
    with open("enemy1.json", "r") as file:
        enemy1JsonObj = json.load(file)
    with open("enemy2.json", "r") as file:
        enemy2JsonObj = json.load(file)
    with open("enemy3.json", "r") as file:
        enemy3JsonObj = json.load(file)

    #player info
    print("You currently have {} health left.".format(playerJsonObj["health"]))
    
    #monster info
    if (enemy1JsonObj["health"] > 0):
        print("There is a earth monster on your left!")
    if (enemy2JsonObj["health"] > 0):
        print("There is a fire monster in front of you!")
    if (enemy3JsonObj["health"] > 0):
        print("There is a water monster on your right!")

    #player attack options
    target = input("Which enemy would you like to target?\n[1] Left\n[2] Middle\n[3] Right\n[4] Inventory\n")

    if target == "1" or target == "2" or target == "3":
        
        spell = input("Which spell would you like to use?\n[1] Fire\n[2] Water\n[3] Earth\n")

        if spell == "1" or spell == "2" or spell == "3":
            
            #player attack
            spellStr = player.castSpellByIndex(int(spell))

            match int(target):
                case 1:
                    if spellStr == "fire":
                        enemy1.health -= (playerJsonObj["damage"] * 2)
                        print("Dealt {} damage!".format(playerJsonObj["damage"] * 2))
                    else:
                        enemy1.health -= playerJsonObj["damage"]
                        print("Dealt {} damage!".format(playerJsonObj["damage"]))
                case 2:
                    if spellStr == "water":
                        enemy2.health -= (playerJsonObj["damage"] * 2)
                        print("Dealt {} damage!".format(playerJsonObj["damage"] * 2))
                    else:
                        enemy2.health -= playerJsonObj["damage"]
                        print("Dealt {} damage!".format(playerJsonObj["damage"]))
                case 3:
                    if spellStr == "earth":
                        enemy3.health -= (playerJsonObj["damage"] * 2)
                        print("Dealt {} damage!".format(playerJsonObj["damage"] * 2))
                    else:
                        enemy3.health -= playerJsonObj["damage"]
                        print("Dealt {} damage!".format(playerJsonObj["damage"]))

            #enemy attack
            if enemy1.health > 0:
                player.health -= enemy1JsonObj["damage"]
                print("Took {} damage!".format(enemy1JsonObj["damage"]))
            if enemy2.health > 0:
                player.health -= enemy1JsonObj["damage"]
                print("Took {} damage!".format(enemy1JsonObj["damage"]))
            if enemy3.health > 0:
                player.health -= enemy1JsonObj["damage"]
                print("Took {} damage!".format(enemy1JsonObj["damage"]))

            if player.health < 0:
                print("YOU LOSE")
                break

        else:
            print("Invalid Spell. Try Again.")
    elif target == "4":
        count = player.printInventory()
        item = input("[" + str(count) + "] Close\nPress the number of the above item would you like to use.\n")

        item = int(item)

        if item > 0 and item <= count:
            if item != count:
                match player.inventory[item - 1][0]:
                    case "Potion":
                        player.usePotion()
        else:
            print("Invalid Item. Try Again.")
    else:
        print("Invalid Target. Try Again.")

    #writing to file
    with open("player.json", "w") as file:
        json.dump(player.giveDict(), file)
    with open("enemy1.json", "w") as file:
        json.dump(enemy1.giveDict(), file)
    with open("enemy2.json", "w") as file:
        json.dump(enemy2.giveDict(), file)
    with open("enemy3.json", "w") as file:
        json.dump(enemy3.giveDict(), file)

    print("End of Round\n")

print("You defeated all the monsters! Congratulations!")