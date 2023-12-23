# automobil.py

class NakladniAuto:
    nosnost = 3000
    naklad = 0

    def naloz(self, naklad):
        self.naklad += naklad
        return self._check_and_return()

    def vyloz(self, naklad):
        self.naklad -= naklad
        return self._check_and_return()

    def nalozeno_celkem(self):
        return f"V nákladním autě je celkem naloženo {self.naklad} kg"

    def _check_and_return(self):
        if 0 <= self.naklad <= self.nosnost:
            return f"V nákladním autě je naloženo {self.naklad} kg"
        else:
            return f"Nevyloženo!"

# main.py

from automobil import NakladniAuto

tatra = NakladniAuto()

tatra.naloz(10000)
tatra.naloz(500)
tatra.vyloz(300)
tatra.vyloz(1000)
print(tatra.nalozeno_celkem())