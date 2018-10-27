class Vogn:
    def __init__(self, type, antSeter):
        self._type = type
        self._antSeter = antSeter
        #print("Vogn opprettet med type", type, "og seter", antSeter)

    def getAntSeter(self):
        return self._antSeter
