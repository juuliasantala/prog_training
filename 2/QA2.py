#Tehtävä 1, sessio 2
numbers = [1, 5, 3, 7, 10, 11, 45, 2, 14]
for number in numbers:
    if number > 10:
        print("iso numero")
    elif number == 10:
        print("Napakymppi!")
    else:
        print("pieni numero")

#Tehtävä 2, sessio 2
from netmiko import ConnectHandler
import netmiko_router as N

net_connect = ConnectHandler(**N.router)
output = net_connect.send_command('show ip int brief')
print(output)
