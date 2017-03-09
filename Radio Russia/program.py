import State.py

def readStates(data):
    states = []
    with open(data, 'r') as info:
        for state in info:
            x = State.State(state[0])
            states.append(x)
    states = make_adjecent_states(data, states)
    return states

def make_adjecent_states(data, states):
    counter = 0
    with open(data, 'r') as info:
        for state in info:
            adjecent_state in state[1:]:
                states[counter] += adjecent_state
            counter++
    return states

x = readStates("Oekraine.txt")

