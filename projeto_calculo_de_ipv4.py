# Calcula redes de IPV4
from POO.classes_ip.calcipv4 import CalcIPv4

if __name__ == '__main__':
    calc_ipv4 = CalcIPv4(ip='192.168.0.25', prefixo=24)
    print(f'IP: {calc_ipv4.ip}')
    print(f'Máscara: {calc_ipv4.mascara}')
    print(f'Broadcast: {calc_ipv4.broadcast}')
    # print(f'Prefixo: {calc_ipv4.cidr}')
    print(f'Número de IPs da rede: {calc_ipv4.numero_ips}')
