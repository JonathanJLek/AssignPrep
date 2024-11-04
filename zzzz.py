# FILE where i test things
import random
NUCLEOTIDES_DNA = ['A','C','G','T']

dna_line = []
dna_file = open("DNA_FILE.txt", 'w')
for y in range(0,50):
    for x in range(0,50): 
        dna_line.append(random.choice(NUCLEOTIDES_DNA))
    dna_line.append('\n')
    dna_file.write(''.join(dna_line))
    dna_line = []