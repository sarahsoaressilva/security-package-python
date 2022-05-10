import socket

# executar primeiro o servidor.
def inicia_serverUDP(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('\n##### Socket Criado com Sucesso.')

    host = 'localhost'
    port = 5432

    # ligação entre cliente -> servidor através do host e da porta.
    s.bind( (host, port) )
    print('\n##### Servidor Conectado com Sucesso.')

    while 1:
        dados, end = s.recvfrom(4096)

        if dados: 
            print('\n##### Servidor Enviando Msg.')
            s.sendto(dados + ( msg.encode() ), end)

