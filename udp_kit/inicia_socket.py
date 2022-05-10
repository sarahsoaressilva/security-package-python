import socket
import sys 

def inicia_socket():
    try:
        # protocolo ip, tcp (default), 0 = TCP.
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)

    except socket.error as e: 
        print('A conexão falhou.')
        print(f'Erro: {e}')
        sys.exit() # termina o programa.

    print('\n##### Socket Iniciado com Sucesso.')

    HostAlvo = input('Digite o host/ip a ser conectado: ')
    PortaAlvo = int(input('Digite a porta alvo: '))
    
    try:
        s.connect( (HostAlvo,PortaAlvo) )
        print('\n#### Conexão bem sucedida...')
        print('\n#### Finalizando a conexão...')
        s.shutdown(2)
    except socket.error as e: 
        print('Erro na conexão.')
        print(f'Erro {e}')
        sys.exit()

