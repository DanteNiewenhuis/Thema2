import program

map = program.readStates("Oekraine.txt")
signals = [zA,zB,zC,zD,zE]

def find_empty(map):
    for state in map:
        if(state.adjacent_states == [])
            return state
        else
            return 1
            #something to stop

def set_signal(empty_state)
    possible_signals = signals
    for state in empty_state.adjacent_states:
        if state.signal in signals
            possible_signals.remove(state.signal)



def fill_in(empty_state):
    ##not_adjacent?
    ##minst gebruikte zender heeft voorkeur


def run_hill():
    empty_state = find_empty(map)
    set_signal(empty_state)

