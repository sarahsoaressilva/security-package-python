import phonenumbers 
from phonenumbers import geocoder


def identifica_telefone(phone):
    # Converte para telefone.
    phone_n = phonenumbers.parse(phone)
    print(f'Numero: {phone_n}')

    # Detecta o lugar.
    l = geocoder.description_for_number(phone_n, 'pt')
    print(l)