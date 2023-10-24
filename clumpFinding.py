#Código de encontrar Clumps

#um "clump" (ou "aglomerado") refere-se a uma região de uma sequência de DNA onde um ou mais padrões específicos, conhecidos como "k-mers"
#(sequências curtas de DNA com um tamanho fixo, k), ocorrem "t" vezes dentro de uma janela de tamanho "L"

def clump_finding(genome, k, L, t):
    clumps = set() #armazena os clumps encontrados

    kmer_count = {} #rastreia a contagem de k-mers

    # Inicialize a contagem de k-mers na primeira janela de L
    for i in range(L - k + 1):
        kmer = genome[i:i + k] 
        if kmer in kmer_count:
            kmer_count[kmer] += 1
        else:
            kmer_count[kmer] = 1


    # Verifique se algum k-mer atende ao critério (L, t)-clump
    for kmer, count in kmer_count.items(): 
        if count >= t: 
            clumps.add(kmer) 

    # Percorra a sequência deslizando a janela de L
    for i in range(1, len(genome) - L + 1): 
        # Remova o k-mer da janela anterior:
        previous_kmer = genome[i - 1:i - 1 + k]
        kmer_count[previous_kmer] -= 1
        if kmer_count[previous_kmer] == 0:
            del kmer_count[previous_kmer]  


        # Adicione o k-mer da nova janela
        current_kmer = genome[i + L - k:i + L] 
        if current_kmer in kmer_count:
            kmer_count[current_kmer] += 1
        else:
            kmer_count[current_kmer] = 1

        # Verifique se algum k-mer atende ao critério (L, t)-clump
        for kmer, count in kmer_count.items():
            if count >= t:
                clumps.add(kmer)

    return clumps

# Função para encontrar todos os padrões distintos em uma string
def find_distinct_patterns(genome, k, L, t):
    patterns = clump_finding(genome, k, L, t)
    return " ".join(patterns)

# Exemplo de uso:
genome = "ACCAACGACCAGCTCTTTCTTGCAGCTTCACGACCCGTCCTATTATCAAGGCCCGGCGACAGTTGTGAGCACCCACCATACCTCCGGTAAGGGTTTACCTTAGGATATTTTGCGTACACTCGTAAAGGAACCCCGCTCTGGCGCATTCCGGATTCCGGAATATTCCGGAGGATCAGAAAAGAAAGGTTCAGAGCCGCGCATTCTGGTACTCAGTAAGAGGTGTTCAGGGCAAAGTAATTATTCGCAAGTCGGGCCGTGAGATCTGATGCGGCGCGGAAGAGACGTCGGTGTGCCGGGATGCGCCCTGCAATGACTCGCGCTTGCAGGGGGTCTCCTCCACCTCTCCACCTCTCCACCTCTCATTTTGAATTGACCATGGAAAGGTTTATCACACAACAATCGTAATTAACTGTCGTGAAAGAACAAGGGAGTGATATGGCATATGACACATAAGTTGCTCGGCGGTTAGAGCGAGAAAACTCCTTCGTAACACGGATAGGCGGGCCGCACGATAAGGCTCAGGAACACTTATAATGACAAGTCGGCTTACCAATTACGTGGAACCCCAGACCTTCAATGCAGACTATAAGTCGTGTATGCCGTACTGCCACAACTGGAGGGGTCAGTTCTATGAATGTGAATATCTGCGATAGGAGTACGTCTATGTTCGGCACACCTGAGACTACACTCACGTATCCTAATTCGCTGCTCGAGCGGGTGGACTTCGAGAATGTGTCTCTATATCGATTGCGCGTGGCGTGCTAGTGCTAGCTAAAGAGAAACTGTGGAGCCTTGATGCTCTTGATTTGACTTGACCCACCCCTTGACCCCTCTTGACCCCAGGATAGAATGCAGCAACAGTATTAAAAATGTACAAGTGTTCTACAGATCCTGTCGGATCCTGTCCTGTGCTTGTTGTTGTCATCATCTGGAGTGCCTTTTGCCTTTCGACCCTATATTGTTCCGTGAAATTGATAGCGAGTCATCAGCACAACTGATCCCGGCAAGTGACACGTTTGCAGCTAGAGCGGCCCTAGACCAGGAAGACCCTTTGGAACTGGTAAGAACTGGTCTGGTGCCTACCTTGTACTCATATTTCCCTCTAGTTGCAGGTATCTCTTAATTCTCGAATACCATCTAACTTCCGTAGAAGCGCCTCCTAACCATCCCGGTCATCCACTCTCACCACATCAGAGCTAACCTCGGCAGCTCTGATACGCTAATTAAATTTCTGAAAGCGGATGAGTCCTCGAGTAGTATTGGGCCTGGGATGTTCAGGGGCTGGGGCTAGGGGCTAGGGGCTAGTGGCGTATGAGGTCTATAGACATATACTATTTTCACGAATGGCCACCTTTACGGTGTCGCACTCCCCTCCCAATATCAACTCCCTCCCAATAGGTCAGAGTCGATAAAGTAAGCGGACATCAGAGAAAGAGAACTTAGCAGGTACGCGCCAGGTACGGTTATTTTATTCGACACTGGTCAACGCCTAATAGTCATAACAGCTCACTCGTCACTCCTAGCTCGCGTAACATCACTGCGCGAGTTTTCACACAATGAAGGAGGGCTGGAATGTATGGTTTCTAAGAAGAAGAGAGGAGGTGATAGATAGTGATAGGTGATAATAGGTCTGGTTATAATCCGCAGTGTTGGATCTCGGATCGTTGGATCGAAGCACTACTCCATACACTCCATTCATTTATTTGACCATTTGACCATTTGACCATTTGACCATTATTTGACCATTTGACCGCCAATTCGCCAATTCGCCAATTCGCCAATTCGCCAATTCGCCAATTCGCCAATTCGCCAATTCGAGGCGGTGAGGCGGTGAGGCGGTGAGGCGGTGAGGCGGTGAGGCGGTGAGGCGGTGAGGCGGT"
k = 8  # Tamanho do k-mer
L = 26  # Tamanho da janela
t = 4  # Número mínimo de ocorrências para formar um (L, t)-clump. Número de vezes que um k-mer deve ocorrer dentro de uma janela L para ser considerado clump

distinct_patterns = find_distinct_patterns(genome, k, L, t)
print(distinct_patterns)
