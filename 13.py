#последний ip компьютера
from ipaddress import *
ip= ip_address("68.203.243.87")
m = ip_address("255.255.224.0")
net = ip_network(f"{ip}/{m}", 0)
print(net[-2])
print(68 + 203 + 255+254)

#номер компьютера. находится над нулями маски. нужно перевести в десятичную систему
from ipaddress import *
mask = ip_address('255.255.255.248')
ip = ip_address('156.128.0.227')
print(bin(int(ip))[2:])
print(bin(int(mask))[2:])
print(int('011', 2))

#количество ип для которых выполняется условие
from ipaddress import*
a = ip_network('234.151.74.12/255.255.128.0', 0)
k=0
for i in a:
    if (bin(int(i)))[2:].count('1')%7 != 0:
        k+=1
print(k)


from ipaddress import*
ip='143.131.211.37'
for mask in range(30,1,-1):
    net=ip_network(f'{ip}/{mask}',0)
    k=0
    for x in net:
        x=bin(int(x))[2:]
        if x.count('1')==10:
            k+=1
    if k==15:
        print(mask)
        break
