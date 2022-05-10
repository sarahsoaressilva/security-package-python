# Importa módulo/biblioteca OS (integra os recursos do Sistema Operacional)
import os
import time


def ping_simples():
    print('\nIniciando ping_simples()\n')
    ipHost = input("Digite o IP ou Host a Ser Verificado: ")
    
    try:
        qtd = int(input("Digite a Quantidade de Pacotes: "))
    except:
        print('Ocorreu algum erro de digitação.')
        print('Numero de pacotes padrão = 4')
        qtd = 4

    # -n : numero de pacotes.
    # 6  : quantidade de pacotes.
    os.system(f'ping -n {qtd} {ipHost}')



# Recebe como parametro um arquivo ('nome_do_arquivo.extensao').
def ping_multiplo(arquivo):
    with open(arquivo) as file:
        dump = file.read()

        # Toda vez que tiver \n, ele separa o conteúdo e forma uma lista.
        dump = dump.splitlines()

        for ip in dump:
            print('\n##### Testando: ' + ip)
            os.system('ping -n 2 ' + ip )

            print('\n#### Encerrando.')

            if ip != dump[-1]:
                print('\n#### Preparando-se para a próxima sequencia.')
            
            time.sleep(5)

