#Ratkaisu tehtävään 1

def tulosta_muuttuja(muuttuja):
    print("muuttuja: {}, tyyppi: {}".format(muuttuja, type(muuttuja)))

muuttuja1 = 9000
muuttuja2 = "Catalyst"
muuttuja3 = 3.5

tulosta_muuttuja(muuttuja1)
tulosta_muuttuja(muuttuja2)
tulosta_muuttuja(muuttuja3)

#Ratkaisu tehtävään 2
print("play a game!")
numero = int(input("Choose a number: "))
if numero == 10:
    print("Hienosti valittu!")
else:
    print("Väärä valinta")

#Ratkaisu tehtävään 3
def summaus(n1, n2):
    summa = n1 + n2
    print("numeroiden {} ja {} summa on {}".format(n1, n2, summa))

numero1 = int(input("Choose a number one: "))
numero2 = int(input("Choose a number two: "))
summaus(numero1, numero2)


#Ratkaisu tehtävään 4
name = "GigabitEthernet1/0/1"
status = "down"
vlan = 30

print("The interface {} has status {} and VLAN {}".format(name, status, vlan))
decision = int(input("Select 1 to change status, 2 to change VLAN: "))
if decision == 1:
    if status == "down":
        status = "up"
    else:
        status = "down"
elif decision == 2:
    vlan = int(input("Choose vlan: "))
else:
    print("Wrong number")

print("The interface {} has now status {} and VLAN {}".format(name, status, vlan))
