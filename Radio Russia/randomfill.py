import random
import readMap

def randomfill(map, signals):
    for state in map:
        if state.signal == 0:
            state.signal = random.choice(signals)
    return map

def random_conflicts(map):
    counter = 0
    for state in map:
        signal = state.signal
        for adjacent_state in state.adjacent_states:
            if signal == adjacent_state.signal:
                counter+= 1
    return counter

with open("randommaps.txt", 'w') as text:
    '''
    zcounter = 0
    min = 100
    for line in text:
        if int(line)== 0:
            zcounter += 1
        if int(line) < min:
            min = int(line)
    print("{},{}".format(zcounter, min))
    '''

    loops = 1000000
    stats = []
    for l in range(loops):
        map = readMap.readStates("Oekraine.txt")
        #print(analyse.analyse_adjacent_states(map))
        signals = ['zA', 'zB', 'zC', 'zD', 'zE', 'zF', 'zG']
        #costs = {'zA':12, 'zB':26, 'zC':27, 'zD':30, 'zE':37, 'zF':39, 'zG':41}

        map = randomfill(map,signals)
        if random_conflicts(map) == 0:
            for state in map:
                text.write(state.signal + ",")
            text.write("\n")

        #sim_an_search.hill_climber(map, costs, signals)
        #freq = analyse.signal_frequentie(map)


