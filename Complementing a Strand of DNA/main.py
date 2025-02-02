

def extract_data(path):
    try:
        with open(path, 'r') as file:
            seq = file.read().strip()
    except FileNotFoundError:
        print("ERROR: file does not seem to exist")
    return seq

def reverse_complement(seq):
    complement = []

    convert = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

    for base in reversed(seq):
        try:
            complement.append(convert[base])
        except KeyError:
            print(f"ERROR: DNA is not well formatted there exists a \"{base}\" character in the data")
            return None

    return ''.join(complement)


DNA = extract_data("rosalind_revc.txt")
if DNA is not None:
    reverse_complement = reverse_complement(DNA)
    if reverse_complement is not None:
        print(reverse_complement)
