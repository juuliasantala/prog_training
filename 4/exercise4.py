import requests

#Do disable warnings about not verifying SSL certificate
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#API key for the DevNet sandbox Meraki
API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
BASE_URI = "api.meraki.com/api/v1"

def get_organizations():
    '''
    Function to get all the network devices from the DNA Center.
    Needs token for authorization.
    Returns the model, hostname and ID of the device.

    '''
    url = "https://{}/organizations".format(BASE_URI)
    headers = {
        'X-Cisco-Meraki-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    organizations = response.json()
    return organizations

def get_organization_devices(org):
    '''
    Function to get all the interfaces of a network device.
    Needs token for authorization.
    Returns the received devices.
    '''
    url = "https://{}/organizations/{}/devices".format(BASE_URI, org)
    headers = {
        'X-Cisco-Meraki-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    devices = response.json()
    return devices

def main():
    organizations = get_organizations()
    for org in organizations:
        if org["name"] == "DevNet Sandbox":
            devices = get_organization_devices(org["id"])
            print("Devices in {}:".format(org["name"]))
            for device in devices:
                print("Model: {}, Serial: {}".format(device["model"], device["serial"]))

if __name__ == "__main__":
    main()
