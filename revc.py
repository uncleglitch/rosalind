def REVC(nts):
    """Complementing a Strand of DNA"""
    complement = ""
    for nt in nts:
        if nt is 'A':
            complement += 'T'
        elif nt is 'T':
            complement += 'A'
        elif nt is 'C':
            complement += 'G'
        elif nt is "G":
            complement += "C"
    return complement[::-1]

if __name__ == "__main__":
    print(REVC("AGGGCTGCTACTAGGGCAGGTCTCGACGAGACACTTCTGCGAGAGTCTTTGAAGTGCTGCACTAGAACATCAGCGAGTGTCGTGTGGCAACGGTCGATCGAAGGTAGGGGATTTACGGAGGTATAACTCCAACCGGGATACCCCCGCCATCAATGCCAGTCAACGGCATTGGATCGGAGATTTGAGTTTCGGTGCCCTGATTTAACAAAAGCCGTAGCGAAGCCGCAAACCAGTGGAGGGAAGACTCGTTGAGCACCAAACTCTTGCGGATACATGCCATCAAACGATACATGCTCGCAAGCTGTCAAAAGGTCCTCGTATCGACCAGTGATAAACGGTGGATCGTCGATGTCGACAAGCCTCAAAGCTTTGAGCGCTTTATTGTCGCATGGCGCATATGGTAGTGTAACTTTTAGATTCGACTCTTCCTACATCGGGAACTCGTAACAGTTCCACTCTGGACCAACACATATCTCTTAGAGACAGTCCTTCCTCGTCGCGTCAGGAGGAGCACGGCGCGGGTAGCCCAATTAACGGACATTATGAAAGCGAGTGTTGTGTCAAGTGTGCACACCATTAATGTAGCCTATACCTGGCTTGGGAACTAGCATTCAAGTTAGTCCTATCTGAGAAGATGAGTTGACGTCATTCGACGGCGGCTCTGTCGAGGCGAGCAAACCAGATTAGCAGTCAACCAGTCCCTATGTTTAGACTAGACTCGTGGCGTAGTTCAAAAGGGGTCGTAACTACCTAGATCGCTTTCAATTCTTGATGCCCTCCAGTTTCATTCGCCATATGCGCCCGAGACACTTGTCAAATCGTTTTGGGGGAGAAGAGCC"))