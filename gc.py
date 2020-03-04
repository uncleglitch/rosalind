def calculateGC(nts):
    """Computing GC Content"""
    gc_counter = 0
    for nt in nts:
        if nt is 'C' or nt is 'G':
            gc_counter += 1
    return gc_counter / len(nts) * 100


def GC(filename):
    data_dict = {}
    with open(filename) as f:
        lines = f.readlines()
        name_of_set = ''
        for line in lines:
            if line.startswith('>'):
                name_of_set = line[1:-1]
                data_dict[name_of_set] = ''
            else:
                data_dict[name_of_set] += line[:-1]
    gc_dict = {}
    for name_of_set, data in data_dict.items():
        gc_dict[name_of_set] = calculateGC(data)
    
    max_gc = 0
    name_of_set_with_max_gc = ''
    for name_of_set, gc in gc_dict.items():
        if gc > max_gc:
            max_gc = gc
            name_of_set_with_max_gc = name_of_set
    print(name_of_set_with_max_gc)
    print(max_gc)
    

if __name__ == "__main__":
    GC("data.txt")