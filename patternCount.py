#Código para encontrar a quantidade de um padrão genônimo dentro de uma string

def PatternCount(Text, Pattern):
    cont = 0
    pattern_length = len(Pattern)
    text_length = len(Text)

    for i in range(text_length - pattern_length + 1):
        if Text[i:i + pattern_length] == Pattern:
            cont += 1


    return cont

# Exemplo de uso:
Text = "GCGCG"
Pattern = "GCG"

res = PatternCount(Text, Pattern)
print(res)
