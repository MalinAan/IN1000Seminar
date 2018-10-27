from tog import Tog

class Togstasjon:
    def __init__(self, maxAntTog):
        self._tog = []
        self._maxAntTog = maxAntTog
        #print("Togstasjon opprettet med plass til", maxAntTog)

    def leggTilTog(self, nyttTog):
        self._tog.append(nyttTog)

    def antVogner(self):
        antVogner = 0
        for tog in self._tog:
            antVogner += tog.antVogner()
        return antVogner

    def totalKapasitet(self):
        antSeter = 0
        for tog in self._tog:
            antSeter += tog.antSeterPaaToget()
            print("Seter til et tog", tog.antSeterPaaToget())

        return antSeter

    def printTogSomHarNokSeter(self, minAntallSeter):
        print("Tog som har minst", minAntallSeter, "seter:")
        for tog in self._tog:
            if(minAntallSeter <= tog.antSeterPaaToget()):
                tog.printInfo()
