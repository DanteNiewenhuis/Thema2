class State(object):

    def __init__(self, name):
        self.name = name
        self.adjacent_states = []
        self.signal = 0

    def __iadd__(self, new_state):
        self.adjacent_states.append(new_state)
        return self

    def __repr__(self):
        return self.name

