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

    humanST = {'Skills': ['Animal Care', 'Charm', 'Cool', 'Evaluate', 'Gossip', 'Haggle', 'Language (Bretonnian)',
                          'Language (Wastelander)', 'Leadership', 'Lore (Reiklander)', 'Melee (Basic)', 'Ranged (Bow)'],
               'Talents': ['Doomed', 'Savvy', 'Suave']}

    dwarfST = {'Skills': ['Consume Alchohol', 'Cool', 'Endurance', 'Entertain (Storytelling)', 'Evaluate', 'Intimidate',
                          'Language (Khazalid)', 'Lore (Dwarfs)', 'Lore (Geology)', 'Lore (Metallurgy)', 'Melee (Basic)', 'Trade (Any one)'],
               'Talents': ['Magic Resistance', 'Night Vision', 'Read/Write', 'Relentless', 'Resolute', 'Strong-minded', 'Sturdy']}

    halflingST = {'Skills': ['Charm', 'Consume Alchohol', 'Dodge', 'Gamble', 'Haggle', 'Intuition', 'Languge (Mootish)',
                             'Lore (Reikland)', 'Perception', 'Sleight of Hand', 'Stealth (Any)', 'Trade (Cook)'],
                  'Talents': ['Acute Sense (Taste)', 'Night Vision', 'Resistance (Chaos)', 'Small', 'Two Random']}

    highelfST = {'Skills': ['Cool', 'Entertain (Sing)', 'Evaluate', 'Language (Eltharin)', 'Leadership', 'Melee (Basic)',
                            'Navigation', 'Perception', 'Play (any one)', 'Ranged (Bow)', 'Sail', 'Swim'],
                 'Talents': ['Acute Sense (Sight)', 'Coolheaded', 'Savvy', 'Night Vision', 'Second Sight', 'Sixth Sense', 'Read/Write']}

    woodelfST = {'Skills': ['Athletics', 'Climb', 'Endurance', 'Entertain (Sing)', 'Intimidate', 'Language (Eltharin)', 'Melee (Basic)',
                            'Outdoor Survival', 'Perception', 'Ranged (Bow)', 'Stealth (Rural)', 'Track'],
                 'Talents': ['Acute Sense (Sight)', 'Hardy', 'Second Sight', 'Night Vision', 'Read/Write', 'Very Resilient', 'Rover']}

    randomTal = {'Acute Sense (any one)': [1, 2, 3], 'Ambidextrous': [4, 5, 6], 'Animal Affinity': [7, 8, 9], 'Artistic': [10, 11, 12],
                 'Attractive': [13, 14, 15], 'Coolheaded': [16, 17, 18], 'Craftsman (Any one)': [19, 20, 21], 'Flee!': [22, 23, 24],
                 'Hardy': [25, 26, 27, 28], 'Lightning Reflexes': [29, 30, 31], 'Linguistics': [32, 33, 34], 'Luck': [35, 36, 37, 38],
                 'Marksman': [39, 40, 41], 'Mimic': [42, 43, 44], 'Night Vision': [45, 46, 47], 'Nimble Fingered': [48, 49, 50],
                 'Noble Blood': [51, 52], 'Orientation': [53, 54, 55], 'Perfect Pitch': [56, 57, 58], 'Pure Soul': [59, 60, 61, 62],
                 'Read/Write': [63, 64, 65], 'Resistance (Any One)': [66, 67, 68], 'Savvy': [69, 70, 71], 'Sharp': [72, 73, 74],
                 'Sixth Sense': [76, 77, 78], 'Strong Legs': [79, 80, 81], 'Sturdy': [82, 83, 84], 'Suave': [85, 86, 87],
                 'Super Numerate': [88, 89, 90, 91], 'Very Resilient': [92, 93, 95], 'Very Strong': [95, 96, 97], 'Warrior Born': [98, 99, 100]}

    d100 = random.randint(1, 100)
    if d100 > 0 and d100 < 91:
        talents = ['']
        # Below is the logic to randomly generate skills. If you didn't get all the skills that your species has in the book.
        # but I can't read, in which case, there is no logic needed. But this logic took a long time to figure out
        # so I am just going to comment it out.
        # for x in range(6):
        #    skl = humanST['Skills'][random.randint(0, end)]
        #    humanST['Skills'].remove(skl)
        #    skills.insert(x, tal)
        #    skills.pop()
        #    end = end - 1
        for y in range(3):
            talRoll = random.randint(1, 100)
            for key in randomTal:
                for roll in randomTal[key]:
                    if talRoll == roll:
                        humanST['Talents'].append(key)

        return [d100, 'Human (Reiklander)', humanST]
    elif d100 > 90 and d100 < 95:
        talents = ['']
        for y in range(2):
            d100 = random.randint(1, 100)
            print (d100)
            for key in randomTal:
                for roll in randomTal[key]:
                    if d100 == roll:
                        halfLingST['Talents'].append(key)
        return [d100, 'Halfling', halflingST]
    elif d100 > 94 and d100 < 99:
        return [d100, 'Dwarf', dwarfST]
    elif d100 == 99:
        return [d100, 'High Elf', highelfST]
    elif d100 == 100:
        return [d100, 'Wood Elf', woodelfST]

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
    laflingPeasant = {'Bailiff': [47], 'Hedge Witch': [], 'Herbalist': [48, 49, 50], 'Hunter': [51, 52], 'Miner': [53], 'Mystic': [], 'Scout': [54], 'Villager': [55, 56, 57]}
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
                for posRoll in dwarfBurgher[charClass]:
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

    elif species == 'Halfling':
        if d100 < 9:
            for charClass in halflingAcademic:
                for posRoll in halflingAcademic[charClass]:
                    if posRoll == d100:
                        specClass = 'Academic'
                        career = charClass
        elif d100 > 8 and d100 < 34:
            for charClass in halflingBurgher:
                for posRoll in halflingBurgher[charClass]:
                    if posRoll == d100:
                        specClass = 'Burgher'
                        career = charClass
        elif d100 > 33 and d100 < 47:
            for charClass in halflingCourtier:
                for posRoll in halflingCourtier[charClass]:
                    if posRoll == d100:
                        specClass = 'Courtier'
                        career = charClass
        elif d100 > 46 and d100 < 58:
            for charClass in halflingPeasant:
                for posRoll in halflingPeasant[charClass]:
                    if posRoll == d100:
                        specClass = 'Peasant'
                        career = charClass
        elif d100 > 57 and d100 < 69:
            for charClass in halflingRanger:
                for posRoll in halflingRanger[charClass]:
                    if posRoll == d100:
                        specClass = 'Ranger'
                        career = charClass
        elif d100 > 68 and d100 < 83:
            for charClass in halflingRiverfolk:
                for posRoll in halflingRiverfolk[charClass]:
                    if posRoll == d100:
                        specClass = 'Riverfolk'
                        career = charClass
        elif d100 > 82 and d100 < 95:
            for charClass in halflingRogue:
                for posRoll in halflingRogue[charClass]:
                    if posRoll == d100:
                        specClass = 'Rogue'
                        career = charClass
        else:
            for charClass in halflingWarrior:
                for posRoll in halflingWarrior[charClass]:
                    if posRoll == d100:
                        specClass = 'Warrior'
                        career = charClass

    elif species == 'High Elf':
        if d100 < 17:
            for charClass in highelfAcademic:
                for posRoll in highelfAcademic[charClass]:
                    if posRoll == d100:
                        specClass = 'Academic'
                        career = charClass
        elif d100 > 16 and d100 < 30:
            for charClass in highelfBurgher:
                for posRoll in highelfBurgher[charClass]:
                    if posRoll == d100:
                        specClass = 'Burgher'
                        career = charClass
        elif d100 > 29 and d100 < 46:
            for charClass in highelfCourtier:
                for posRoll in highelfCourtier[charClass]:
                    if posRoll == d100:
                        specClass = 'Courtier'
                        career = charClass
        elif d100 > 45 and d100 < 57:
            for charClass in highelfPeasant:
                for posRoll in highelfPeasant[charClass]:
                    if posRoll == d100:
                        specClass = 'Peasant'
                        career = charClass
        elif d100 > 56 and d100 < 64:
            for charClass in highelfRanger:
                for posRoll in highelfRanger[charClass]:
                    if posRoll == d100:
                        specClass = 'Ranger'
                        career = charClass
        elif d100 > 63 and d100 < 81:
            for charClass in highelfRiverfolk:
                for posRoll in highelfRiverfolk[charClass]:
                    if posRoll == d100:
                        specClass = 'Riverfolk'
                        career = charClass
        elif d100 > 80 and d100 < 89:
            for charClass in highelfRogue:
                for posRoll in highelfRogue[charClass]:
                    if posRoll == d100:
                        specClass = 'Rogue'
                        career = charClass
        else:
            for charClass in highelfWarrior:
                for posRoll in highelfWarrior[charClass]:
                    if posRoll == d100:
                        specClass = 'Warrior'
                        career = charClass

    elif species == 'Wood Elf':
        if d100 < 6:
            for charClass in woodelfAcademic:
                for posRoll in woodelfAcademic[charClass]:
                    if posRoll == d100:
                        specClass = 'Academic'
                        career = charClass
        elif d100 > 5 and d100 < 11:
            for charClass in woodelfBurgher:
                for posRoll in woodelfBurgher[charClass]:
                    if posRoll == d100:
                        specClass = 'Burgher'
                        career = charClass
        elif d100 > 10 and d100 < 36:
            for charClass in woodelfCourtier:
                for posRoll in woodelfCourtier[charClass]:
                    if posRoll == d100:
                        specClass = 'Courtier'
                        career = charClass
        elif d100 > 35 and d100 < 69:
            for charClass in woodelfPeasant:
                for posRoll in woodelfPeasant[charClass]:
                    if posRoll == d100:
                        specClass = 'Peasant'
                        career = charClass
        elif d100 > 68 and d100 < 79:
            for charClass in woodelfRanger:
                for posRoll in woodelfRanger[charClass]:
                    if posRoll == d100:
                        specClass = 'Ranger'
                        career = charClass
        elif d100 > 78 and d100 < 80:
            for charClass in woodelfRiverfolk:
                for posRoll in woodelfRiverfolk[charClass]:
                    if posRoll == d100:
                        specClass = 'Riverfolk'
                        career = charClass
        elif d100 > 79 and d100 < 86:
            for charClass in woodelfRogue:
                for posRoll in woodelfRogue[charClass]:
                    if posRoll == d100:
                        specClass = 'Rogue'
                        career = charClass
        else:
            for charClass in woodelfWarrior:
                for posRoll in woodelfWarrior[charClass]:
                    if posRoll == d100:
                        specClass = 'Warrior'
                        career = charClass

    return [d100, specClass, career]

def attributeTable(species):
    print("""
Part 3: Attributes
------------------------------------------------------------------------------
- Now we will roll for your attributes and skills.
- The attributes that will be rolled for are as follows:
    - Weapon skill
    - Ballistic skill
    - Strength
    - Toughness
    - Initiative
    - Agility
    - Dexeterity
    - Intelligence
    - Willpower
    - Fellowship
- Wounds, Fate, Resilience, Extra Points, and Movement will be displayed as is
  in the table on page 33.
------------------------------------------------------------------------------""")
    species = species[1]
    wep = 0
    ball = 0
    stren = 0
    tough = 0
    initi = 0
    agi = 0
    dex = 0
    intell = 0
    willpow = 0
    fellow = 0
    wounds = 0
    fate = 0
    resil = 0
    extra = 0
    movement = 0

    if species == 'Human (Reiklander)':
        wep = 20 + random.randint(1, 10) + random.randint(1, 10)
        ball = 20 + random.randint(1, 10) + random.randint(1, 10)
        stren = 20 + random.randint(1, 10) + random.randint(1, 10)
        tough = 20 + random.randint(1, 10) + random.randint(1, 10)
        initi = 20 + random.randint(1, 10) + random.randint(1, 10)
        agi = 20 + random.randint(1, 10) + random.randint(1, 10)
        dex = 20 + random.randint(1, 10) + random.randint(1, 10)
        intell = 20 + random.randint(1, 10) + random.randint(1, 10)
        willpow = 20 + random.randint(1, 10) + random.randint(1, 10)
        fellow = 20 + random.randint(1, 10) + random.randint(1, 10)
        fate = 2
        resil = 1
        extra = 3
        movement = 4
        wounds = stren + (2 * tough) + willpow

    elif species == 'Dwarf':
        wep = 30 + random.randint(1, 10) + random.randint(1, 10)
        ball = 20 + random.randint(1, 10) + random.randint(1, 10)
        stren = 20 + random.randint(1, 10) + random.randint(1, 10)
        tough = 30 + random.randint(1, 10) + random.randint(1, 10)
        initi = 20 + random.randint(1, 10) + random.randint(1, 10)
        agi = 10 + random.randint(1, 10) + random.randint(1, 10)
        dex = 30 + random.randint(1, 10) + random.randint(1, 10)
        intell = 20 + random.randint(1, 10) + random.randint(1, 10)
        willpow = 40 + random.randint(1, 10) + random.randint(1, 10)
        fellow = 10 + random.randint(1, 10) + random.randint(1, 10)
        fate = 0
        resil = 2
        extra = 2
        movement = 2
        wounds = stren + (2 * tough) + willpow

    elif species == 'Halfling':
        wep = 10 + random.randint(1, 10) + random.randint(1, 10)
        ball = 30 + random.randint(1, 10) + random.randint(1, 10)
        stren = 10 + random.randint(1, 10) + random.randint(1, 10)
        tough = 20 + random.randint(1, 10) + random.randint(1, 10)
        initi = 20 + random.randint(1, 10) + random.randint(1, 10)
        agi = 20 + random.randint(1, 10) + random.randint(1, 10)
        dex = 30 + random.randint(1, 10) + random.randint(1, 10)
        intell = 20 + random.randint(1, 10) + random.randint(1, 10)
        willpow = 30 + random.randint(1, 10) + random.randint(1, 10)
        fellow = 30 + random.randint(1, 10) + random.randint(1, 10)
        fate = 0
        resil = 2
        extra = 3
        movement = 3
        wounds = (2 * tough) + willpow

    elif species == 'High Elf' or species == 'Wood Elf':
        wep = 30 + random.randint(1, 10) + random.randint(1, 10)
        ball = 30 + random.randint(1, 10) + random.randint(1, 10)
        stren = 20 + random.randint(1, 10) + random.randint(1, 10)
        tough = 30 + random.randint(1, 10) + random.randint(1, 10)
        initi = 40 + random.randint(1, 10) + random.randint(1, 10)
        agi = 30 + random.randint(1, 10) + random.randint(1, 10)
        dex = 30 + random.randint(1, 10) + random.randint(1, 10)
        intell = 30 + random.randint(1, 10) + random.randint(1, 10)
        willpow = 30 + random.randint(1, 10) + random.randint(1, 10)
        fellow = 20 + random.randint(1, 10) + random.randint(1, 10)
        fate = 0
        resil = 0
        extra = 2
        movement = 5
        wounds = stren + (2 * tough) + willpow

    return [wep, ball, stren, tough, initi, agi, dex, intell, willpow, fellow, wounds, fate, resil, extra, movement]

species = randomSpecies()
stDict = species[2]
time.sleep(5)
classCareer = randomClass(species)
time.sleep(5)
attTable = attributeTable(species)

print(f"""
Part 4: Exit Prompt
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

- Your Attribute Table is below:
--------------------------------
[Weapon Skill]: {attTable[0]}.
[Ballistic Skill]: {attTable[1]}.
[Strength]: {attTable[2]}.
[Toughness]: {attTable[3]}.
[Initiative]: {attTable[4]}.
[Agility]: {attTable[5]}.
[Dexterity]: {attTable[6]}.
[Intelligence]: {attTable[7]}.
[Willpower]: {attTable[8]}.
[Fellowship]: {attTable[9]}.
[Wounds]: {attTable[10]}.
[Fate]: {attTable[11]}.
[Resilience]: {attTable[12]}.
[Extra Points]: {attTable[13]}.
[Movement]: {attTable[14]}.

-Your Skills and Talents portfolio is below:
--------------------------------------------
[Skills]: {stDict['Skills'][0]}, {stDict['Skills'][1]}, {stDict['Skills'][2]}, {stDict['Skills'][3]}, {stDict['Skills'][4]},
{stDict['Skills'][5]}, {stDict['Skills'][6]}, {stDict['Skills'][7]}, {stDict['Skills'][8]}, {stDict['Skills'][9]},
{stDict['Skills'][10]}, {stDict['Skills'][11]}.

[Talents]: {stDict['Talents'][0]}, {stDict['Talents'][1]}, {stDict['Talents'][2]}, {stDict['Talents'][3]}, {stDict['Talents'][4]}

----------------------------------------------------------------------------------
- You have completed the random character creation tool for Warhammer Fantasy RP.
- Roll again for a chance at a different opportunity!
----------------------------------------------------------------------------------
\n""")
