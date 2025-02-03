import numpy as np

def extract_sequences(path):
    sequences = {}
    with open(path, 'r') as file:

        n = 0
        header = None
        sequence = []
        counting = True

        for line in file:
            line = line.strip()
            if line[0] == '>':
                header = line[1:]
                if header is not None:
                    counting = False
                    sequences[header] = ''.join(sequence)
                    sequence.clear()
            else:
                if counting:
                    n += len(line)
                sequence.append(line)

    return [sequences,n]

def profile(sequence_dict,n):
    base_map = {
        "A": np.array([[1], [0], [0], [0]]),
        "C": np.array([[0], [1], [0], [0]]),
        "G": np.array([[0], [0], [1], [0]]),
        "T": np.array([[0], [0], [0], [1]])
    }

    profile_matrix = np.zeros((4, n))

    for i in sequence_dict.values():
        print(i)
        for j in range(n):
            profile_matrix[:, j] += base_map[i[j]]

    return profile_matrix

outputs = extract_sequences("example.fasta")
print(outputs[0])
profile_matrix = profile(outputs[0],outputs[1])

print(profile_matrix)


