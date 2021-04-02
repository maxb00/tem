import pdb
import itertools
import temlib

def main():
    dex = temlib.loadDexFromFile('temdex.json')
    box = temlib.fillBox(dex)

    # begin run loop
    while True:
        # ask player which tem they want to breed
        target = input("Which tem do you want to breed?\n").lower()
        if target == 'exit':
            break

        # create a list of all females of target species
        possible_mothers = temlib.findMothers(box, target)

        # create list of eligible suitors
        possible_fathers = temlib.findFathers(box, possible_mothers[0])

        # in list of all father-mother pairs, we want the best average case stat total
        possible_pairs = itertools.product(possible_mothers, possible_fathers)

        best_total = 0
        best_pair = None
        for pair in possible_pairs:
            omega = temlib.evaluatePair(pair[0], pair[1])
            if omega > best_total:
                best_total = omega
                best_pair = pair

        # best pair now holds best pairs
        handleOuts(best_pair, best_total)

    pdb.set_trace()

def handleOuts(pair, total):
    # print pair
    print()
    print('---------------- Results ----------------')
    for tem in pair:
        if tem.nickname != None:
            print(f'{tem.nickname}, {tem.gender}')
        else:
            print(f'{tem.name}, {tem.gender}:')
        print(f'\tHP: {tem.sv[0]}')
        print(f'\tSTA: {tem.sv[1]}')
        print(f'\tSPD: {tem.sv[2]}')
        print(f'\tATK: {tem.sv[3]}')
        print(f'\tDEF: {tem.sv[4]}')
        print(f'\tSPATK: {tem.sv[5]}')
        print(f'\tSPDEF: {tem.sv[6]}')
        print()

    print('--- Baby ---')
    baby = temlib.getBaby(pair[0], pair[1])
    print(f'{baby.name}, {baby.gender}:')
    print(f'\tHP: {baby.sv[0]}')
    print(f'\tSTA: {baby.sv[1]}')
    print(f'\tSPD: {baby.sv[2]}')
    print(f'\tATK: {baby.sv[3]}')
    print(f'\tDEF: {baby.sv[4]}')
    print(f'\tSPATK: {baby.sv[5]}')
    print(f'\tSPDEF: {baby.sv[6]}')
    print()

    print(f'Stat score: {total}')

if __name__ == '__main__':
    main()
