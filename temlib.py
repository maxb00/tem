import json
import pdb
from os import path

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

    def getSvString(self):
        string = '['
        for sv in self.sv:
            string += str(sv) + ','
        string = string[:len(string)-1] + ']'
        return string

def loadBox(dex):
    if path.exists('box.txt'):
        box = boxFromFile('box.txt', dex)
        choice = input('Would you like to add more Tems to your saved box? (Y/N)')
        if choice.lower() == 'y':
            box += fillBox(dex)
    else:
        box = fillBox(dex)

    return box


def fillBox(dex):
    # create box
    box = []

    # fill box
    while (usr_input := input('Enter tem data: [Species] [Gender] [hp,sta,spd,atk,def,spatk,spdef] <nickname>\n')) != 'stop':
        # sample input: Yowlar F [46,32,24,42,30,20,15]
        # Yowlar M [50,1,50,50,50,50,50] Yowza
        # Skunch M [1,1,1,1,1,1,1]
        # Skunch F [30,40,13,50,43,49,25] Miocic
        att = usr_input.lower().split(' ')
        if len(att) > 3:
            new_tem = Tem(att[0], att[1], att[2], dex, att[3])
        else:
            new_tem = Tem(att[0], att[1], att[2], dex)


        # covert stats to integer list
        new_tem.sv = new_tem.sv.strip('[]\n').split(',')
        new_tem.sv = [int(i) for i in new_tem.sv]

        # put tem in box
        box.append(new_tem)

    return box

def boxFromFile(filename, dex):
    box = []
    with open(filename) as f:
        lines = f.readlines()

    for line in lines:
        att = line.split(' ')
        if len(att) > 3:
            new_tem = Tem(att[0], att[1], att[2], dex, att[3])
        else:
            new_tem = Tem(att[0], att[1], att[2], dex)

        # covert stats to integer list
        new_tem.sv = new_tem.sv.strip('[]\n').split(',')
        new_tem.sv = [int(i) for i in new_tem.sv]

        # put tem in box
        box.append(new_tem)

    return box

def saveBoxToFile(filename, box):
    with open(filename, 'w') as f:
         for tem in box:
             svs = tem.getSvString()
             f.write(f'{tem.species} {tem.gender} {svs}')
             if tem.nickname != None:
                 f.write(f' {tem.nickname}\n')
             else:
                 f.write('\n')

def getBaby(mother, father, dex):
    stats = []
    for i in range(7):
        # for each stat...
        stat1 = mother.sv[i]
        stat2 = father.sv[i]
        average = (stat1 + stat2) // 2
        stats.append(average)

    baby = Tem(mother.species, '?', stats, dex)
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
            for type in tem.types:
                if type in target.types:
                    fathers.append(tem)
    return fathers

# finds all mothers of target species
def findMothers(box, target):
    mothers = []
    for tem in box:
        if tem.species == target and tem.gender == 'f':
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
