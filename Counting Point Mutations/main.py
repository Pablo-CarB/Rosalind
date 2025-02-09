def data_extract(path):
    with open(path,'r') as file:
        str1 = file.readline()
        str2 = file.readline()
    return str1,str2

# given two strings of equal length, computes the hamming distance
def hamming_distance(str1,str2):
    h_distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            h_distance+=1
    return h_distance

seq1,seq2 = data_extract("rosalind_hamm.txt")
print(hamming_distance(seq1,seq2))