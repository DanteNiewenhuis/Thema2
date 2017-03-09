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
            for adjecent_state in split_state[1:]:
                states[counter] += adjecent_state
            counter += 1
    return states

x = readStates("Oekraine.txt")
for state in x:
    print("state = " + state.name)
    print(state.adjacent_States)
