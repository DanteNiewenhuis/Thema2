class State(object):

    def __init__(self, name):
        self.name = name
        self.adjacent_States = []

    def __iadd__(self, new_State):
        self.adjacent_States.append(new_State)


s1 = State("hello")
s2 = State("bye")
s1 += s2
print(s1._name)


