import json
from urllib.request import urlopen


def info_ip(url):
    # abrir a url e jogar a requisição para a resposta.
    resp = urlopen(url)

    # o json irá carregar o JS da resposta e jogar para os dados.
    dados = json.load(resp)

    dict_dados = {
        'ip': dados['ip'],
        'hostname': dados['hostname'],
        'city': dados['city'],
        'region': dados['region']
    }

    print(dict_dados)