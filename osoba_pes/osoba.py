#!/usr/bin/env python3

class Osoba:
    def __init__(self, jmeno, pes):
        self.jmeno = jmeno
        self.pes = pes

    def __str__(self):
        return str(f"Jsem {self.jmeno} a můj pes je {self.pes}.")

    def adopce(self, pes):
        self.pes=pes


