#!/usr/bin/env python3

class Pes:
    jmeno = None
    vek = 1

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self.vek = vek

    def __str__(self):
        return str(f"Jsem pes se jménem {self.jmeno}.")

    def panicek(self, osoba):
        osoba.panicek(self)


    def zestarni(self, vek):
        self.vek = vek
        return f"{self.jmeno} ({vek + 1})"
