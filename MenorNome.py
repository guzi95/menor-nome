'''
Esta função recebe uma lista de nomes e informa qual o menor deles.
'''

def menor_nome(lista_nomes):
    
    nomes_corrigidos = []
    for i in range(len(lista_nomes)):
        if lista_nomes[i] != str:  # Se houver objetos diferentes de strings, corrige-os.
            lista_nomes[i] = str(lista_nomes[i])
            
        nomes_corrigidos.append(lista_nomes[i].strip().capitalize())  # Retira espaços em branco nos início e final do nomes e torna maisúcula a letra inicial de cada nome.

    k = len(nomes_corrigidos) - 1 
    comprimento_menor_nome = len(nomes_corrigidos[k])
    menor_nome = ''
    for i in range(len(nomes_corrigidos)):
        if comprimento_menor_nome > len(nomes_corrigidos[i]):  # Verifica qual nome é menor.
            menor_nome = nomes_corrigidos[i]
            comprimento_menor_nome = len(nomes_corrigidos[i])
            
    return menor_nome
            
