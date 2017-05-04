import State

def readStates(data):
    states = []
    with open(data, 'r') as info:
        for state in info:
            split_state = state.split(',')
            x = State.State(split_state[0], split_state[1])
            states.append(x)
    make_adjecent_states(data, states)
    return states

def make_adjecent_states(data, states):
    counter = 0
    with open(data, 'r') as info:
        for state in info:
            split_state = state.split(',')
            for adjecent_state in split_state[2:]:
                adjecent_state = find_state(adjecent_state.rstrip(), states)
                states[counter] += adjecent_state
            counter += 1

def find_state(name, states):
    for state in states:
        if(state.code == name):
            return state

def read_complete_map(name):
    map = []
    with open(name, 'r') as text:
        for line in text:
            split_line = line.split(',')
            x = State.State(split_line[0],split_line[1])
            x.signal = split_line[2]
            map.append(x)
    with open(name, 'r') as text:
        for line in text:
            split_line = line.split(',')
            for adj in split_line[3:-1]:
                adj_state = find_state(adj.rstrip(), map)
                state = find_state(split_line[1], map)
                state += adj_state
    return map
