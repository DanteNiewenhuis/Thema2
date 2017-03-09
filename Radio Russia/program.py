import State

def readStates(data):
    states = []
    with open(data, 'r') as info:
        for state in info:
            split_state = state.split(',')
            x = State.State(split_state[0])
            states.append(x)
    states = make_adjecent_states(data, states)
    return states

def make_adjecent_states(data, states):
    counter = 0
    with open(data, 'r') as info:
        for state in info:
            split_state = state.split(',')
            for adjecent_state in split_state:
                adjecent_state = find_state(adjecent_state.rstrip(), states)
                states[counter] += adjecent_state
            counter += 1
    return states

def find_state(name, states):
    for state in states:
        if(state.name == name):
            return state

x = readStates("Oekraine.txt")
for state in x:
    print("state = " + state.name)
    print(state.adjacent_states)
