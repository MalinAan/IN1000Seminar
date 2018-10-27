from tog import Tog
from togstasjon import Togstasjon
from vogn import Vogn

def hovedprogram():
    # Lage datastruktur
    ts = Togstasjon(5)

    tog1 = Tog("persontog")
    ts.leggTilTog(tog1)
    tog1.leggTilVogn(Vogn("ordinaer", 50))
    tog1.leggTilVogn(Vogn("stille", 30))
    tog1.leggTilVogn(Vogn("ordinaer", 55))

    tog2 = Tog("persontog")
    ts.leggTilTog(tog2)
    tog2.leggTilVogn(Vogn("ordinaer", 50))
    tog2.leggTilVogn(Vogn("komfort", 25))

    tog3 = Tog("godstog")
    ts.leggTilTog(tog3)
    tog3.leggTilVogn(Vogn("last", 0))
    tog3.leggTilVogn(Vogn("last", 0))

    # Finne antall vogner.
    print("Antall vogner", ts.antVogner())

    # Finne antall seter

    print("Total kapasitet(antall seter)", ts.totalKapasitet())

    #tog1.printInfo()

    # Finne tog som har nok seter
    ts.printTogSomHarNokSeter(60)


hovedprogram()
