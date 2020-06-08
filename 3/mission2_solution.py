# an example solution for mission 2, session 2
import json

def read_file(filename):
    with open(filename) as file:
        return file.read()

def get_json_data(json_file):
    json_text = read_file(json_file)
    data = json.loads(json_text)
    interfaces = data["response"]
    interface_list = []
    for interface in interfaces:
        if interface["speed"] == "1000000" and interface["interfaceType"]!="Virtual":
            name = interface["portName"]
            vlan = interface["vlanId"]
            status = interface["status"]
            interface_list.append({"name":name, "vlan":vlan, "status":status})
    return interface_list

def print_interface_vlan_and_status(interface_info):
    interface = interface_info["name"]
    status = interface_info["status"]
    vlan = interface_info["vlan"]
    return "The interface {} has status {} and VLAN {}.".format(interface, status, vlan)

def print_all_interfaces(interface_list):
    i = 1
    for interface in interface_list:
        print("{}. {}".format(i, print_interface_vlan_and_status(interface)))
        i = i+1

def change_interface_status(current_status):
    if current_status == "down":
        new_status = "up"
    else:
        new_status = "down"
    return new_status

def main():
    json_file = "mission_response.json"

    interfaces = get_json_data(json_file)
    print_all_interfaces(interfaces)

    while True:
        try:
            selected_interface = int(input("which interface do you want to work with? "))-1
            print("Got it, configuring interface {}!".format(interfaces[selected_interface]["name"]))
        except IndexError:
            print("That is not an available interface! Please select another.")
            continue
        except ValueError:
            print("Please provide a number!")
            continue
        else:
            try:
                decision = int(input("Select 1 to change status and 2 to change VLAN: "))
            except ValueError:
                print("Please provide a number!")
                continue
            break

    if decision == 1:
        status = interfaces[selected_interface]["status"]
        interfaces[selected_interface]["status"] = change_interface_status(status)
    elif decision == 2:
        interfaces[selected_interface]["vlan"] = input("Which VLAN would you like to have? ")
    else:
        print("The selection {} is invalid.".format(decision))

    print(print_interface_vlan_and_status(interfaces[selected_interface]))
    print("Thank you for using the application!")

if __name__ == "__main__":
    main()
