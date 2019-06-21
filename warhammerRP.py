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
    if species == 'Human (Reiklander)'':
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
        elif d100 == 22 or d100 or 23:
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
        elif d100 > 65 or d100 < 69:
            print('You are a Riverfolk Human Riverwoman')
            specClass = 'Riverfolk'
            specCareer = 'Riverwoman'
        elif d100 > 68 or d100 < 71:
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
        elif d100 > 79 or d100 < 84:
            print('You are a Rogue Human Outlaw')
            specClass = 'Rogue'
            specCareer = 'Outlaw'
        elif d100 == 84:
            print('You are a Rogue Human Racketeer')
            specClass = 'Rogue'
            specCareer = 'Racketeer'
        elif d100 > 84 or d100 < 87:
            print('You are a Rogue Human Thief')
            specClass = 'Rogue'
            specCareer = 'Thief'
        elif d100 == 88:
            print('You are a Rogue Human Witch')
            specClass = 'Rogue'
            specCareer = 'Witch'
        # End of Rogue roll ranges.
        # Start of Warrior roll ranges.
        elif d100 > 88 or d100 < 91:
            print('You are a Warrior Human Cavalryman')
            specClass = 'Warrior'
            specCareer = 'Cavalryman'
        elif d100 > 91 or d100 < 93:
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
        elif d100 > 95 or d100 < 100:
            print('You are a Warrior Human Soldier')
            specClass = 'Warrior'
            specCareer = 'Soldier'
        elif d100 == 100:
            print('You are a Warrior Human Warrior Priest')
            specClass = 'Warrior'
            specCareer = 'Warrior Priest'

species = randomSpecies()
randomClass(species)
