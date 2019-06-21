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
    - Rangers: Bounty Hunter, Coachman, Entertainer, Flagellant, Messanger, Pedlar, Road Warden, Witch Hunter.
    - Riverfolk: Boatman, Huffer, Riverwarden, Riverwoman, Seaman, Smuggler, Stevedore, Wrecker.
    - Rogues: Bawd, Charlatan, Fence, Grave Robber, Outlaw, Racketeer, Thief, Witch.
    - Warriors: Cavalryman, Guard, Knight, Pit Fighter, Protagonist, Soldier, Slayer, Warrior Priest.
    -----------------------------------------------------------------------------------------------------------\n""")

    d100 = random.randint(1, 100)

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

species = randomSpecies()
randomClass(species)
