#!/usr/bin/env python3

import random

class GeneratorVet:
    privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
    podmety = ["jednorožec", "programátor", "manažer", "hroch", "T-rex"]
    prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
    slovesa = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
    mista = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    def privlastek(self):
        return random.choice(self.privlastky)
    def podmet(self):
        return random.choice(self.podmety)
    def prislovec(self):
        return random.choice(self.prislovce)
    def sloveso(self):
        return random.choice(self.slovesa)
    def misto(self):
        return random.choice(self.mista)

