#!/usr/bin/env python3

from generator_vet import GeneratorVet

generator = GeneratorVet()
# Zde dokonči úlohu svým kódem...
for _ in range(10):
    sentence = f"{generator.privlastek()} {generator.podmet()} {generator.prislovec()} {generator.sloveso()} {generator.misto()}"
    print(sentence)
