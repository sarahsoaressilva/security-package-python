from bs4 import BeautifulSoup
import requests
import operator
from collections import Counter

def start(url):
    wordlist = []

    # pega a url e transforma em texto.
    source = requests.get(url).text

    # transforma em html e separa organizadamente.
    soup = BeautifulSoup(source, 'html.parser')

    # varredura de div. A cada div, ele realizará esse processo.
    # coletará as words dentro das divs.
    for each_text in soup.find_all('div', {'class':'entry-content'} ):
       content = each_text.text
        
       # separa as palavras do conteúdo.
       # as palavras são transformadas em minusculas. 
       words = content.lower().split()

       for each_word in words:
           # para cada palavra separada, é adicionada
           # na lista de wordlists.
           wordlist.append(each_word)
    
    return wordlist


def clean_wordlist(wordlist):
    # lista nova e limpa.
    clean_list = []

    # varredura de simbolos.
    # para cada palavra dentro da lista de words
    # ele irá procurar os simbolos e substituir.
    for word in wordlist:
        symbols = '!@#$%^*-+/\;:<>.,?_()&[{]}|'

        # substitui os simbolos.
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
        
        if len(word) > 0:
            clean_list.append(word)
        
        
    create_dict(clean_list)

def create_dict(cleanlist):
    
    # armazenará o n° de vezes que aparece e a palavra.
    word_count = {}

    # varredura de contagem de palavras.
    for word in cleanlist:
        # se está presente na lista, adiciona 1
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted( word_count.items(), key = operator.itemgetter(1) ):
        print( '%s : %s ' %(key, value) )
    
    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


