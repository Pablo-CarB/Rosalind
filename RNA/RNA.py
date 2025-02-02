with open('rosalind_rna.txt','r') as file:
    DNA = file.read()

RNA = DNA.replace("T", "U")

print(RNA)
