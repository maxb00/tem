import json
import pdb

def findTypes(species, dex):
    return dex[species]['types']

def findNumber(species, dex):
    return dex[species]['number']

class Tem:
    def __init__(self, species, gender, sv, dex, nickname=None):
        self.species = species
        self.nickname = nickname
        self.gender = gender
        self.sv = sv
        self.types = findTypes(species, dex)
        self.number = findNumber(species, dex)

def fillBox(dex):
    # create box
    box = []

    # fill box
    while (usr_input := input('Enter tem data: [Species] [Gender] [hp,sta,spd,atk,def,spatk,spdef] <nickname>\n')) != 'stop':
        # TODO: automate typing based on species
        # sample input: Yowlar F Neutral None [46,32,24,42,30,20,15]s
        # Yowlar M Neutral None [50,1,50,50,50,50,50] Yowza
        # Skunch M Neutral Melee [1,1,1,1,1,1,1]
        # Skunch F Neutral Melee [30,40,13,50,43,49,25] Miocic
        att = usr_input.lower().split(' ')
        if len(att) > 3:
            new_tem = Tem(att[0], att[1], att[2], dex, att[3])
        else:
            new_tem = Tem(att[0], att[1], att[2], dex, att[3])


        # covert stats to integer list
        new_tem.sv = new_tem.sv.strip('[]').split(',')
        new_tem.sv = [int(i) for i in new_tem.sv]

        # put tem in box
        box.append(new_tem)

    return box

def getBaby(mother, father):
    stats = []
    for i in range(7):
        # for each stat...
        stat1 = mother.sv[i]
        stat2 = father.sv[i]
        average = (stat1 + stat2) // 2
        stats.append(average)

    baby = Tem(mother.name, '?', mother.type1, mother.type2, stats)
    return baby

def evaluatePair(mother, father):
    # returns average case stat total
    stats = []
    for i in range(7):
        # for each stat...
        stat1 = mother.sv[i]
        stat2 = father.sv[i]
        average = (stat1 + stat2) // 2
        stats.append(average)
    return sum(stats)

# finds all fathers that can breed with target species
def findFathers(box, target):
    fathers = []
    for tem in box:
        if tem.gender == 'm':
            if tem.type1 in [target.type1, target.type2]:
                fathers.append(tem)
            elif tem.type2 != None:
                if tem.type2 in [target.type1, target.type2]:
                    fathers.append(tem)
    return fathers

# finds all mothers of target species
def findMothers(box, target):
    mothers = []
    for tem in box:
        if tem.name == target and tem.gender == 'f':
            mothers.append(tem)
    return mothers

def loadDexFromFile(filename):
    with open(filename) as file:
        dex = json.load(file) # dex is dict
    # fix dex
    temp_dex = {}
    for tem in iter(dex):
        temp = dex[tem]
        temp_dex[temp['name'].lower()] = {'types': temp['types'], 'number': temp['number']}

    return temp_dex.copy()
