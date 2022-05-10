import itertools


def gera_perm(frase):
    # perm = 'String_Teste'
    
    print('Tamanho desejado:')
    print(f'[1]: tamanho da string\n[2]: tamanho a ser informado')
    r = int(input('R: '))
    
    if r == 1: tam_str = len(frase)
    if r == 2: tam_str = int(input('Informe o tamanho: '))
    

    res = itertools.permutations(frase, tam_str)

    for i in res:
        print( ''.join(i) )