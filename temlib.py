import json
import pdb
from os import path

evo_lines = {
    'oree': ['oree', 'zaobian'],
    'zaobian': ['oree', 'zaobian'],
    'platypet': ['platypet', 'platox', 'platimous'],
    'platox': ['platypet', 'platox', 'platimous'],
    'platimous': ['platypet', 'platox', 'platimous'],
    'swali': ['swali', 'loali'],
    'loali': ['loali', 'swali'],
    'tateru': ['tateru'],
    'paharo': ['paharo', 'paharac', 'granpah'],
    'paharac': ['paharo', 'paharac', 'granpah'],
    'granpah': ['paharo', 'paharac', 'granpah'],
    'bunbun': ['bunbun', 'mudrid'],
    'mudrid': ['bunbun', 'mudrid'],
    'hidody': ['hidody', 'taifu'],
    'taifu': ['hidody', 'taifu'],
    'fomu': ['fomu', 'wiplump'],
    'wiplump': ['fomu', 'wiplump'],
    'skail': ['skail', 'skunch'],
    'skunch': ['skail', 'skunch'],
    'goty': ['goty', 'mouflank'],
    'mouflank': ['goty', 'mouflank'],
    'rhoulder': ['rhoulder'],
    'houchic': ['houchic', 'tental', 'nagaise'],
    'tental': ['houchic', 'tental', 'nagaise'],
    'nagaise': ['houchic', 'tental', 'nagaise'],
    'orphyll': ['orphyll', 'nidrasil'],
    'nidrasil': ['orphyll', 'nidrasil'],
    'banapi': ['banapi', 'capyre'],
    'capyre': ['banapi', 'capyre'],
    'lapinite': ['lapinite', 'azuroc', 'zenoreth'],
    'azuroc': ['lapinite', 'azuroc', 'zenoreth'],
    'zenoreth': ['lapinite', 'azuroc', 'zenoreth'],
    'bigu': ['bigu', 'babawa'],
    'babawa': ['bigu', 'babawa'],
    'kaku': ['kaku', 'saku'],
    'saku': ['kaku', 'saku'],
    'valash': ['valash'],
    'barnshe': ['barnshe'],
    'gyalis': ['gyalis'],
    'occlura': ['occlura', 'myx'],
    'myx': ['occlura', 'myx'],
    'raiber': ['raiber', 'raize', 'raican'],
    'raize': ['raiber', 'raize', 'raican'],
    'raican': ['raiber', 'raize', 'raican'],
    'pewki': ['pewki', 'piraniant'],
    'piraniant': ['pewki', 'piraniant'],
    'osuchi': ['osuchi', 'osukan', 'osukai'],
    'osukan': ['osuchi', 'osukan', 'osukai'],
    'osukai': ['osuchi', 'osukan', 'osukai'],
    'saipat': ['saipat'],
    'pycko': ['pycko', 'drakash'],
    'drakash': ['pycko', 'drakash'],
    'crystle': ['crystle', 'sherald', 'tortenite'],
    'sherald': ['crystle', 'sherald', 'tortenite'],
    'tortenite': ['crystle', 'sherald', 'tortenite'],
    'hocus': ['hocus', 'pocus'],
    'pocus': ['hocus', 'pocus'],
    'sparzy': ['sparzy'],
    'mushi': ['mushi', 'mushook'],
    'mushook': ['mushi', 'mushook'],
    'magmis': ['magmis', 'mastione'],
    'mastione': ['magmis', 'mastione'],
    'umishi': ['umishi', 'ukama'],
    'raignet': ['raignet'],
    'smazee': ['smazee', 'baboong', 'seismunch'],
    'baboong': ['smazee', 'baboong', 'seismunch'],
    'seismunch': ['smazee', 'baboong', 'seismunch'],
    'zizare': ['zizare'],
    'momo': ['momo'],
    'kuri': ['kuri', 'kauren'],
    'kauren': ['kuri', 'kauren'],
    'spriole': ['spriole', 'deendre', 'cerneaf'],
    'deendre': ['spriole', 'deendre', 'cerneaf'],
    'cerneaf': ['spriole', 'deendre', 'cerneaf'],
    'toxolotl': ['toxolotl', 'noxolotl'],
    'noxolotl': ['toxolotl', 'noxolotl'],
    'blooze': ['blooze', 'goolder'],
    'goolder': ['blooze', 'goolder'],
    'zephyruff': ['zephyruff', 'volarend'],
    'volarend': ['zephyruff', 'volarend'],
    'grumvel': ['grumvel', 'grumper'],
    'grumper': ['grumvel', 'grumper'],
    'ganki': ['ganki', 'gazuma'],
    'gazuma': ['ganki', 'gazuma'],
    'oceara': ['oceara'],
    'yowlar': ['yowlar'],
    'droply': ['garyo', 'droply'],
    'garyo': ['droply', 'garyo'],
    'shuine': ['shuine'],
    'nessla': ['nessla'],
    'valiar': ['valiar'],
    'kalazu': ['kalazu', 'kalabyss'],
    'kalabyss': ['kalazu', 'kalabyss'],
    'adoroboros': ['adoroboros'],
    'tuwai': ['tuwai', 'tukai', 'tuvine', 'turoc'],
    'tukai': ['tuwai', 'tuaki', 'tuvine', 'turoc'],
    'tuvine': ['tuwai', 'tukai', 'tuvine', 'turoc'],
    'turoc': ['tuwai', 'tukai', 'tuvine', 'turoc'],
    'kinu': ['kinu'],
    'vulvir': ['vulvir', 'vulor', 'vulcrane'],
    'vulor': ['vulvir', 'vulor', 'vulcrane'],
    'vulcrane': ['vulvir', 'vulor', 'vulcrane'],
    'pigepic': ['pigepic'],
    'akranox': ['akranox'],
    'koish': ['koish'],
    'vulffy': ['vulffy'],
    'anahir': ['anahir']
}

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
        # sample inputs in box.txt
        att = usr_input.lower().strip('\n').split(' ')
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

    i = 0
    for line in lines:
        att = line.lower().strip('\n').split(' ')
        if len(att) > 3:
            new_tem = Tem(att[0], att[1], att[2], dex, att[3])
        else:
            new_tem = Tem(att[0], att[1], att[2], dex)

        # covert stats to integer list
        new_tem.sv = new_tem.sv.strip('[]\n').split(',')
        new_tem.sv = [int(i) for i in new_tem.sv]

        if len(new_tem.sv) < 7:
            print('issue at line ' + str(i))
        i += 1

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
        if target.lower() in evo_lines[tem.species]:
            if tem.gender == 'f':
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

# what if we are not sure of what to breed?
# get all possible parent pairings with a total score of 250+
def getPairsOfInterest(box, dex, thresh=250):
    # first, make list of all females
    mothers = []
    for tem in box:
        if tem.gender == 'f':
            mothers.append(tem)

    # for each female, create a pair with a possible male
    sig_pairs = []
    scores = []
    for mother in mothers:
        fathers = findFathers(box, mother)
        for father in fathers:
            # score pair. if pair is above thresh, add to sig_pairs
            score = evaluatePair(mother, father)
            if score >= thresh:
                sig_pairs.append(tuple((mother, father)))
                scores.append(score)

    return sig_pairs, scores
