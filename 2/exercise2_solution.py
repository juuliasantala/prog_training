# an example solution for exercise 2, session 2

from netmiko import ConnectHandler
import exercise2_module_solution as C

device = {
    'device_type':'cisco_xe',
    'host':C.HOST,
    'username':C.USERNAME,
    'password':C.PASSWORD,
    'port':8181,          # optional, defaults to 22
    'secret':C.SECRET,     # optional, defaults to ''
}

net_connect = ConnectHandler(**device)

output = net_connect.send_command('show ip int brief')
print(output)
