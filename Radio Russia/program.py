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

def readCost(name):
    with open(name, "r") as cost_table:
        return [[int(i) for i in line.split(",")] for line in cost_table]


x = readStates("Oekraine.txt")
cost_table = readCost("kosten.txt")
cost_type = 0
