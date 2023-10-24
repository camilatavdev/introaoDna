#Código para encontrar o complemento reverso de uma sequência de nucleotídeos

def reverse_complement(sequence):

    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}

    reverse_comp = [complement[base] for base in reversed(sequence)]

    return "".join(reverse_comp)

#Exemplo de uso:

sequence = "CCAGATC"

reverse_comp_sequence = reverse_complement(sequence)

print("Reverse complement:", reverse_comp_sequence)
