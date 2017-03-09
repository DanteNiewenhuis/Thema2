class Cost(object):

    def __init__(self, name):
        self.name = name
        self.adjacent_States = []

    def __iadd__(self, new_State):
        self.adjacent_States.append(new_State)

