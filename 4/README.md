# Hands-on material for session 4

While going through the reading material from DevNet learninglabs marked for this session, try things out in the interactive python shell in terminal! Try out what happens when you change values. Then practice with the following exercises. For the practice exercises, try to solve those by yourself before the Q&A. The solution files will be added here after we have covered them in the Q&A session. Remember, the solutions are just examples on how you could solve the exercises, there are different ways to do things!

**Reading material:**
- DevNet: [Introduction to Ansible](https://developer.cisco.com/learning/modules/sdx-ansible-intro)
- DevNet: [Cisco DNA Center API overview](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav4-intro-dnac/dne-dnac-api-overview/step/1)


**Additional reading material if you are interested in more APIs**
- DevNet: [Cisco SD-WAN programmability](https://developer.cisco.com/learning/modules/sd-wan)
- DevNet: [Cisco Meraki programmability](https://developer.cisco.com/learning/modules/getting-started-with-meraki)

**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)
- [Exercise 4](#exercise-4)

Remember to activate the virtual environment, and never work outside of it. You can use the same environment through out the sessions, and activate it by using source together with the part to your environments "activate" functionality. Here is an example of creating a virtual environment and activating it:

Mac:
```
$ python3 -m venv session3_exercises
$ source session3_exercises/bin/activate

```
Windows:
```
$ py -3 -m venv session3_exercises
$ source session3_exercises/Scripts/activate

```

You need to create the virtual environment only once, after that you just use source to activate it.

### Exercise 1

Create an application using http://restcountries.eu/ API! The idea is that your user can ask to get some information of a country by writing the country's name.

Start by trying this out in Postman, and after that you can use the "code" functionality to get an example of Python code using **requests** Python library. You can remove the payload and headers (you would see in documentation if headers and payload was needed). Use json() method on the response to transform it from JSON to Python datatype. This is a built in feature of requests library. In the end therefor the API call would be simply:
```Python
response = requests.request("GET", url)
print(response.json())
```

Once you have the API call working in your code, create your application around it! Ask from the user what country they want information of, and print out the information you want to provide.

**Example output:**
```
$ python exercise1.py
Please select country or write 'end'
What country would you like to know more about? finland
Found 1 countries:

Finland (Suomi)
Capital: Helsinki
Population: 5491817
Languages: 1. Finnish 2. Swedish

Please select country or write 'end'
What country would you like to know more about? africa
Found 2 countries:

Central African Republic (Ködörösêse tî Bêafrîka)
Capital: Bangui
Population: 4998000
Languages: 1. French 2. Sango

South Africa (South Africa)
Capital: Pretoria
Population: 55653654
Languages: 1. Afrikaans 2. English 3. Southern Ndebele 4. Southern Sotho 5. Swati 6. Tswana 7. Tsonga 8. Venda 9. Xhosa 10. Zulu

Please select country or write 'end'
What country would you like to know more about? mycountry
404 not a valid country code.
Please select country or write 'end'
What country would you like to know more about? end
```

### Exercise 2

Work on the DNA Center APIs! You can use the DevNet Sandbox always-on DNA Center, if you do not have access to a lab DNA Center.
Sandbox credentials:
```Python
DNAC_ADDRESS = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PW = "Cisco123!"
```

Start by getting the token, as you need that to authenticate yourself.

Once you've got your token, get all the network devices. Once you have parsed the response from JSON to Python data structure, loop through the items and print the fammily and hostname of each of the returned devices on the screen.

Check the [DNA Center API documentation](https://developer.cisco.com/docs/dna-center/api/1-3-3-x/) to find the correct API to use for getting token and network devices.

**TIP**
Requests can ignore verifying the SSL certificate if you set verify to False (check the [example file]( ./rest_dnac_example.py)). This will however throw you a warning everytime you do the API call. By adding the following in the beginning of your code, you can remove the InsecureRequestWarnings:
```Python
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```

**Example output:**
```
$ python exercise2.py
Family Routers device with hostname asr1001-x.abc.inc
Family Switches and Hubs device with hostname cat_9k_1.abc.inc
Family Switches and Hubs device with hostname cat_9k_2.abc.inc
Family Switches and Hubs device with hostname cs3850.abc.inc
```

### Exercise 3

Continue working with DNA Center APIs. We have been successful in getting all of the network devices in the previous exercise. Now utilise this information, and get all the interfaces of the device that the user selects!

How can you filter the list of interfaces and print out only the physical interfaces? Study the JSON to see what key holds the value that can be used to define this.

Check the [DNA Center API documentation](https://developer.cisco.com/docs/dna-center/api/1-3-3-x/) to find the correct API to use for getting interface info by device id.

**Example output:**
```
$ python exercise3.py
The switches in the network:
1. C9300-24UX (cat_9k_1)
2. C9300-24UX (cat_9k_2)

Select number from which you would like to know the port utilisation (number or end): 2

Interfaces of cat_9k_2:

FortyGigabitEthernet1/1/1: down
FortyGigabitEthernet1/1/2: down
GigabitEthernet1/1/1: down
GigabitEthernet1/1/2: down
GigabitEthernet1/1/3: down
GigabitEthernet1/1/4: down
TenGigabitEthernet1/0/1: down
TenGigabitEthernet1/0/2: down
TenGigabitEthernet1/0/3: down
TenGigabitEthernet1/0/4: down
TenGigabitEthernet1/0/5: down
TenGigabitEthernet1/0/6: down
TenGigabitEthernet1/0/7: down
TenGigabitEthernet1/0/8: down
TenGigabitEthernet1/0/9: down
TenGigabitEthernet1/0/10: down
TenGigabitEthernet1/0/11: down
TenGigabitEthernet1/0/12: down
TenGigabitEthernet1/0/13: down
TenGigabitEthernet1/0/14: down
TenGigabitEthernet1/0/15: down
TenGigabitEthernet1/0/16: down
TenGigabitEthernet1/0/17: down
TenGigabitEthernet1/0/18: down
TenGigabitEthernet1/0/19: down
TenGigabitEthernet1/0/20: down
TenGigabitEthernet1/0/21: down
TenGigabitEthernet1/0/22: down
TenGigabitEthernet1/0/23: down
TenGigabitEthernet1/0/24: up
TenGigabitEthernet1/1/1: up
TenGigabitEthernet1/1/2: down
TenGigabitEthernet1/1/3: down
TenGigabitEthernet1/1/4: down
TenGigabitEthernet1/1/5: down
TenGigabitEthernet1/1/6: down
TenGigabitEthernet1/1/7: down
TenGigabitEthernet1/1/8: down

Select number from which you would like to know the port utilisation (number or end): 10
list index out of range

Select number from which you would like to know the port utilisation (number or end): one
Please type a number!

Select number from which you would like to know the port utilisation (number or end): end
Thank you for using the application
```

### Exercise 4

Try out Cisco Meraki APIs. You can find from DevNet Sandboxes an always-on Meraki Sandbox if you don't have access to your own Meraki environment.
To use Meraki APIs, you need an API key. Compared to DNA Center, Meraki is a cloud service, therefor we don't have IP address or domain name for our own Meraki. Instead of that, use the Meraki base URI in your API calls.
Sandbox credentials:
```Python
API_KEY = "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
BASE_URI = "api.meraki.com/api/v1"
```

Check Meraki [API documentation](https://developer.cisco.com/meraki/api-v1/v).
Meraki docmentation is a swagger, meaning that you can try out the API calls directly in the documentation. Note that the sandbox API key is already as a default key in the documentation, so you can try to run the API calls against the sandbox.

Under General section you can find an API to get all the devices in an organization. You will notice that the URI requires the ID of the organization: in the documentation you can also find an API to get that ID. On the right side of the documentation you will also be able to see what kind of headers you need (pay attention to especially what name Meraki uses for the API key.)

When getting the organizations, you will get all of those in the Sandbox lab. A good organization for this exercise is named "DevNet Sandbox", I recommend you to define in your script that it will find the ID of this organization to be used in the API call that fetches the devices.

**Example output:**
```
$ python exercise4.py
Devices in DevNet Sandbox:
Model: MR84, Serial: Q2EK-S3AA-BXFW
Model: MR84, Serial: Q2EK-SARE-UUBY
Model: MV12WE, Serial: Q2FV-4QSY-KBF6
Model: MV12WE, Serial: Q2FV-TG7N-MF4E
Model: MV12WE, Serial: Q2FV-W72R-U7WX
Model: MS225-24P, Serial: Q2GW-2CA5-RW6A
Model: MS225-24P, Serial: Q2GW-2CPC-JCYZ
Model: MS225-24P, Serial: Q2GW-2WW9-LLZC
Model: MS220-8P, Serial: Q2HP-AJ22-UG72
Model: MS220-8P, Serial: Q2HP-F5K5-R88R
Model: MS220-8P, Serial: Q2HP-Q9S8-BVHB
Model: MS220-8P, Serial: Q2HP-TQPZ-M5LP
Model: MS220-8P, Serial: Q2HP-WH5E-MK7H
Model: MR32, Serial: Q2JD-CAF3-Y6G2
Model: MR32, Serial: Q2JD-N9K5-3QRB
Model: MR53, Serial: Q2MD-9PJD-E9L7
Model: MR53, Serial: Q2MD-BHHS-5FDL
Model: MR53, Serial: Q2MD-C3CG-4DBC
Model: MR53, Serial: Q2MD-MFNY-6L6H
Model: MR53, Serial: Q2MD-Y5QK-LAK2
Model: MX64W, Serial: Q2MN-R73U-YZ8M
Model: MR33, Serial: Q2PD-2S5P-WFC5
Model: MX84, Serial: Q2PN-JRAG-STZY
Model: MX84, Serial: Q2PN-PSMX-KDDC
Model: MX84, Serial: Q2PN-WWNM-JRAS
Model: MX65, Serial: Q2QN-9J8L-SLPD
Model: MX65, Serial: Q2QN-WPR6-UJPL
Model: MX65, Serial: Q2QN-WS5Y-DN8E
Model: MX65, Serial: Q2QN-XPL2-2MPN
Model: MR30H, Serial: Q2RD-4YLL-CSUN
Model: MR30H, Serial: Q2RD-4ZSU-DLC6
```
