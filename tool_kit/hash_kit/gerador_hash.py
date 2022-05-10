import hashlib 

# Retorna um hash do conteúdo de acordo com a escolha
def gera_hash():
    # Dicionario de objetos disponiveis para conversão.
    conteudos = {
        1:'string',
        2:'arquivo'
    }

    r = 0

    while r not in conteudos.keys():
        print('\nEscolha o tipo de conteúdo a ser convertido:')
        print('[1]: string\n[2]: arquivo')
        r = int(input('R: ')) # recebe um novo valor de r pelo usuário.

        if r > 2: print('Valor inválido!')

    # Dicionario de Hashes Disponíveis.
    hashes = {
        1:'md5',
        2: 'sha1',
        3: 'sha256',
        4:'sha512'
    }

    # Escolha Hash.
    print('\nEscolha o tipo de hash:')
    print(f'1:{hashes[1]} \
    \n2:{hashes[2]} \
    \n3:{hashes[3]} \
    \n4:{hashes[4]}'
    )

    esc = int(input('R: '))

    # Inicia Hash.
    if esc == 1: res = hashlib.md5()
    if esc == 2: res = hashlib.sha1()
    if esc == 3: res = hashlib.sha256()
    if esc == 4: res = hashlib.sha512()

    if r == 1:
        uso = input('Insira a string:\nR: ')

        # transforma a string em bytes.
        uso = uso.encode('utf-8')
        # atualiza o md5.
        res.update(uso)
    else:
        file1 = input('Insira o caminho do arquivo abaixo:\nR: ')

        # Teste de caminho de arquivo.  
        # file1 = 'C:/Users/learn/Downloads/Materiais/Programação/Python/Python/Dio_Cognizant/Criação_de_Pacotes/security_package/tool_kit/arq_testes/a.txt'
            
        # .read() lê o conteúdo do arquivo.
        uso = open(file1, 'rb').read()
        res.update(uso)

    # Retorna o Hash.
    print( res.hexdigest() ) 