import requests

#Do disable warnings about not verifying SSL certificate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

DNAC_ADDRESS = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PW = "Cisco123!"

def get_token(password, username):
    '''
    Function to get DNA Center token.
    Returns the token to be used with other API calls to authorize the call.
    '''

    url = "https://{}/dna/system/api/v1/auth/token".format(DNAC_ADDRESS)
    authentication = requests.auth.HTTPBasicAuth(username=username,password=password)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST",
                                url,
                                auth=authentication,
                                headers=headers,
                                verify=False)
    token = response.json()["Token"]
    return token

def get_devices(token):
    '''
    Function to get all the network devices from the DNA Center.
    Needs token for authorization.
    Returns the model, hostname and ID of the device.
    '''

    url = "https://{}/dna/intent/api/v1/network-device".format(DNAC_ADDRESS)
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    devices = response.json()
    device_list = []
    for device in devices["response"]:
        device_info = {
            "id":device["id"],
            "model":device["platformId"],
            "hostname":device["hostname"]
            }
        device_list.append(device_info)

    return device_list

def get_interfaces(token, device):
    '''
    Function to get all the interfaces of a network device.
    Needs token for authorization.
    Returns the received devices.
    '''

    url = "https://{}/dna/intent/api/v1/interface/network-device/{}".format(DNAC_ADDRESS, device)
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    interfaces = response.json()
    return interfaces["response"]

def print_interfaces(token, selected_device):
    '''
    Print in CLI the info of selected device: interface names and status.
    Device information and DNAC token provided as an argument.
    Token needed for the API call to get the interface info with get_interfaces().
    '''
    interfaces = get_interfaces(token, selected_device["id"])
    print("\nInterfaces of {}:\n".format(selected_device["hostname"]))
    for interface in interfaces:
        if interface["className"] == "SwitchPort":
            print("{}: {}".format(interface["portName"], interface["status"]))

def main():
    token = get_token(DNAC_PW, DNAC_USER)
    devices = get_devices(token)
    print("The switches in the network: ")
    for index, device in enumerate(devices):
        print("{}. {} ({})".format(index+1, device["model"], device["hostname"]))

    while True:
        value = input("\nSelect number from which you would like to know the port utilisation (number or end): ")
        if value.strip().isdigit():
            try:
                print_interfaces(token, devices[int(value)-1])
            except IndexError as error: print(error)
        elif value.strip() == "end":
            break
        else:
            print("Please type a number!")
    print("Thank you for using the application")

if __name__ == "__main__":
    main()
