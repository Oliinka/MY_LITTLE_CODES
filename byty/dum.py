class Dum:
    def __init__(self, pocet_bytu=5):
        self.pocet_bytu = pocet_bytu
        self.obyvatele = [None] * pocet_bytu

    def __str__(self):
        result = ""
        for i, obyvatel in enumerate(self.obyvatele):
            if obyvatel is not None:
                result += f"V bytě číslo {i} je {obyvatel}\n"
            else:
                result += f"Byt číslo {i} je na prodej\n"
        return result.strip()

    def __setitem__(self, index, hodnota):
        self.obyvatele[index] = hodnota

    def __getitem__(self, index):
        return self.obyvatele[index]