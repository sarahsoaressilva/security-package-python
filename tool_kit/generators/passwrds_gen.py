# Password Generator. 

import random
import string


def inicia_passwordGen():
    print('\n### Iniciando Gerador de Senhas.')
    print('Lembrando que uma boa senha tem por volta de 8 caracteres.\n')
    tam = int(input('Digite o tamanho da senha desejado: '))

    geraSenha(tam)



def geraSenha(tam):
    # string.digits (0 a 9)
    # / /  .ascii_letters (letras diversas)
    chars = string.ascii_letters + string.digits + 'ç!@#$*'
    rnd = random.SystemRandom() # gera numeros aleatorios a partir do SO.

    # para cada valor em TAM, será gerado um caracter randomico.
    print(''.join( rnd.choice(chars) for i in range(tam) ) )



