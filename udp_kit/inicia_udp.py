import socket

# DGRAM:  UDP - protocolo de datagrama.
# AF_INET: IPv4
# Recebe como parametro uma mensagem para o servidor.
def inicia_clienteUDP(msg):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('\n##### Cliente Socket Criado com Sucesso.')

    host = 'localhost'
    port = 5433
    try:
        print('\n### Empacotando Mensagem Cliente. ')
        s.sendto(msg.encode(), (host, 5432) ) #empacotamento para enviar.

        # 4096 bytes.
        dados, servidor = s.recvfrom(4096)
        dados = dados.decode()

        print('\n### Mensagem Recebida. ')
        print('### Mensagem: ')
        print(dados)
    finally:
         print('\n### Encerrando a conexão.')
         s.close()
    
