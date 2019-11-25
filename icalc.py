import pegpy

peg = pegpy.grammar("Math.tpeg")
parser = pegpy.generate(peg)

t = parser("1+2")
print(repr(t))

t = parser("1@2")
print(repr(t))

