class Hose:
    def __init__(self, color, rider):
        self.color = color
        self.owner = rider

class Rider:
    def __init__(self, name):
        self.name = name

mick = Rider("Mick Jagger")
stan = Hose("brown", mick)

print(stan.owner.name)