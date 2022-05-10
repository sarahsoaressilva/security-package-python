from bs4 import BeautifulSoup
import requests


def web_scrap_html(html):
    # recebe o conteúdo da requisição. 
    site = requests.get(html).content

    # 'baixa' o html da variável site.
    soup = BeautifulSoup(site, 'html.parser')

    # exibe em forma de html.
    print( soup.prettify() )

# html = link, objeto = tag, classe = nome da classe.
def web_scrap_finder(html, objeto, classe):
 
    site = requests.get(html).content
    soup = BeautifulSoup(site, 'html.parser')

    # procurar uma parte específica
    achado = soup.find(objeto, class_=classe)

    # converter em string o conteudo.
    print(achado.string)













