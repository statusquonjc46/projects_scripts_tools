#! /usr/bin/python3
# Simple Warhammer Fantasy Role Play Character Generator
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import random
import time

print("""
Part 0: Welcome Prompt
-------------------------------------------------------------------------------------
- Welcome to the Warhammer Fantasy RolePlay(WFRP) game character generator.
- Everything you find in this script is from the 4th edition of WFRP.
- If you would like to follow along with the prompts,
- I will try to accurately label each prompt with its corresponding page in the book.
- Enjoy, and may the d100 be with you.
-------------------------------------------------------------------------------------""")
time.sleep(3)

def randomSpecies():
    print("""
Part 1: Species
--------------------------------------------------------
- First we are going to roll for your species.
- This is done with a d100.
- Human falls in the range of 1-90.
- Halfling falls in the range of 91-94.
- Dwarf falls in the range of 95-98.
- High Elf is 99.
- Wood Elf is 100.
- This can be found on page 24 of the 4th Edition Guide.
--------------------------------------------------------""")

    d100 = random.randint(1, 100)
    if d100 > 0 and d100 < 91:
        return d100, 'Human (Reiklander)'
    elif d100 > 90 and d100 < 95:
        return d100, 'Halfling'
    elif d100 > 94 and d100 < 99:
        return d100, 'Dwarf'
    elif d100 == 99:
        return d100, 'High Elf'
    elif d100 == 100:
        return d100, 'Wood Elf'

def randomClass(species):
    firstRoll = species[0]
    species = species[1]
    specClass = ''
    career = ''

    # Dictionaries for each class for each species containing rolls for each career.
    # Human Class dictionary that contains careers as each key. Then the value for each key is a list of rolls that decides the career.
    humanAcademic = {'Apothecary': [1], 'Engineer': [2], 'Lawyer': [3], 'Nun': [4, 5], 'Physcian': [6], 'Priest': [7, 8, 9, 10, 11], 'Scholar': [12, 13], 'Wizard': [14]}
    humanBurgher = {'Agitator': [15], 'Artisan': [16, 17], 'Beggar': [18, 19], 'Investigator': [20], 'Merchant': [21], 'Rat Catcher': [22, 23], 'Townsman': [24, 25, 26], 'Watchman': [27]}
    humanCourtier = {'Advisor': [28], 'Artist': [29], 'Duelist': [30], 'Envoy': [31], 'Noble': [32], 'Servant': [33, 34, 35], 'Spy': [36], 'Warden': [37]}
    humanPeasant = {'Bailiff': [38], 'Hedge Witch': [39], 'Herbalist': [40], 'Hunter': [41, 42], 'Miner': [43], 'Mystic': [44], 'Scout': [45], 'Villager': [46, 47, 48, 49, 50]}
    humanRanger = {'Bounty Hunter': [51], 'Coachman': [52], 'Entertainer': [53, 54], 'Flagellant': [55, 56], 'Messenger': [57], 'Pedlar': [58], 'Road Warden': [59], 'Witch Huner': [60]}
    humanRiverfolk = {'Boatman': [61, 62], 'Huffer': [63], 'Riverwarden': [64, 65], 'Riverwoman': [66, 67, 68], 'Seaman': [69, 70], 'Smuggler': [71], 'Stevedore': [72, 73], 'Wrecker': [74]}
    humanRogue = {'Bawd': [75, 76], 'Charlatan': [77], 'Fence': [78], 'Grave Robber': [79], 'Outlaw': [80, 81, 82, 83], 'Racketeer': [84], 'Thief': [85, 86, 87], 'Witch': [88]}
    humanWarrior = {'Cavalryman': [89, 90], 'Guard': [91, 92], 'Knight': [93], 'Pit Fighter': [94], 'Protagonist': [95], 'Soldier': [96, 97, 98, 99], 'Slayer': [], 'Warrior Priest': [100]}

    # Dwarf Class dictionary that contains careers as each key. Then the value for each key is a list of rolls that decides the career.
    dwarfAcademic = {'Apothecary': [1], 'Engineer': [2, 3, 4], 'Lawyer': [5, 6], 'Nun': [], 'Physcian': [7], 'Priest': [], 'Scholar': [8, 9], 'Wizard': []}
    dwarfBurgher = {'Agitator': [10, 11], 'Artisan': [12, 13, 14, 15, 16, 17], 'Beggar': [18], 'Investigator': [19, 20], 'Merchant': [21, 22, 23, 24], 'Rat Catcher': [25], 'Townsman': [26, 27, 28, 29, 30, 31], 'Watchman': [32, 33, 34]}
    dwarfCourtier = {'Advisor': [35, 36], 'Artist': [37], 'Duelist': [38], 'Envoy': [39, 40], 'Noble': [41], 'Servant': [42], 'Spy': [43], 'Warden': [44, 45]}
    dwarfPeasant = {'Bailiff': [46, 47], 'Hedge Witch': [], 'Herbalist': [], 'Hunter': [48, 49], 'Miner': [50, 51, 52, 53, 54], 'Mystic': [], 'Scout': [55], 'Villager': [56]}
    dwarfRanger = {'Bounty Hunter': [57, 58, 59, 60], 'Coachman': [61], 'Entertainer': [62, 63], 'Flagellant': [], 'Messenger': [64, 65], 'Pedlar': [66, 67], 'Road Warden': [], 'Witch Huner': []}
    dwarfRiverfolk = {'Boatman': [68, 69], 'Huffer': [70], 'Riverwarden': [], 'Riverwoman': [71, 72], 'Seaman': [73], 'Smuggler': [74, 75], 'Stevedore': [76, 77], 'Wrecker': [78]}
    dwarfRogue = {'Bawd': [], 'Charlatan': [], 'Fence': [79], 'Grave Robber': [], 'Outlaw': [80, 81, 82], 'Racketeer': [83], 'Thief': [84], 'Witch': []}
    dwarfWarrior = {'Cavalryman': [], 'Guard': [85, 86, 87], 'Knight': [], 'Pit Fighter': [88, 89, 90], 'Protagonist': [91, 92, 93], 'Soldier': [94, 95, 96], 'Slayer': [97, 98, 99, 100], 'Warrior Priest': []}

    # Halfling Class dictionary that contains careers as each key. Then the value for each key is a list of rolls that decides the career.
    halflingAcademic = {'Apothecary': [1], 'Engineer': [2], 'Lawyer': [3, 4], 'Nun': [], 'Physcian': [5, 6], 'Priest': [], 'Scholar': [7, 8], 'Wizard': []}
    halflingBurgher = {'Agitator': [9, 10], 'Artisan': [11, 12, 13, 14, 15], 'Beggar': [16, 17, 18, 19], 'Investigator': [20, 21], 'Merchant': [22, 23, 24, 25], 'Rat Catcher': [26, 27, 28], 'Townsman': [29, 30, 31], 'Watchman': [32, 33]}
    halflingCourtier = {'Advisor': [34], 'Artist': [35, 36], 'Duelist': [], 'Envoy': [37], 'Noble': [], 'Servant': [38, 39, 40, 41, 42, 43], 'Spy': [44], 'Warden': [45, 46]}
    laflingeasant = {'Bailiff': [47], 'Hedge Witch': [], 'Herbalist': [48, 49, 50], 'Hunter': [51, 52], 'Miner': [53], 'Mystic': [], 'Scout': [54], 'Villager': [55, 56, 57]}
    halflingRanger = {'Bounty Hunter': [58], 'Coachman': [59, 60], 'Entertainer': [61, 62, 63], 'Flagellant': [], 'Messenger': [64, 65], 'Pedlar': [66, 67], 'Road Warden': [68], 'Witch Huner': []}
    halflingRiverfolk = {'Boatman': [69], 'Huffer': [70], 'Riverwarden': [71], 'Riverwoman': [72, 73, 74], 'Seaman': [75], 'Smuggler': [76, 77, 78, 79], 'Stevedore': [80, 81, 82], 'Wrecker': []}
    halflingRogue = {'Bawd': [83, 84, 85], 'Charlatan': [86], 'Fence': [87], 'Grave Robber': [88], 'Outlaw': [89], 'Racketeer': [90], 'Thief': [91, 92, 93, 94], 'Witch': []}
    halflingWarrior = {'Cavalryman': [], 'Guard': [95, 96], 'Knight': [], 'Pit Fighter': [97], 'Protagonist': [], 'Soldier': [98, 99, 100], 'Slayer': [], 'Warrior Priest': []}

    # Highelf Class dictionary that contains careers as each key. Then the value for each key is a list of rolls that decides the career.
    highelfAcademic = {'Apothecary': [1, 2], 'Engineer': [], 'Lawyer': [3, 4, 5, 6], 'Nun': [], 'Physcian': [7, 8], 'Priest': [], 'Scholar': [9, 10, 11, 12], 'Wizard': [13, 14, 15, 16]}
    highelfBurgher = {'Agitator': [], 'Artisan': [17, 18, 19], 'Beggar': [], 'Investigator': [20, 21], 'Merchant': [22, 23, 24, 25, 26], 'Rat Catcher': [], 'Townsman': [27, 28], 'Watchman': [29]}
    highelfCourtier = {'Advisor': [30, 31], 'Artist': [32], 'Duelist': [33, 34], 'Envoy': [35, 36, 37], 'Noble': [38, 39, 40], 'Servant': [], 'Spy': [41, 42, 43], 'Warden': [44, 45]}
    highelfPeasant = {'Bailiff': [], 'Hedge Witch': [], 'Herbalist': [46, 47], 'Hunter': [48, 49, 50], 'Miner': [], 'Mystic': [], 'Scout': [51, 52, 53, 54, 55, 56], 'Villager': []}
    highelfRanger = {'Bounty Hunter': [57, 56, 59], 'Coachman': [], 'Entertainer': [60, 61, 62], 'Flagellant': [], 'Messenger': [63], 'Pedlar': [], 'Road Warden': [], 'Witch Huner': []}
    highelfRiverfolk = {'Boatman': [64], 'Huffer': [], 'Riverwarden': [], 'Riverwoman': [], 'Seaman': [65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75], 'Smuggler': [80], 'Stevedore': [], 'Wrecker': []}
    highelfRogue = {'Bawd': [81, 82], 'Charlatan': [83, 84, 85], 'Fence': [], 'Grave Robber': [], 'Outlaw': [86, 87, 88], 'Racketeer': [], 'Thief': [], 'Witch': []}
    highelfWarrior = {'Cavalryman': [89, 90, 91, 92], 'Guard': [93, 94], 'Knight': [95], 'Pit Fighter': [96, 97], 'Protagonist': [98], 'Soldier': [99, 100], 'Slayer': [], 'Warrior Priest': []}

    # Woodelf Class dictionary that contains careers as each key. Then the value for each key is a list of rolls that decides the career.
    woodelfAcademic = {'Apothecary': [], 'Engineer': [], 'Lawyer': [], 'Nun': [], 'Physcian': [], 'Priest': [], 'Scholar': [1], 'Wizard': [2, 3, 4, 5]}
    woodelfBurgher = {'Agitator': [], 'Artisan': [6, 7, 8, 9, 10], 'Beggar': [], 'Investigator': [], 'Merchant': [], 'Rat Catcher': [], 'Townsman': [], 'Watchman': []}
    woodelfCourtier = {'Advisor': [11, 12, 13, 14], 'Artist': [15, 16, 17, 18], 'Duelist': [], 'Envoy': [19, 20, 21, 22, 23, 24, 25], 'Noble': [26, 27, 28, 29, 30, 31], 'Servant': [], 'Spy': [32, 33, 34, 35], 'Warden': []}
    woodelfPeasant = {'Bailiff': [], 'Hedge Witch': [], 'Herbalist': [36, 37, 38, 39, 40, 41, 42], 'Hunter': [43, 44, 45, 46, 47, 48, 49, 50, 51, 52], 'Miner': [], 'Mystic': [53, 54, 55, 56, 57], 'Scout': [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68], 'Villager': []}
    woodelfRanger = {'Bounty Hunter': [69, 70], 'Coachman': [], 'Entertainer': [71, 72, 73, 74, 75], 'Flagellant': [], 'Messenger': [76, 77, 78], 'Pedlar': [], 'Road Warden': [], 'Witch Huner': []}
    woodelfRiverfolk = {'Boatman': [], 'Huffer': [], 'Riverwarden': [], 'Riverwoman': [], 'Seaman': [], 'Smuggler': [], 'Stevedore': [], 'Wrecker': [79]}
    woodelfRogue = {'Bawd': [], 'Charlatan': [], 'Fence': [], 'Grave Robber': [], 'Outlaw': [80, 81, 82, 83, 84, 85], 'Racketeer': [], 'Thief': [], 'Witch': []}
    woodelfWarrior = {'Cavalryman': [86, 87, 88, 89, 90], 'Guard': [91, 92], 'Knight': [93, 94], 'Pit Fighter': [95, 96], 'Protagonist': [], 'Soldier': [97, 98, 99, 100], 'Slayer': [], 'Warrior Priest': []}

    print("""
Part 2: Class and Career
-----------------------------------------------------------------------------------------------------------
- Next we will roll for your class and career.
- The following list is the class followed by the career.
- I won't be typing out the details on what can be what, so please reference pages 30 and 31 of the guide.
- I will have the correct stops in place for species not being able to be certain careers, etc.
- Academics: Apothecary, Engineer, Lawyer, Nun, Physcian, Priest, Scholar, Wizard.
- Burghers: Agitator, Artisan, Beggar, Investigator, Merchant, Rat Catcher, Townsman.
- Courtiers: Advisor, Artist, Duelist, Envoy, Noble, Servant, Spy, Warden.
- Peasants: Baliff, Hedge Witch, Herbalist, Hunter, Miner, Mystic, Scout, Villager.
- Rangers: Bounty Hunter, Coachman, Entertainer, Flagellant, Messenger, Pedlar, Road Warden, Witch Hunter.
- Riverfolk: Boatman, Huffer, Riverwarden, Riverwoman, Seaman, Smuggler, Stevedore, Wrecker.
- Rogues: Bawd, Charlatan, Fence, Grave Robber, Outlaw, Racketeer, Thief, Witch.
- Warriors: Cavalryman, Guard, Knight, Pit Fighter, Protagonist, Soldier, Slayer, Warrior Priest.
-----------------------------------------------------------------------------------------------------------""")

    d100 = random.randint(1, 100)

    if species == 'Human (Reiklander)':
        if d100 < 15:
            for charClass in humanAcademic:
                for posRoll in humanAcademic[charClass]:
                    if posRoll == d100:
                        specClass = 'Academic'
                        career = charClass
        elif d100 > 14 and d100 < 28:
            for charClass in humanBurgher:
                for posRoll in humanBurgher[charClass]:
                    if posRoll == d100:
                        specClass = 'Burgher'
                        career = charClass
        elif d100 > 27 and d100 < 38:
            for charClass in humanCourtier:
                for posRoll in humanCourtier[charClass]:
                    if posRoll == d100:
                        specClass = 'Courtier'
                        career = charClass
        elif d100 > 37 and d100 < 51:
            for charClass in humanPeasant:
                for posRoll in humanPeasant[charClass]:
                    if posRoll == d100:
                        specClass = 'Peasant'
                        career = charClass
        elif d100 > 50 and d100 < 61:
            for charClass in humanRanger:
                for posRoll in humanRanger[charClass]:
                    if posRoll == d100:
                        specClass = 'Ranger'
                        career = charClass
        elif d100 > 60 and d100 < 75:
            for charClass in humanRiverfolk:
                for posRoll in humanRiverfolk[charClass]:
                    if posRoll == d100:
                        specClass = 'Riverfolk'
                        career = charClass
        elif d100 > 74 and d100 < 89:
            for charClass in humanRogue:
                for posRoll in humanRogue[charClass]:
                    if posRoll == d100:
                        specClass = 'Rogue'
                        career = charClass
        else:
            for charClass in humanWarrior:
                for posRoll in humanWarrior[charClass]:
                    if posRoll == d100:
                        specClass = 'Warrior'
                        career = charClass

    elif species == 'Dwarf':
        if d100 < 10:
            for charClass in dwarfAcademic:
                for posRoll in dwarfAcademic[charClass]:
                    if posRoll == d100:
                        specClass = 'Academic'
                        career = charClass
        elif d100 > 9 and d100 < 35:
            for charClass in dwarfBurgher:
                for posRoll in dwrfBurgher[charClass]:
                    if posRoll == d100:
                        specClass = 'Burgher'
                        career = charClass
        elif d100 > 34 and d100 < 46:
            for charClass in dwarfCourtier:
                for posRoll in dwarfCourtier[charClass]:
                    if posRoll == d100:
                        specClass = 'Courtier'
                        career = charClass
        elif d100 > 45 and d100 < 57:
            for charClass in dwarfPeasant:
                for posRoll in dwarfPeasant[charClass]:
                    if posRoll == d100:
                        specClass = 'Peasant'
                        career = charClass
        elif d100 > 56 and d100 < 68:
            for charClass in dwarfRanger:
                for posRoll in dwarfRanger[charClass]:
                    if posRoll == d100:
                        specClass = 'Ranger'
                        career = charClass
        elif d100 > 67 and d100 < 79:
            for charClass in dwarfRiverfolk:
                for posRoll in dwarfRiverfolk[charClass]:
                    if posRoll == d100:
                        specClass = 'Riverfolk'
                        career = charClass
        elif d100 > 78 and d100 < 85:
            for charClass in dwarfRogue:
                for posRoll in dwarfRogue[charClass]:
                    if posRoll == d100:
                        specClass = 'Rogue'
                        career = charClass
        else:
            for charClass in dwarfWarrior:
                for posRoll in dwarfWarrior[charClass]:
                    if posRoll == d100:
                        specClass = 'Warrior'
                        career = charClass

    return [d100, specClass, career]

species = randomSpecies()
time.sleep(5)
classCareer = randomClass(species)
time.sleep(5)
print(f"""
Part: 3 Exit Prompt
----------------------------------------------------------------------------------
- Roll for [Species]: {species[0]}.
- Roll for [Class] and [Career]: {classCareer[0]}
--------------------------------------------------------

- Your final character is below:
--------------------------------
[Species]: {species[1]}.
[Class]: {classCareer[1]}.
[Career]: {classCareer[2]}.
--------------------------------

- You have completed the random character creation tool for Warhammer Fantasy RP.
- Roll again for a chance at a different opportunity!
----------------------------------------------------------------------------------
\n""")
