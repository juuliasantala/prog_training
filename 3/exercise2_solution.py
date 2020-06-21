import requests
from requests.auth import HTTPBasicAuth
import dnac_credentials as c

# To remove the InsecureRequestWarnings:
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def get_token():
    url = "https://{}/dna/system/api/{}/auth/token".format(c.DNAC_ADDRESS, c.VERSION)
    header = {"content-type": "application/json"}
    try:
        response= requests.post(url,auth=HTTPBasicAuth(username=c.DNAC_USER,password=c.DNAC_PW), headers=header, verify=False)

        if(not response):
            print ("No token returned!")
        else:
            response_json=response.json()
            token = response_json["Token"]
            return token
    except:
        print( "Error when calling the Token API!")

def get_network_devices(token):
    url = "https://{}/dna/intent/api/{}/network-device".format(c.DNAC_ADDRESS, c.VERSION)
    devices = []
    try:
        header = {"X-Auth-Token": token, "content-type" : "application/json"}
        response = requests.get(url, headers=header, verify=False)

        if(not response):
            print("No data returned!")
        else:
            response_json = response.json()
            for item in response_json["response"]:
                devices.append({
                    "family":item["family"],
                    "hostname":item["hostname"],
                    "id":item["id"]
                })
        return devices
    except:
        print( "Error when calling the network devices API!")

if __name__ == "__main__":
    devices = get_network_devices(get_token())
    for device in devices:
        print("Family {} device with hostname {}".format(device["family"], device["hostname"]))
