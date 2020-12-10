import requests
import pprint

DNAC_ADDRESS = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PW = "Cisco123!"

def get_token(password, username):
    '''
    Function to get DNA Center token.
    Returns the token to be used with other API calls to authorize the call.
    '''

    url = "https://{}/dna/system/api/v1/auth/token".format(DNAC_ADDRESS)
    authentication = requests.auth.HTTPBasicAuth(username=username, password=password)
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, auth=authentication, headers=headers, verify=False)
    token = response.json()["Token"]
    return token

def get_devices(token):
    '''
    Function to get all the network devices from the DNA Center.
    Needs token for authorization.
    Returns the received devices.
    '''
    url = "https://{}/dna/intent/api/v1/network-device".format(DNAC_ADDRESS)
    headers = {
        'X-Auth-Token': token,
        'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers, verify=False)
    devices = response.json()
    return devices

def main():
    token = get_token(DNAC_PW, DNAC_USER)
    pprint.pprint(get_devices(token))

if __name__ == "__main__":
    main()
