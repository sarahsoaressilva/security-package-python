import webbrowser
from tkinter import *


def abrir_motores_pesquisa():

    root = Tk()
    root.title('Abrir Browser')
    root.geometry('300x200')

    # abre o site quando executado.
    def google(): webbrowser.open('www.google.com')
    def bing(): webbrowser.open('www.bing.com')
    def yahoo(): webbrowser.open('https://br.search.yahoo.com/')

    # variável que guardará o botão.
    mygoogle = Button(root, text='Abrir Google', command=google).pack(pady=20)
    mybing = Button(root, text='Abrir Bing', command=bing).pack(pady=20)
    myyahoo = Button(root, text='Abrir Yahoo Search', command=yahoo).pack(pady=20)

    # aberto até o usuário fechar.
    root.mainloop()


