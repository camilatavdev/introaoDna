#Código para encontrar os genomas mais comuns dentro de uma string, de acordo com uma determinada quantidade de letras(k)

def frequent_words(text, k):
    word_count = {}
    max_count = 0
    most_frequent_words = []

    for i in range(len(text) - k + 1):

        kmer = text[i:i + k]

        if kmer in word_count:
            word_count[kmer] += 1
        else:
            word_count[kmer] = 1

        if word_count[kmer] > max_count:
            max_count = word_count[kmer]

    for kmer, count in word_count.items():
        if count == max_count:
            most_frequent_words.append(kmer)


    return most_frequent_words

# Exemplo de uso:
text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
k = 4

most_frequent_kmers = frequent_words(text, k)

print(most_frequent_kmers)