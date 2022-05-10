from ast import arg
from threading import Thread

# Inicia o Start de duas funções paralelamente. 
def inicia_thread(func1, func2, arg1, arg2):

    # Para passar mais de um argumento, utilize listas.
    th1 = Thread(target=func1, args=arg1)
    th2 = Thread(target=func2, args=arg2)

    th1.start()
    th2.start()
