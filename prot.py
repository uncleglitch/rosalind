def PROT(rna):
    """Translating RNA into Protein"""
    start_codon = 'AUG'
    stop_codons = ['UAA', 'UAG', 'UGA']
    protein_dict = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
                    'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
                    'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
                    'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
                    'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
                    'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
                    'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
                    'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
                    'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
                    'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
                    'CAA':'Q', 'AAA':'K', 'GAA':'E', 'CAG':'Q',
                    'AAG':'K', 'GAG':'E', 'UGU':'C', 'CGU':'R', 
                    'AGU':'S', 'GGU':'G', 'UGC':'C', 'CGC':'R',      
                    'AGC':'S', 'GGC':'G', 'CGA':'R', 'AGA':'R',      
                    'GGA':'G', 'UGG':'W', 'CGG':'R', 'AGG':'R',      
                    'GGG':'G'}

    start_index = rna.find(start_codon)
    proteins = ''
    for i in range(start_index, len(rna), 3):
        codon = rna[i:i+3]
        if codon in stop_codons:
            break
        proteins += protein_dict[codon]
    return proteins
    

if __name__ == "__main__":
    print(PROT("AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA"))