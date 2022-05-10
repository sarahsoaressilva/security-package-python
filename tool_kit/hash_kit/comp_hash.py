import hashlib


def comp_hashes(file1, file2):

    hash_1 = hashlib.new('ripemd160')
    hash_1.update( open(file1, 'rb').read() )

    hash_2 = hashlib.new('ripemd160')
    hash_2.update( open(file2, 'rb').read() )

    if hash_1.digest() != hash_2.digest():
        print('#### Os Hashes são Diferentes.')
    else:
        print('#### Os Hashes são Iguais.')

    print(f'Hash do Arquivo 1: {hash_1.hexdigest()}\nHash do Arquivo 2: {hash_2.hexdigest()}')
    print('Encerrando função...\n')


    
