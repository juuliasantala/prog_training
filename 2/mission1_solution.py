# an example solution for mission 1, session 1

interface = "GigabitEthernet1/0/1"
status = "up"
vlan = "20"

print("The interface {} has status {} and VLAN {}.".format(interface, status, vlan))

decision = int(input("Select 1 to change status and 2 to change VLAN: "))

if decision == 1:
    status = "down"
elif decision == 2:
    vlan = input("Which VLAN would you like to have? ")
else:
    print("The selection {} is invalid.".format(decision))

print("Now the interface {} has status {} and VLAN {}.".format(interface, status, vlan))
print("Thank you for using the application!")
