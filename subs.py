def SUBS(dna, fragment):
    """Finding a Motif in DNA"""
    indexes = []
    i = dna.find(fragment)
    while i != -1:
        indexes.append(i + 1)
        i = dna.find(fragment, i + 1)
    return indexes


if __name__ == "__main__":
    indexes = SUBS("GATATATGCATATACTT", "ATAT")
    indexes_string = ' '.join([str(index) + ' ' for index in indexes])
    print(indexes_string)
