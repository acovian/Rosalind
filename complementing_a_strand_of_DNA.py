test_dna = ""

test_dna = test_dna.replace("C", "g").replace("T", "a").replace("G", "c").replace("A", "t").upper()[::-1]

reversed=''.join(reversed(test_dna))
print(test_dna)
