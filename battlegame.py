# File Name: MonsterBattleArena
# This is a game that allows a user to choose a character and battle a monster of their choosing.
# This includes if statements, while loops, input, and printing.

from random import randint
from tkinter import scrolledtext

print('''

.___  ___.   ______   .__   __.      _______.___________. _______ .______         .______        ___   .___________.___________. __       _______         ___      .______       _______ .__   __.      ___      
|   \/   |  /  __  \  |  \ |  |     /       |           ||   ____||   _  \        |   _  \      /   \  |           |           ||  |     |   ____|       /   \     |   _  \     |   ____||  \ |  |     /   \     
|  \  /  | |  |  |  | |   \|  |    |   (----`---|  |----`|  |__   |  |_)  |       |  |_)  |    /  ^  \ `---|  |----`---|  |----`|  |     |  |__         /  ^  \    |  |_)  |    |  |__   |   \|  |    /  ^  \    
|  |\/|  | |  |  |  | |  . `  |     \   \       |  |     |   __|  |      /        |   _  <    /  /_\  \    |  |        |  |     |  |     |   __|       /  /_\  \   |      /     |   __|  |  . `  |   /  /_\  \   
|  |  |  | |  `--'  | |  |\   | .----)   |      |  |     |  |____ |  |\  \----.   |  |_)  |  /  _____  \   |  |        |  |     |  `----.|  |____     /  _____  \  |  |\  \----.|  |____ |  |\   |  /  _____  \  
|__|  |__|  \______/  |__| \__| |_______/       |__|     |_______|| _| `._____|   |______/  /__/     \__\  |__|        |__|     |_______||_______|   /__/     \__\ | _| `._____||_______||__| \__| /__/     \__\ 
                                                                                                                                                                                                                 
''')

while True:

    # create characters with stats
    orc = "Orc"
    orcHp = 200

    elf = "Elf"
    elfHp = 100

    human = "Human"
    humanHp = 150

    # create monsters with stats
    wyvern = "Wyvern"
    wyvernHp = 300
    wyvernDMG = 200

    gryphon = "Gryphon"
    gryphonHp = 250
    grphonDMG = 150

    centaur = "Centaur"
    centaurHp = 200
    centaurDMG = 100

    # create weapons and magic with stats
    swordAndShield = "Sword and Shield"
    swordAndShieldDMG = 100

    spear = "Spear"
    spearDMG = 120

    axe = "Axe"
    axeDMG = 110

    bowAndArrow = "Bow and Arrow"
    bowAndArrowDMG = 90

    sorcery = "Sorcery"
    sorceryDMG = 130

    # ask for input for character choice, and assign attributes to user based on character
    while True:

        print(f"\nMonster Battle Arena\n")

        print(f"Characters: | {orc} | {elf} | {human} |")
        playerCharacter = input("Choose your fighter: ")

        if playerCharacter == orc:
            myHp = orcHp

        elif playerCharacter == human:
            myHp = humanHp

        elif playerCharacter == elf:
            myHp = elfHp

        else:
            print("\nNo correct character was chosen or name was misspelled.\n")
            continue

        # ask for weapon class choice
        print(
            f"\nWeapon Classes: | {swordAndShield} | {spear} | {axe} | {bowAndArrow} | {sorcery} |")
        weaponClass = input("What weapon class will you use? ")

        if weaponClass == swordAndShield:
            myDMG = swordAndShieldDMG
        elif weaponClass == spear:
            myDMG = spearDMG
        elif weaponClass == axe:
            myDMG = axeDMG
        elif weaponClass == bowAndArrow:
            myDMG = sorcery
        else:
            print("\nNo correct weapon choice was entered or name was misspelled.\n")
            continue

        # ask what monster to fight
        print("What monster will you fight? ")
        print("\nThe Wyvern?")
        print('''
        \****__              ____                                              
         |    *****\_      --/ *\-__                                          
         /_          (_    ./ ,/----'                                         
            \__         (_./  /                                                
               \__           \___----^__                                       
               _/   _                  \                                      
        |    _/  __/ )\"\ _____         *\                                    
        |\__/   /    ^ ^       \____      )                                   
         \___--"                    \_____ )                                  
                                          "
            \n''')

        print("\nThe Gryphon?")
        print('''
                                    ______
                    ______,---'__,---'
                _,-'---_---__,---'
        /_    (,  ---____',
        /  ',,   `, ,-'
        ;/)   ,',,_/,'
        | /\   ,.'//\\
        `-` \ ,,'    `.
            `',   ,-- `.
            '/ / |      `,         _
            //'',.\_    .\\      ,{==>-
        __//   __;_`-  \ `;.__,;'
        ((,--,) (((,------;  `--' 
            \n''')

        print("Or the Centaur?")
        print('''
         <--------]}-------
            --.   /|
           _\"/_.'/
         .'._._,.'
         :/ \\//
        (L  /--',----._
           |          \\
         : /-\ .'-'\ / |
          \\, ||    \|
           \/ ||    || 
            \n''')

        enemy = input(f"Enter your choice: ")

        if enemy == wyvern:
            enemyHp = wyvernHp
            enemyDMG = wyvernDMG
            break

        elif enemy == gryphon:
            enemyHp = gryphonHp
            enemyDMG = grphonDMG
            break

        elif enemy == centaur:
            enemyHp = centaurHp
            enemyDMG = centaurDMG
            break
        else:
            print("\nNo correct monster was entered or name was misspelled.\n")
            continue

    # print character chosen, HP, and DMG
    print(f"\nGreat selection. Your character is {playerCharacter}")
    print(f"Your {playerCharacter}'s health is: {myHp}")
    print(
        f"Your {playerCharacter}'s weapon is: {weaponClass} and has {myDMG} damage.\n")

    # print the battle according to stats that have been assigned until dragon or player dies

    # announce event
    print(f"\nTodays event will be a battle against a {enemy}!\n")
    print(f"\nOur fighter is {playerCharacter}!\n")
    print(F"\nThey will be facing the undefeated {enemy}\n")
    print(f"\n{playerCharacter} enters the arena and the crowd begins to cheer!")

    while True:

        # player attack
        realMyDMG = randint(0, myDMG)
        print(f"{playerCharacter} attacks for {realMyDMG}.")
        print(f"{enemy}'s health is {enemyHp} and takes {realMyDMG}")
        enemyHp -= realMyDMG
        if enemyHp < 0:
            print(f"\n{playerCharacter} performed a fatal attack!\n")
            enemyHp == 0
            break
        print(f"{enemy}'s health is now at: {enemyHp}\n")

        input("\nPRESS ENTER TO CONTINUE...\n")

        # enemy death
        if enemyHp <= 0:
            print(f"\n{playerCharacter} has defeated the {enemy}\n")
            print("\nThe crowd goes wild!\n")
            break

        # wyvern attack
        realEnemyDMG = randint(0, enemyDMG)
        print(f"\n{enemy} attacks for {realEnemyDMG}")
        print(f"{playerCharacter}'s health is {myHp} and takes {realEnemyDMG}")
        myHp -= realEnemyDMG
        # player death
        if myHp <= 0:
            print(f"\n{enemy} massacred the {playerCharacter}\n")
            print(f"The {enemy} remains undefeated!\n")
            myHp == 0
            break

        print(f"{playerCharacter} is now at: {myHp}\n")

        input("\nPRESS ENTER TO CONTINUE...\n")

    # end game
    print("\nYour game has ended...\n")
    newGame = input("\nWould you like to play again? \n")

    # yes/no to restart game
    if newGame[0].lower() == "n":
        break

# say goodbye
print("\nGoodbye and thanks for all the fish.\n")
