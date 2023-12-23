class Kalkulacka:
    def pozdrav(self, a, b):
        self.a = a
        self.b = b
        return f"""
Součet: {a + b}
Rozdíl: {a-b}
Součin: {a*b}
Podíl: {a/b}"""