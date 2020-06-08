# Hands-on material for session 3
Smaller exercises with examples and the mission.

**Reading material:**
- [Optional] Recap info covered in the session 3:
  - DevNet: [Cisco DNA Center API overview](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav4-intro-dnac/dne-dnac-api-overview/step/1)
  - DevNet: [What and why of Model Driven Programmability](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-why-mdp/step/1)
  - DevNet: [Exploring IOS XE YANG Data Models with NETCONF](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-intro-netconf/step/1)

- Self study, will not be covered in the session:
  - DevNet: [Exploring IOS XE YANG Data Models with RESTCONF](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-intro-restconf/step/1)
  - DevNet: [Introduction to the Guest Shell](https://developer.cisco.com/learning/lab/intro-guestshell/step/1)
  - DevNet: [Introduction to On-Box Python](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-guestshell/dnav3-intro-on-box-python/step/1)
  
- If you didn't yet do it, familiarise yourself with error handling: https://realpython.com/python-exceptions/
  
**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)
- [Mission 3/3](#mission-33)

## Small exercises
You can work on the small exercises on either interactive python shell in terminal (python / py -i), or save them as python files and run them with python script.py / py script.py.
Remember to activate the virtual environment, and never work outside of it. To create a virtual environment for session 3 exercises, you can do for example:

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

Create an app that utilises the https://api.chucknorris.io/ Chuck Norris API you tried out in Postman!
You can start by just creating a REST API call to retrieve a Chuck Norris joke. Once you got that working, make the program a little bit more complicated: Let the user decide which category they want to get the joke from. You can do this by getting the categories with an API, listing them for the user and asking their input, then using the selected category as an argument when getting the joke. Add also error handling with try-except, and a loop to let the user to get more than one joke if they so wish!

### Example output:
```
$ python exercise1.py
Welcome to the Chuck Norris joke application!
Available categories:
1. animal
2. career
3. celebrity
4. dev
5. explicit
6. fashion
7. food
8. history
9. money
10. movie
11. music
12. political
13. religion
14. science
15. sport
16. travel
Which category joke would you like to hear? Select a number! 6
Here is your joke:
Chuck Norris does not follow fashion trends, they follow him. But then he turns around and kicks their ass. Nobody follows Chuck Norris.
Would you like to hear another joke? (yes/no) yes
Welcome to the Chuck Norris joke application!
Available categories:
1. animal
2. career
3. celebrity
4. dev
5. explicit
6. fashion
7. food
8. history
9. money
10. movie
11. music
12. political
13. religion
14. science
15. sport
16. travel
Which category joke would you like to hear? Select a number! 4
Here is your joke:
Chuck Norris knows the last digit of PI.
Would you like to hear another joke? (yes/no) no
```


### Exercise 2

Try out the DNA Center APIs! You can use the DevNet Sandbox always-on DNA Center, if you do not have access to a lab DNA Center.
Sandbox credentials:
```Python
DNAC_ADDRESS = "sandboxdnac.cisco.com"
DNAC_USER = "devnetuser"
DNAC_PW = "Cisco123!"
```

Start by getting the token, as you need that to authenticate yourself.

Once you've got your token, get all the network devices. Once you have parsed the response from JSON to Python data structure, loop through the items and print the fammily and hostname of each of the returned devices on the screen.

**TIP**
By adding this in the beginning of your code, you can remove the InsecureRequestWarnings:
```Python
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
```


### Example output:
```
$ python exercise2.py
Family Routers device with hostname asr1001-x.abc.inc
Family Switches and Hubs device with hostname cat_9k_1.abc.inc
Family Switches and Hubs device with hostname cat_9k_2.abc.inc
Family Switches and Hubs device with hostname cs3850.abc.inc
```


### Exercise 3

Continue the previous exercise. DNA Center provides health information for network components.
Now, save also the ID of the all the returned devices. Loop through all the devices and fecth their health information (overall, memory, CPU) with device-detail API.
```
$ python exercise3.py
asr1001-x.abc.inc has following health scores:
Overall health: 10
Memory health: 10
CPU health: 10

cat_9k_1.abc.inc has following health scores:
Overall health: 10
Memory health: 10
CPU health: 10

cat_9k_2.abc.inc has following health scores:
Overall health: 10
Memory health: 10
CPU health: 10

cs3850.abc.inc has following health scores:
Overall health: 10
Memory health: 10
CPU health: 10
```


## Mission 3/3

In the mission 1/3 and 2/3 we started creating a simple app which changes a single interface status and VLAN, first for one interface and then for many from JSON. In the final week, we will update our small application to change VLAN value in real life over Netconf. You can continue with the file you created last time, or use the solution file provided on this page (mission2_solution.py).

To simplify the work with YANG datamodels, we focus only on changing the VLAN information, and leave status out of the program.

Remember: Don't try to create the whole application on one go, rather create some of the parts, test it by running the it, and then add more.

Place all the different functionalities in separate functions that you call from your main function.

**I personally reserved the "IOS XE on Catalyst 9000 16.12 EFT Code" sandbox from DevNet for this exercise. If you cannot work on real equipment, I would recommend to reserve a sandbox.**
--> [DevNet sandboxes](https://devnetsandbox.cisco.com/RM/Topology?c=14ec7ccf-2988-474e-a135-1e90b9bc6caf)

1. First, create a function that creates a netconf connection to a switch and retrieves the interface information. Check that the function works for example by printing the outcome. The YANG models to be utilised are the Cisco native models "Cisco-IOS-XE-native" and "Cisco-IOS-XE-switch" (which extends the first model). Review for IOS XE 17.1.1 [here](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1711/Cisco-IOS-XE-native.yang) and [here](https://github.com/YangModels/yang/blob/master/vendor/cisco/xe/1711/Cisco-IOS-XE-switch.yang). If you find challenging defining the filter, please see below.

2. Once the function to retrieve information works, transform the xml data into Python data structure. Check how the response is formed, and loop through all the interfaces. While looping through them, create a dictionary of the name and vlan of the interface and add those to a list, like we did in 2/3 for JSON file information. Note that (depending on which switch you are working with) not all interfaces have VLAN defined. Before saving VLAN information to the dictionary, check that it exists. See below an example. Finally, return the list of interfaces and their VLAN information.

3. Now that you have a function to get information from the switch, create a function to change VLAN information! First you can use static values when testing your function. The function should take two arguments: the name of the interface to be changed and the vlan number. Once the function works with static values, you can start implementing it to the code we created in previous weeks. If you have challenges in creating the config string, please see below.

4. Modify the code from 2/3 so that it doesn't involve anymore the part for the status. We still want to first print out all the interfaces, and provide the number by which user chooses which interface they want to work with. Once the user has selected the interface, ask which VLAN they want to choose, and call the function defined in step 3 to actually do that change!

5. Once the program works, you can put it into a loop, and ask from the user if they want to end or modify another interface VLAN.

6. Add error handling! How can we prevent the program crashing if the user selects an interface that is not in the list? Or doesn't type numbers when we ask for it? Or creates a VLAN with a number that is not a valid VLAN number?

7. Separate your netconf related functions into own file, and import it to your main code. Separate also the credentials to another file, and import them to the code where needed.

**Filters:**
To get the interfaces:
```xml
<filter>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"> <interface>
<GigabitEthernet>
<name/>
<switchport>
<access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch" />
</switchport>
</GigabitEthernet>
</interface>
</native>
</filter>
```

To update the VLAN info (note the placeholders for interface name and VLAN)
```xml
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
<interface>
<GigabitEthernet>
<name>{}</name>
<switchport>
<access xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-switch">
<vlan><vlan>{}</vlan></vlan>
</access>
</switchport>
<description> Configured by NETCONF </description>
</GigabitEthernet>
</interface>
</native>
</config>
```

**Tips:**
Surviving the nested XML data once it is parsed into a Python dictionary:
```Python
interfaces = interfaces["data"]["native"]["interface"]["GigabitEthernet"]
    for item in interfaces:
    ...
```

How do I prevent my program from crashing when there is no VLAN defined for the interface? One solution is to utilise the try-except error handling!
```Python
try:
    vlan = item["switchport"]["access"]["vlan"]["vlan"]
except KeyError:
    vlan = None
```

How do I change information with Netconf? Create the connection like you would when getting information, but now instead of m.get_config you would use the following (note the config instead of filter):
```Python
m.edit_config(source="running", config=config)
```

### Example output:
```
$ python mission3.py
1. The interface 1/0/10 has VLAN None.
2. The interface 1/0/11 has VLAN None.
3. The interface 1/0/12 has VLAN None.
4. The interface 1/0/13 has VLAN None.
5. The interface 1/0/14 has VLAN None.
6. The interface 1/0/15 has VLAN None.
7. The interface 1/0/16 has VLAN 98.
8. The interface 1/0/17 has VLAN None.
9. The interface 1/0/18 has VLAN None.
10. The interface 1/0/19 has VLAN None.
11. The interface 1/0/2 has VLAN None.
12. The interface 1/0/20 has VLAN None.
13. The interface 1/0/21 has VLAN None.
14. The interface 1/0/22 has VLAN None.
15. The interface 1/0/23 has VLAN None.
16. The interface 1/0/24 has VLAN None.
17. The interface 1/0/25 has VLAN 13.
18. The interface 1/0/26 has VLAN None.
19. The interface 1/0/27 has VLAN None.
20. The interface 1/0/28 has VLAN None.
21. The interface 1/0/29 has VLAN None.
22. The interface 1/0/3 has VLAN None.
23. The interface 1/0/30 has VLAN None.
24. The interface 1/0/31 has VLAN None.

which interface do you want to work with? 3
Got it, configuring interface 1/0/12!
Which VLAN would you like to have? 15
Vlan has been changed!
Do you want to continue changing VLANs? (yes/no)yes
1. The interface 1/0/10 has VLAN None.
2. The interface 1/0/11 has VLAN None.
3. The interface 1/0/12 has VLAN 15.
4. The interface 1/0/13 has VLAN None.
5. The interface 1/0/14 has VLAN None.
6. The interface 1/0/15 has VLAN None.
7. The interface 1/0/16 has VLAN 98.
8. The interface 1/0/17 has VLAN None.
9. The interface 1/0/18 has VLAN None.
10. The interface 1/0/19 has VLAN None.
11. The interface 1/0/2 has VLAN None.
12. The interface 1/0/20 has VLAN None.
13. The interface 1/0/21 has VLAN None.
14. The interface 1/0/22 has VLAN None.
15. The interface 1/0/23 has VLAN None.
16. The interface 1/0/24 has VLAN None.
17. The interface 1/0/25 has VLAN 13.
18. The interface 1/0/26 has VLAN None.
19. The interface 1/0/27 has VLAN None.
20. The interface 1/0/28 has VLAN None.
21. The interface 1/0/29 has VLAN None.
22. The interface 1/0/3 has VLAN None.
23. The interface 1/0/30 has VLAN None.
24. The interface 1/0/31 has VLAN None.

which interface do you want to work with? 5
Got it, configuring interface 1/0/14!
Which VLAN would you like to have? 140
Vlan has been changed!
Do you want to continue changing VLANs? (yes/no)no
Thank you for using the application!
```


### Solution to mission 2/3
[Mission 2/3](./mission2_solution.py)

### Solution to mission 3
TBD
