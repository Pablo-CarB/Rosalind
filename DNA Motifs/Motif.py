
def extract_data(path):
    with open(path,'r') as file:
        seq = file.readline().strip()
        motif = file.readline().strip()
    return [seq,motif]

def find_motif(motif,seq):
    motif_list = []
    if len(seq) < len(motif):
        raise ValueError(f"the motif length ({len(motif)}) cannot be longer than the sequence length ({len(seq)})")

    for i in range(len(seq) - len(motif)):
        if seq[i:i+len(motif)] == motif:
            motif_list.append(i+1)

    return motif_list

def format_list(motif_list):
    output = ""

    for i in range(len(motif_list)):
        output += str(motif_list[i]) + " " if i < len(motif_list) - 1 else str(motif_list[i])

    return output


outputs = extract_data("rosalind_subs.txt")
print(format_list(find_motif(outputs[1], outputs[0])))

