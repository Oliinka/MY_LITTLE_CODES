from kouzlo import Kouzlo
from mag import Mag

# Vytvoříme kouzla
ohniva_koule = Kouzlo("Ohnivá koule", "ohnive")
kletba_smrti = Kouzlo("Kletba Smrti", "temne")
absolutni_nula = Kouzlo("Absolutní Nula", "vodni")
manipulace_zive_energie = Kouzlo("Manipulace Živé Energie", "cista")

# Vytvoříme kouzelníka
gandalf = Mag("Gandalf", "voda")


scenarios = [
(f"{gandalf.jmeno} se nyní specializuje na {gandalf.typ} "),
(f"{gandalf.jmeno} použil kouzlo {absolutni_nula.nazev} "),
(f"{gandalf.jmeno} nemůže použít {kletba_smrti.nazev} s typem poškození {kletba_smrti.typ} "),
(f"{gandalf.jmeno} se nyni specializuje na temna"),
(f"{gandalf.jmeno} použil kouzlo Kletba Smrti"),
(f"{gandalf.jmeno} nemůže použít Manipulace Živé Energie s typem poškození cista"),
(f"{gandalf.jmeno} se nyni specializuje na ohen"),
(f"{gandalf.jmeno} použil kouzlo Ohnivá koule")
]


# Iterate through scenarios and print statements
for scenario in scenarios:
    print(f"{gandalf.jmeno} {scenario[0]}", end=" ")

    print()

for scenario in scenarios:
    print(f"{gandalf.jmeno} {scenario[0]}", end=" ")
    for i in range(1, len(scenario), 2):
        print(f"{scenario[i]}", end=" ")
        if i + 1 < len(scenario):
            print(f"{gandalf.jmeno} {scenario[i + 1]}", end=" ")
    print()