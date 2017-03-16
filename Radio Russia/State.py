class State(object):

    def __init__(self, name):
        self.name = name
        self.adjacent_states = []

    def __iadd__(self, new_state):
        print(new_state.name)
        self.adjacent_states.append(new_state)
        return self

    def __repr__(self):
        return "State:{}".format(self.name)

x = []
y = State("hoi")
z = State("dag")
x.append(y)
x.append(z)
print(x[0].adjacent_states)

x[0] += x[1]

x[0].adjacent_states.append(5)
print(x[0].adjacent_states)
