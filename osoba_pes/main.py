#!/usr/bin/env python3

from pes import Pes
from osoba import Osoba

karel = Osoba("Karel Novák", "Azor")
lenka = Osoba("Lenka Nováková", "Azor")

azor = Pes("Azor", 1)

print(karel.pes.zestarni(1))
#print(lenka.pes.zestarni(1))

print(karel.__str__())