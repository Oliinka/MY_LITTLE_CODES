from automobil import NakladniAuto

tatra = NakladniAuto()

tatra.naloz(10000)
tatra.naloz(500)
tatra.vyloz(300)
tatra.vyloz(1000)
print(tatra.nalozeno_celkem())