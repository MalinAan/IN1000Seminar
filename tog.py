from vogn import Vogn

class Tog:
    def __init__(self, type):
        self._type = type
        self._vogner = []
        #print("Tog opprettet med type", type)

    def leggTilVogn(self, nyVogn):
        self._vogner.append(nyVogn)

    def antSeterPaaToget(self):
        antSeter = 0
        for vogn in self._vogner:
            antSeter += vogn.getAntSeter()
        return antSeter

    def printInfo(self):
        print("Tog av type", self._type, "med", self.antVogner(), "vogner med totalt", self.antSeterPaaToget(), "seter")

    def antVogner(self):
        return len(self._vogner)
