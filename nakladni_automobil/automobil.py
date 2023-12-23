class NakladniAuto:
    nosnost = 3000
    naklad = 0
    def naloz (self, naklad):
        if self.naklad + naklad <= self.nosnost:
            self.naklad += naklad
            return f"V nákladním autě je naloženo {self.naklad} kg"
        else:
            return f"Nenaloženo! Překročena nosnost."

    def vyloz (self, naklad):
        if self.naklad - naklad < 0:
            return f"Nelze vyložit! Záporný náklad"
        else:
            self.naklad -= naklad
            return f"Vyloženo."

    def nalozeno_celkem (self):
        if 0 <= self.naklad <= self.nosnost:
            return f"V nákladním autě je naloženo {self.naklad} kg"
        else:
            return f"Nevyloženo!"
