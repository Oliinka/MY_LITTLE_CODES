class Clovek:
    jmeno = None
    vek = None
    def pozdrav(self, kamarad):
        self.kamarad = kamarad
        return f"Ahoj, já jsem {self.jmeno}, je mi {self.vek} let a můj kamarád je {kamarad}"
