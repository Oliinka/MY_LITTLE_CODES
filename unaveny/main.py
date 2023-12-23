from clovek import Clovek

karel = Clovek()
print(karel.__str__("Karel Nový", 25))

karel.beh(10)
karel.beh(10)
karel.beh(10)
print(karel.celek())