def extract_data(path):
    sequences = {}
    with open(path, 'r') as f:
        head = None
        seq = []
        for line in f:
            line = line.strip()
            if line[0]=='>':
                if head is not  None:
                    sequences[head] = ''.join(seq)
                    seq.clear()
                head = line[1:]
            else:
                seq.append(line)

        sequences[head] = ''.join(seq)
    
    return sequences

# returns the name of the sequence as well as the GC content of the sequence [0,1]
def gc_content(sequences):
    maxKey = ""
    maxVal = 0
    for key,value in sequences.items():
        gc_count = 0
        for i in value:
            if i == "G" or i == "C":
                gc_count += 1
        gc_percentage = gc_count/len(value)
        if(gc_percentage >= maxVal):
            maxVal = gc_percentage
            maxKey = key
    
    return maxKey,maxVal


seq = extract_data("rosalind_gc.txt")
print(seq)
gc_data = gc_content(seq)

#prints sequence title and percentage of GC
print(gc_data[0])
print(gc_data[1]*100)

            

