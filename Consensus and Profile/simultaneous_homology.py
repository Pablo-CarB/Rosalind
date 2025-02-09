import numpy as np
import random as rd

# creates a dictionary mapping headers (ie gene names) to sequences both of them being kept as Strings
def extract_sequences(path):
    sequences = {}
    with open(path,'r') as file:
        sequence = []
        header = None

        for line in file:
            line = line.strip()
            if line[0] == '>':
                if header is not None:
                    sequences[header] = ''.join(sequence)
                    sequence.clear()

                header = line[1:]
            else:
                sequence.append(line)

        # this line is needed to save the last sequence & header pair
        sequences[header] = ''.join(sequence)

    n = len(rd.choice(list(sequences.values())))
    return sequences,n

# given an iterable of sequences and a size/depth generates a profile matrix
# any sequences that are shorter than the depth will just contribute what they can,
# and any sequences that are longer than the depth will have their nucleotides ignored past the size/depth limit
def profile(seqs,n):
    base_map = {
        "A": np.array([[1], [0], [0], [0]]),
        "C": np.array([[0], [1], [0], [0]]),
        "G": np.array([[0], [0], [1], [0]]),
        "T": np.array([[0], [0], [0], [1]])
    }

    profile_matrix = np.zeros((4, n), dtype=int)

    for i in seqs:
        for j in range(n):
            profile_matrix[:, j:j+1] += base_map[i[j]]

    return profile_matrix

# given an iterable of sequences and a depth/size, will generate a consensus sequence among them,there could be several
def consensus(seqs,n):
    consensus_string = ""
    pos_map = {"A": 0, "C": 1, "G": 2, "T": 3}
    for i in range(n):
        consensus_arr = [0,0,0,0]
        for j in seqs:
            try:
                consensus_arr[pos_map[j[i]]] += 1
            except IndexError:
                pass
        consensus_string += consensus_arr



def main():
    with open("example.fasta") as file:
        print(file.read())

    outputs = extract_sequences("example.fasta")
    profile_matrix = profile(outputs[0], outputs[1])
    print(profile_matrix)


if __name__ == "__main__":
    main()


