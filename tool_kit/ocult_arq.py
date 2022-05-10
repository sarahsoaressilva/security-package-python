import ctypes


# path = caminho do arquivo.
def oculta_arq(path):
    # atributo para ocultar de acordo com a biblioteca.
    att_ocultar = 0x02
    
    # atribui a caracteristica de oculto ao arquivo passado.
    r = ctypes.windll.kernel32.SetFileAttributesW(path, att_ocultar)

    if r:
        print('Arquivo Ocultado com Sucesso...')
    else:
        print('Arquivo não foi ocultado. Tente novamente.')