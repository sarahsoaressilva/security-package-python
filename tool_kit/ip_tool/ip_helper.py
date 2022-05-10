import ipaddress

# Soma uma quantidade especifica ao IPv4 ou IPv6 passado.
def soma_ip(ip, n):
    return ipaddress.ip_address(ip) + n

# Esta função imprime todos os ip possíveis dentro de uma network.
def imprime_ip(ip):
    ip_net = ipaddress.ip_network(ip, strict=False)

    for ip in ip_net: 
        print(ip)
 