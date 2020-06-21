# an example solution for mission 3, session 3
import mission3_netconf as nc

def print_interface_vlan_and_status(interface_info):
    interface = interface_info["name"]
    vlan = interface_info["vlan"]
    return "The interface {} has VLAN {}.".format(interface, vlan)

def print_all_interfaces(interface_list):
    i = 1
    for interface in interface_list:
        print("{}. {}".format(i, print_interface_vlan_and_status(interface)))
        i = i+1


def main():
    while True:
        interfaces = nc.get_interfaces()
        print_all_interfaces(interfaces)
        try:
            selected_interface = int(input("\nwhich interface do you want to work with? "))-1
            print("Got it, configuring interface {}!".format(interfaces[selected_interface]["name"]))
        except IndexError:
            print("That is not an available interface! Please select another.")
            continue
        except ValueError:
            print("Please provide a number!")
            continue

        while True:
            try:
                new_vlan = input("Which VLAN would you like to have? ")
                int(new_vlan)
            except ValueError:
                print("Please provide a number!")
                continue
            else:
                break

        nc.change_vlan(interfaces[selected_interface]["name"], new_vlan)
        print("Vlan has been changed!")
        decision = input("Do you want to continue changing VLANs? (yes/no)")
        if decision == "yes":
            continue
        elif decision == "no":
            print("Thank you for using the application!")
            break
        else:
            print("Unknown selection, shutting down the program.")
            break

if __name__ == "__main__":
    main()
