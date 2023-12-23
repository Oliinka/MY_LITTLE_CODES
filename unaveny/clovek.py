class Clovek:
    jmeno = None
    vek = None
    unava = 0

    def __str__ (self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek
        return f"{jmeno} {vek}"
    def beh(self, vzdalenost):
        self.vzdalenost = vzdalenost
        self.unava = self.unava + vzdalenost
    def spanek(self, cas):
        self.cas= cas
        self.unava = self.unava - cas*10

    def celek (self):
        if self.unava >= 20:
            return "Jsem příliš unavený"
        else:
            return f"Unava je {self.unava}"


