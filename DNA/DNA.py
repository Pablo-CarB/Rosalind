with open('rosalind_dna.txt','r') as file:
    DNA = file.read()

base_count = {'A' : 0, 'T' : 0, 'G' : 0, 'C' : 0}

for base in DNA:
    if base in base_count:
        base_count[base] += 1

print(f"{base_count['A']} {base_count['C']} {base_count['G']} {base_count['T']}")
