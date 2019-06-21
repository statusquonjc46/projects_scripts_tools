#! /usr/bin/python3
# Simple Warhammer Fantasy Role Play Character Generator
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import random

# d100 = random.randint(1, 100)
species = ''
specClass = ''
career = ''
print("""
-------------------------------------------------------------------------------------
- Welcome to the Warhammer Fantasy RolePlay(WFRP) game character generator.
- Everything you find in this script is from the 4th edition of WFRP.
- If you would like to follow along with the prompts,
- I will try to accurately label each prompt with its corresponding page in the book.
- Enjoy, and may the d100 be with you.
-------------------------------------------------------------------------------------""")


def randomSpecies():
    print("""
    --------------------------------------------------------
    - First we are going to roll for your species.
    - This is done with a d100.
    - Human falls in the range of 1-90.
    - Halfling falls in the range of 91-94.
    - Dwarf falls in the range of 95-98.
    - High Elf is 99.
    - Wood Elf is 100.
    - This can be found on page 24 of the 4th Edition Guide.
    --------------------------------------------------------\n\n""")

    d100 = random.randint(1, 100)
    print(f'You rolled a {d100}.\n')
    if d100 > 0 and d100 < 91:
        print('You got: Human (Reiklander)!\n')
        return 'Human (Reiklander)'
    elif d100 > 90 and d100 < 95:
        print('You got: Halfling!\n')
        return 'Halfling'
    elif d100 > 94 and d100 < 99:
        print('You got: Dwarf!\n')
        return 'Dwarf'
    elif d100 == 99:
        print('You got: High Elf!\n')
        return 'High Elf'
    elif d100 == 100:
        print('You got: Wood Elf!\n')
        return 'Wood Elf'

def randomClass(species):
    species = species
    specClass = ''
    specCareer = ''

    # Dictionaries for each class for each species containing rolls for each career.
    # Human Class with their careers.
    humanAcademic = {1: 'Apothecary', 2: 'Engineer', 3: 'Lawyer', 4: 'Nun', 5: 'Nun', 6: 'Physcian', 7: 'Priest', 8: 'Priest',
                        9: 'Priest', 10: 'Priest', 11: 'Priest', 12: 'Scholar', 13: 'Scholar', 14: 'Wizard'}
    humanBurgher = {15: 'Agitator', 16: 'Artisan', 17: 'Artisan', 18: 'Beggar', 19: 'Beggar', 20: 'Investigator', 21: 'Merchant',
                        22: 'Rat Catcher', 23: 'Rat Catcher', 24: 'Townsman', 25: 'Townsman', 26: 'Townsman', 27: 'Watchman'}
    humanCourtier = {28: 'Advisor', 29: 'Artist', 30: 'Duelist', 31: 'Envoy', 32: 'Noble', 33: 'Servant', 34: 'Servant', 35: 'Servant',
                     36: 'Spy', 37: 'Warden'}
    humanPeasant = {38: 'Bailiff', 39: 'Hedge Witch', 40: 'Herbalist', 41: 'Hunter', 42: 'Hunter', 43: 'Miner', 44: 'Mystic', 45: 'Scout',
                    46: 'Villager', 47: 'Villager', 48: 'Villager', 49: 'Villager', 50: 'Villager'}
    humanRanger = {51: 'Bounty Hunter', 52: 'Coachman', 53: 'Entertainer', 54: 'Entertainer', 55: 'Flagellant', 56: 'Flagellant',
                       57: 'Messenger', 58: 'Pedlar', 59: 'Road Warden', 60: 'Witch Hunter'}
    humanRiverfolk = {61: 'Boatman', 62: 'Boatman', 63: 'Huffer', 64: 'Riverwarden', 65: 'Riverwarden', 66: 'Riverwoman', 67: 'Riverwoman',
                          68: 'Riverwoman', 69: 'Seaman', 70: 'Seaman', 71: 'Smuggler', 72: 'Stevedore', 73: 'Stevedore', 74: 'Wrecker'}
    humanRogue = {75: 'Bawd', 76: 'Bawd', 77: 'Charlatan', 78: 'Fence', 79: 'Grave Robber', 80: 'Outlaw', 81: 'Outlaw', 82: 'Outlaw',
                      83: 'Outlaw', 84: 'Racketeer', 85: 'Thief', 86: 'Thief', 87: 'Thief', 88: 'Witch'}
    humanWarrior = {89: 'Cavalryman', 90: 'Cavalryman', 91: 'Guard', 92: 'Guard', 93: 'Knight', 94: 'Pit Fighter', 95: 'Protagonist',
                    96: 'Soldier', 97: 'Soldier', 98: 'Soldier', 99: 'Soldier', 100: 'Warrior Priest'}

    # Dwarf Class with careers.
    dwarfAcademic = {1: 'Apothecary', 2: 'Engineer', 3: 'Engineer', 4: 'Engineer', 5: 'Lawyer', 6: 'Lawyer', 7: 'Physcian', 8: 'Scholar',
                        9: 'Scholar'}
    dwarfBurgher = {10: 'Agitator', 11: 'Agitator', 12: 'Artisan', 13: 'Artisan', 14: 'Artisan', 15: 'Artisan', 16: 'Artisan',
                        17: 'Artisan', 18: 'Beggar', 19: 'Investigator', 20: 'Investigator', 21: 'Merchant', 22: 'Merchant', 23: 'Merchant',
                        24: 'Merchant', 25: 'Rat Catcher', 26: 'Townsman', 27: 'Townsman', 28: 'Townsman', 29: 'Townsman', 30: 'Townsman',
                        31: 'Townsman', 32: 'Watchman', 33: 'Watchman', 34: 'Watchman'}
    dwarfCourtier = {35: 'Advisor', 36: 'Advisor', 37: 'Artist', 38: 'Duelist', 39: 'Envoy', 40: 'Envoy', 41: 'Noble', 42: 'Servant',
                     43: 'Spy', 44: 'Warden', 45: 'Warden'}
    dwarfPeasant = {46: 'Bailiff', 47: 'Bailiff', 48: 'Hunter', 49: 'Hunter', 50: 'Miner', 51: 'Miner', 52: 'Miner', 53: 'Miner',
                    54: 'Miner', 55: 'Scout', 56: 'Villager'}
    dwarfRanger = {57: 'Bounty Hunter', 58: 'Bounty Hunter', 59: 'Bounty Hunter', 60: 'Bounty Hunter', 61: 'Coachman', 62: 'Entertainer',
                       63: 'Entertainer', 64: 'Messenger', 65: 'Messenger', 66: 'Pedlar', 67: 'Pedlar'}
    dwarfRiverfolk = {68: 'Boatman', 69: 'Boatman', 70: 'Huffer', 71: 'Riverwoman', 72: 'Riverwoman', 73: 'Seaman', 74: 'Smuggler', 75: 'Smuggler'
                          76: 'Stevedore', 77: 'Stevedore', 78: 'Wrecker'}
    dwarfRogue = {79: 'Fence', 80: 'Outlaw', 81: 'Outlaw', 82: 'Outlaw', 83: 'Racketeer', 84: 'Thief'}
    dwarfWarrior = {85: 'Guard', 86: 'Guard', 87: 'Guard', 88: 'Pit Fighter', 89: 'Pit Fighter', 90: 'Pit Fighter', 91: 'Protagonist',
                    92: 'Protagonist', 93: 'Protagonist', 94: 'Soldier', 95: 'Soldier', 96: 'Soldier', 97: 'Slayer', 98: 'Slayer', 99: 'Slayer',
                    100: 'Warrior Priest'}

    # Halfling Class with careers.
    halflingAcademic = {1: 'Apothecary', 2: 'Engineer', 3: 'Lawyer', 4: 'Lawyer', 5: 'Physcian', 6: 'Physcian', 7: 'Scholar', 8: 'Scholar'}
    halflingBurgher = {9: 'Agitator', 10: 'Agitator', 11: 'Artisan', 12: 'Artisan', 13: 'Artisan', 14: 'Artisan', 15: 'Artisan', 16: 'Beggar',
                          18: 'Beggar', 19: 'Beggar', 20: 'Investigator', 21: 'Investigator', 22: 'Merchant', 23: 'Merchant',
                          24: 'Merchant', 25: 'Merchant', 26: 'Rat Catcher', 27: 'Rat Catcher', 28: 'Rat Catcher', 29: 'Townsman', 30: 'Townsman',
                          31: 'Townsman', 32: 'Watchman', 33: 'Watchman'}
    halflingCourtier = {34: 'Advisor', 35: 'Artist', 36: 'Artist', 37: 'Envoy', 38: 'Servant', 39: 'Servant', 40: 'Servant', 41: 'Servant', 42: 'Servant',
                        43: 'Servant', 44: 'Spy', 45: 'Warden', 46: 'Warden'}
    halflingPeasant = {47: 'Bailiff', 48: 'Herbalist', 49: 'Herbalist', 50: 'Herbalist', 51: 'Hunter', 52: 'Hunter', 53: 'Miner', 54: 'Scout', 55: 'Villager',
                           56: 'Villager', 57: 'Villager'}
    halflingRanger = {58: 'Bounty Hunter', 59: 'Coachman', 60: 'Coachman', 61: 'Entertainer', 62: 'Entertainer', 63: 'Entertainer', 64: 'Messenger', 65: 'Messenger',
                          66: 'Pedlar', 67: 'Pedlar', 68: 'Road Warden'}
    halflingRiverfolk = {69: 'Boatman', 70: 'Huffer', 71: 'Riverwarden', 72: 'Riverwoman', 73: 'Riverwoman', 74: 'Riverwoman', 75: 'Seaman', 76: 'Smuggler',
                             77: 'Smuggler', 78: 'Smuggler', 79: 'Smuggler', 80: 'Stevedore', 81: 'Stevedore', 82: 'Stevedore'}
    halflingRogue = {83: 'Bawd', 84: 'Bawd', 85: 'Bawd', 86: 'Charlatan', 87: 'Fence', 88: 'Grave Robber', 89: 'Outlaw', 90: 'Racketeer', 91: 'Thief', 92: 'Thief',
                         93: 'Thief', 94: 'Thief'}
    halflingWarrior = {95: 'Guard', 96: 'Guard', 97: 'Pit Fighter', 98: 'Soldier', 99: 'Soldier', 100: 'Soldier'}

    # High Elf Class with careers.
    highelfAcademic = {1: 'Apothecary', 2: 'Apothecary', 3: 'Lawyer', 4: 'Lawyer', 5: 'Lawyer', 6: 'Lawyer', 7: 'Physcian', 8: 'Physcian', 9: 'Scholar', 10: 'Scholar',
                          11: 'Scholar', 12: 'Scholar', 13: 'Wizard', 14: 'Wizard', 15: 'Wizard', 16: 'Wizard'}
    highelfBurgher = {17: 'Artisan', 18: 'Artisan', 19: 'Artisan', 20: 'Investigator', 21: 'Investigator', 22: 'Merchant', 23: 'Merchant', 24: 'Merchant', 25: 'Merchant',
                          26: 'Merchant', 27: 'Townsman', 28: 'Townsman', 29: 'Watchman'}
    highelfCourtier = {30: 'Advisor', 31: 'Advisor', 32: 'Artist', 33: 'Duelist', 34: 'Duelist', 35: 'Envoy', 36: 'Envoy', 37: 'Envoy', 38: 'Noble', 39: 'Noble',
                           40: 'Noble', 41: 'Spy', 42: 'Spy', 43: 'Spy', 44: 'Warden', 45: 'Warden'}
    highelfPeasant = {46: 'Herbalist', 47: 'Herbalist', 48: 'Hunter', 49: 'Hunter', 50: 'Hunter', 51: 'Scout', 52: 'Scout', 53: 'Scout', 54: 'Scout', 55: 'Scout',
                          56: 'Scout'}
    highelfRanger = {57: 'Bounter Hunter', 58: 'Bounty Hunter', 59: 'Bounty Hunter', 60: 'Entertainer', 61: 'Entertainer', 62: 'Entertainer', 63: 'Messenger'}
    highelfRiverfolk = {64: 'Boatman', 65: 'Seaman', 66: 'Seaman', 67: 'Seaman', 68: 'Seaman', 69: 'Seaman', 70: 'Seaman', 71: 'Seaman', 72: 'Seaman', 73: 'Seaman',
                            74: 'Seaman', 75: 'Seaman', 76: 'Seaman', 77: 'Seaman', 78: 'Seaman', 79: 'Seaman', 80: 'Smuggler'}
    highelfRogue = {81: 'Bawd', 82: 'Bawd', 83: 'Charlatan', 84: 'Charlatan', 85: 'Charlatan', 86: 'Outlaw', 87: 'Outlaw', 88: 'Outlaw'}
    highelfWarrior = {89: 'Cavalryman', 90: 'Cavalryman', 91: 'Cavalryman', 92: 'Cavalryman', 93: 'Guard', 94: 'Guard', 95: 'Knight', 96: 'Pit Fighter', 97: 'Pit Fighter',
                          98: 'Protagonist', 99: 'Soldier', 100: 'Soldier'}

    # Wood Elf Class with careers.
    woodelfAcademic = {1: 'Scholar', 2: 'Wizard', 3: 'Wizard', 4: 'Wizard', 5: 'Wizard'}
    woodelfBurgher = {6: 'Artisan', 7: 'Artisan', 8: 'Artisan', 9: 'Artisan', 10: 'Artisan'}
    woodelfCourtier = {11: 'Advisor', 12: 'Advisor', 13: 'Advisor', 14: 'Advisor', 15: 'Artist', 16: 'Artist', 17: 'Artist', 18: 'Artist', 19: 'Envoy', 20: 'Envoy',
                       21: 'Envoy', 22: 'Envoy', 23: 'Envoy', 24: 'Envoy', 25: 'Envoy', 26: 'Noble', 27: 'Noble', 28: 'Noble', 29: 'Noble', 30: 'Noble', 31: 'Noble',
                       32: 'Spy', 33: 'Spy', 34: 'Spy', 35: 'Spy'}
    woodelfPeasant = {36: 'Herbalist', 37: 'Herbalist', 38: 'Herbalist', 39: 'Herbalist', 40: 'Herbalist', ''}

    print("""\n
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
    -----------------------------------------------------------------------------------------------------------\n""")

    d100 = random.randint(1, 100)
    # Start of Human class and career selection.
    # Start of Academic roll ranges.
    if species == 'Human (Reiklander)':
        if d100 == 1:
            print('You are an Academic Human Apothecary')
            specClass = 'Academic'
            specCareer = 'Apothecary'
        elif d100 == 2:
            print('You are an Academic Human Engineer')
            specClass = 'Academic'
            specCareer = 'Engineer'
        elif d100 == 3:
            print('You are an Academic Human Lawyer')
            specClass = 'Academic'
            specCareer = 'Lawyer'
        elif d100 == 4 or d100 == 5:
            print('You are an Academic Human Nun')
            specClass = 'Academic'
            specCareer = 'Nun'
        elif d100 == 6:
            print('You are an Academic Human Physcian')
            specClass = 'Academic'
            specCareer = 'Physcian'
        elif d100 > 6 and d100 < 12:
            print('You are an Academic Human Priest')
            specClass = 'Academic'
            specCareer = 'Priest'
        elif d100 == 12 or d100 == 13:
            print('You are an Academic Human Scholar')
            specClass = 'Academic'
            specCareer = 'Scholar'
        elif d100 == 14:
            print('You are an Academic Human Wizard')
            specClass = 'Academic'
            specCareer = 'Wizard'
        elif d100 == 15:
            # End of Academic roll ranges.
            # Start of Burgher roll ranges.
            print('You are a Burgher Human Agitator')
            specClass = 'Burgher'
            specCareer = 'Agitator'
        elif d100 == 16 or d100 == 17:
            print('You are a Burgher Human Artisan')
            specClass = 'Burgher'
            specCareer = 'Artisan'
        elif d100 == 18 or d100 == 19:
            print('You are a Burgher Human Beggar')
            specClass = 'Burgher'
            specCareer = 'Beggar'
        elif d100 == 20:
            print('You are a Burgher Human Investigator')
            specClass = 'Burgher'
            specCareer = 'Investigator'
        elif d100 == 21:
            print('You are a Burgher Human Merchant')
            specClass = 'Burgher'
            specCareer = 'Merchant'
        elif d100 == 22 or d100 == 23:
            print('You are a Burgher Human Rat Catcher')
            specClass = 'Burgher'
            specCareer = 'Rat Catcher'
        elif d100 > 23 and d100 < 27:
            print('You are a Burgher Human Townsman')
            specClass = 'Burgher'
            specCareer = 'Townsman'
        elif d100 == 27:
            print('You are a Burgher Human Watchman')
            specClass = 'Burgher'
            specCareer = 'Watchman'
        elif d100 == 28:
            # End of Burgher roll range.
            # Start of Courtier roll range.
            print('You are a Courtier Human Advisor')
            specClass = 'Courtier'
            specCareer = 'Advisor'
        elif d100 29:
            print('You are a Courtier Human Artist')
            specClass = 'Courtier'
            specCareer = 'Artist'
        elif d100 == 30:
            print('You are a Courtier Human Duelist')
            specClass = 'Courtier'
            specCareer = 'Duelist'
        elif d100 == 31:
            print('You are an Courtier Human Envoy')
            specClass = 'Courtier'
            specCareer = 'Envoy'
        elif d100 == 32:
            print('You are a Courtier Human Noble')
            specClass = 'Courtier'
            specCareer = 'Noble'
        elif d100 > 32 and d100 < 36:
            print('You are a Courtier Human Servant')
            specClass = 'Courtier'
            specCareer = 'Servant'
        elif d100 == 36:
            print('You are a Courtier Human Spy')
            specClass = 'Courtier'
            specCareer = 'Spy'
        elif d100 == 37:
            print('You are a Courtier Human Warden')
            specClass = 'Courtier'
            specCareer = 'Warden'
        # End of Courtier roll range.
        # Start of Peasant roll range.
        elif d100 == 38:
            print('You are a Peasant Human Bailiff')
            specClass = 'Peasant'
            specCareer = 'Bailiff'
        elif d100 39:
            print('You are a Peasant Human Hedge Witch')
            specClass = 'Peasant'
            specCareer = 'Hedge Witch'
        elif d100 == 40:
            print('You are a Peasant Human Herbalist')
            specClass = 'Peasant'
            specCareer = 'Herbalist'
        elif d100 == 41 or d100 == 42:
            print('You are a Peasant Human Hunter')
            specClass = 'Peasant'
            specCareer = 'Hunter'
        elif d100 == 43:
            print('You are a Peasant Human Miner')
            specClass = 'Peasant'
            specCareer = 'Miner'
        elif d100 == 44:
            print('You are a Peasant Human Mystic')
            specClass = 'Peasant'
            specCareer = 'Mystic'
        elif d100 == 45:
            print('You are a Peasant Human Scout')
            specClass = 'Peasant'
            specCareer = 'Scout'
        elif d100 > 45 and d100 < 51:
            print('You are a Peasant Human Villager')
            specClass = 'Peasant'
            specCareer = 'Villager'
        # End of Peasant roll range.
        # Start of Ranger roll range.
        elif d100 == 51:
            print('You are a Ranger Human Bounty Hunter')
            specClass = 'Ranger'
            specCareer = 'Bounter Hunter'
        elif d100 == 52:
            print('You are a Ranger Human Coachman')
            specClass = 'Ranger'
            specCareer = 'Coachman'
        elif d100 == 53 or d100 == 54:
            print('You are a Ranger Human Entertainer')
            specClass = 'Ranger'
            specCareer = 'Entertainer'
        elif d100 == 55 or d100 == 56:
            print('You are a Ranger Human Flagellant')
            specClass = 'Ranger'
            specCareer = 'Flagellant'
        elif d100 == 57:
            print('You are a Ranger Human Messanger')
            specClass = 'Ranger'
            specCareer = 'Messenger'
        elif d100 == 58:
            print('You are a Ranger Human Pedlar')
            specClass = 'Ranger'
            specCareer = 'Pedlar'
        elif d100 == 59:
            print('You are a Ranger Human Road Warden')
            specClass = 'Ranger'
            specCareer = 'Road Warden'
        elif d100 == 60:
            print('You are a Ranger Human Witch Hunter')
            specClass = 'Ranger'
            specCareer = 'Witch Hunter'
        # End of Ranger roll range.
        # Start of Riverfolk roll range.
        elif d100 == 61 or d100 == 62:
            print('You are a Riverfolk Human Boatman')
            specClass = 'Riverfolk'
            specCareer = 'Boatman'
        elif d100 == 63:
            print('You are a Riverfolk Human Huffer')
            specClass = 'Riverfolk'
            specCareer = 'Huffer'
        elif d100 == 64 or d100 == 65:
            print('You are a Riverfolk Human Riverwarden')
            specClass = 'Riverfolk'
            specCareer = 'Riverwarden'
        elif d100 > 65 and d100 < 69:
            print('You are a Riverfolk Human Riverwoman')
            specClass = 'Riverfolk'
            specCareer = 'Riverwoman'
        elif d100 > 68 and d100 < 71:
            print('You are a Riverfolk Human Seaman')
            specClass = 'Riverfolk'
            specCareer = 'Seaman'
        elif d100 == 71:
            print('You are a Riverfolk Human Smuggler')
            specClass = 'Riverfolk'
            specCareer = 'Smuggler'
        elif d100 == 72 or d100 == 73:
            print('You are a Riverfolk Human Stevedore')
            specClass = 'Riverfolk'
            specCareer = 'Stevedore'
        elif d100 == 74:
            print('You are a Riverfolk Human Wrecker')
            specClass = 'Riverfolk'
            specCareer = 'Wrecker'
        # End of Riverfolk roll range.
        # Start of Rogue roll range.
        elif d100 == 75 or d100 == 76:
            print('You are a Rogue Human Bawd')
            specClass = 'Rogue'
            specCareer = 'Bawd'
        elif d100 == 77:
            print('You are a Rogue Human Charlatan')
            specClass = 'Rogue'
            specCareer = 'Charlatan'
        elif d100 == 78:
            print('You are a Rogue Human Fence')
            specClass = 'Rogue'
            specCareer = 'Fence'
        elif d100 == 79:
            print('You are a Rogue Human Grave Robber')
            specClass = 'Rogue'
            specCareer = 'Grave Robber'
        elif d100 > 79 and d100 < 84:
            print('You are a Rogue Human Outlaw')
            specClass = 'Rogue'
            specCareer = 'Outlaw'
        elif d100 == 84:
            print('You are a Rogue Human Racketeer')
            specClass = 'Rogue'
            specCareer = 'Racketeer'
        elif d100 > 84 and d100 < 87:
            print('You are a Rogue Human Thief')
            specClass = 'Rogue'
            specCareer = 'Thief'
        elif d100 == 88:
            print('You are a Rogue Human Witch')
            specClass = 'Rogue'
            specCareer = 'Witch'
        # End of Rogue roll ranges.
        # Start of Warrior roll ranges.
        elif d100 > 88 and d100 < 91:
            print('You are a Warrior Human Cavalryman')
            specClass = 'Warrior'
            specCareer = 'Cavalryman'
        elif d100 > 91 and d100 < 93:
            print('You are a Warrior Human Guard')
            specClass = 'Warrior'
            specCareer = 'Guard'
        elif d100 == 93:
            print('You are a Warrior Human Knight')
            specClass = 'Warrior'
            specCareer = 'Knight'
        elif d100 == 94:
            print('You are a Warrior Human Pit Fighter')
            specClass = 'Warrior'
            specCareer = 'Pit Fighter'
        elif d100 == 95:
            print('You are a Warrior Human Protagonist')
            specClass = 'Warrior'
            specCareer = 'Protagonist'
        elif d100 > 95 and d100 < 100:
            print('You are a Warrior Human Soldier')
            specClass = 'Warrior'
            specCareer = 'Soldier'
        elif d100 == 100:
            print('You are a Warrior Human Warrior Priest')
            specClass = 'Warrior'
            specCareer = 'Warrior Priest'
    # End Human class/career rolls.
    # Start Dwarf class/career rolls.
    if species == 'Dwarf':
        # Start Dwarf Academic rolls.
        if d100 == 1:
            print('You are an Academic Dwarf Apothecary')
            specClass = 'Academic'
            specCareer = 'Apothecary'
        elif d100 > 1 and d100 < 5:
            print('You are an Academic Dwarf Engineer')
            specClass = 'Academic'
            specCareer = 'Engineer'
        elif d100 == 5 or d100 == 6:
            print('You are an Academic Dwarf Lawyer')
            specClass = 'Academic'
            specCareer = 'Lawyer'
        elif d100 == 7:
            print('You are an Academic Dwarf Physcian')
            specClass = 'Academic'
            specCareer = 'Physcian'
        elif d100 == 8 or d100 == 9:
            print('You are an Academic Dwarf Scholar')
            specClass = 'Academic'
            specCareer = 'Scholar'
        # End Dwarf Academic rolls.
        # Start Dwarf Burgher rolls.
        elif d100 == 10 or d100 == 11:
            print('You are a Burgher Dwarf Agitator')
            specClass = 'Burgher'
            specCareer = 'Agitator'
        elif d100 > 11 and d100 < 18:
            print('You are a Burgher Dwarf Artisan')
            specClass = 'Burgher'
            specCareer = 'Artisan'
        elif d100 == 18:
            print('You are a Burgher Dwarf Beggar')
            specClass = 'Burgher'
            specCareer = 'Beggar'
        elif d100 == 19 or d100 == 20:
            print('You are a Burgher Dwarf Investigator')
            specClass = 'Burgher'
            specCareer = 'Investigator'
        elif d100 > 20 and d100 < 25:
            print('You are a Burgher Dwarf Merchant')
            specClass = 'Burgher'
            specCareer = 'Merchant'
        elif d100 == 25:
            print('You are a Burgher Dwarf Rat Catcher')
            specClass = 'Burgher'
            specCareer = 'Rat Catcher'
        elif d100 > 25 and d100 < 32:
            print('You are a Burgher Dwarf Townsman')
            specClass = 'Burgher'
            specCareer = 'Townsman'
        elif d100 > 32 and d100 < 35:
            print('You are an Burgher Dwarf Watchman')
            specClass = 'Burgher'
            specCareer = 'Watchman'
        # End of Dwarf Burger rolls.
        # Start of Dwarf Courtier rolls.
        elif d100 == 35 or d100 == 36:
            print('You are a Courtier Dwarf Advisor')
            specClass = 'Courtier'
            specCareer = 'Advisor'
        elif d100 == 35 or d100 == 36:
            print('You are a Courtier Dwarf Advisor')
            specClass = 'Courtier'
            specCareer = 'Advisor'
        elif d100 == 37:
            print('You are a Courtier Dwarf ')
            specClass = 'Courtier'
            specCareer = 'Advisor'


species = randomSpecies()
randomClass(species)
