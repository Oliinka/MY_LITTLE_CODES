from clovek import Clovek

karel = Clovek()
karel.jmeno = "Karel Novák"
karel.vek = 33

cyril = Clovek()
cyril.jmeno = "Cyril Nový"
cyril.vek = 27

print(karel.pozdrav("Cyril Nový"))
print(cyril.pozdrav("Karel Novák"))