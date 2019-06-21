#! /usr/bin/python3
# Simple Warhammer Fantasy Role Play Character Generator
# By Nicholas Coletta, in the year 2019.
# www.github.com/statusquonjc46 for plenty of other python things that may or may not be useful to you. Also my IT490 full stack project lol.

import random

# d100 = random.randint(1, 100)
species = ''
specClass = ''
career = ''
print("""- Welcome to the Warhammer Fantasy RolePlay(WFRP) game character generator.
- Everything you find in this script is from the 4th edition of WFRP.
- If you would like to follow along with the prompts, I will try to accurately label each prompt with its corresponding page in the book.
- Enjoy, and may the d100 be with you.""")


def randomSpecies():
    print("""- First we are going to roll for your species.
    - This is done with a d100.
    - Human falls in the range of 1-90.
    - Halfling falls in the range of 91-94.
    - Dwarf falls in the range of 95-98.
    - High Elf is 99.
    - Wood Elf is 100.
    - This can be found on page 24 of the 4th Edition Guide."""\n\n)

    d100 = random.randint(1, 100)
    print(f'You rolled a {d100}.\n')
    if d100 > 0 and d100 < 91:
        print('You got: Human (Reiklander)!'\n)
        return 'Human (Reiklander)'
    elif d100 > 90 and d100 < 95:
        print('You got: Halfling!'\n)
        return 'Halfling'
    elif d100 > 94 and d100 < 99:
        print('You got: Dwarf!'\n)
        return 'Dwarf'
    elif d100 == 99:
        print('You got: High Elf!'\n)
        return 'High Elf'
    elif d100 == 100:
        print('You got: Wood Elf!'\n)
        return 'Wood Elf'

def randomClass(species):
    species = species
    print("""\n- Next we will roll for your class and career.
    - The following list is the class followed by the career. I won't be typing out the details on what can be what, so please reference pages 30 and 31 of the guide.
    - I will have the correct stops in place for species not being able to be certain careers, etc.
    - Academics: Apothecary, Engineer, Lawyer, Nun, Physcian, Priest, Scholar, Wizard.
    - Burghers: Agitator, Artisan, Beggar, Investigator, Merchant, Rat Catcher, Townsman.
    - Courtiers: Advisor, Artist, Duelist, Envoy, Noble, Servant, Spy, Warden.
    - Peasants: Baliff, Hedge Witch, Herbalist, Hunter, Miner, Mystic, Scout, Villager.
    - Rangers: Bounty Hunter, Coachman, Entertainer, Flagellant, Messanger, Pedlar, Road Warden, Witch Hunter.
    - Riverfolk: Boatman, Huffer, Riverwarden, Riverwoman, Seaman, Smuggler, Stevedore, Wrecker.
    - Rogues: Bawd, Charlatan, Fence, Grave Robber, Outlaw, Racketeer, Thief, Witch.
    - Warriors: Cavalryman, Guard, Knight, Pit Fighter, Protagonist, Soldier, Slayer, Warrior Priest.\n""")

    d8 = random.randint(1, 8)
    d100 = random.randint(1, 100)

    if d8 == 1:
        specClass = 'Academics'
    elif d8 == 2:
        specClass == 'Burghers'
    elif d8 == 3:
        specClass == 'Courtiers'
    elif d8 == 4:
        specClass == 'Peasants'
    elif d8 == 5:
        specClass == 'Rangers'
    elif d8 == 6:
        specClass == 'Riverfolk'
    elif d8 == 7:
        specClass == 'Rogues'
    elif d8 == 8:
        specClass == 'Warriors'

    if species == 'Human (Reiklander)' and specClass == 'Academics':
        if d100 == 1:
            print('You are an Academic Human Apothecary')
            return 'Apothecary'
        elif d100 == 2:
            print('You are an Academic Human Engineer')
            return 'Engineer'
        elif d100 == 3:
            print('You are an Academic Human Lawyer')
            return 'Lawyer'
        elif d100 == 4 or d100 == 5:
            print('You are an Academic Human Nun')
            return 'Nun'
        elif d100 == 6:
            print('You are an Academic Human Physcian')
            return 'Physcian'
        elif d100 > 6 or d100 < 12:
            print('You are an Academic Human Priest')
            return 'Priest'
        elif d100 == 12 or d100 == 13:
            print('You are an Academic Human Scholar')
            return 'Scholar'
        elif d100 == 14:
            print('You are an Academic Human Wizard')
            return 'Wizard'
