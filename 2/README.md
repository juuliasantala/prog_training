# Hands-on material for session 2
Smaller exercises with examples and the mission.

**Reading material:**
- [Optional] Recap info covered in the session 2:
  - DevNet: [Intro to Python part 2](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/intro-python-part2/step/1)
  - DevNet: [Parsing JSON with Python](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/parsing-json-python/step/1)

- Prepare for session 3:
  - DevNet: [What is REST? What are REST APIs?](https://developer.cisco.com/learning/devnet-express/dnav4-track/rest-api-fundamentals/what-are-rest-apis/step/1)
  - DevNet: [Getting started with REST APIs](https://developer.cisco.com/learning/devnet-express/dnav4-track/rest-api-fundamentals/getting-started-rest-apis/step/1)
  - Install Postman: https://www.postman.com/downloads/
  - Play with REST APIs ([Exercise 4](#exercise-4))
  
**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)
- [Exercise 4](#exercise-4)
- [Mission 2/3](#mission-23)

## Small exercises
You can work on the small exercises on either interactive python shell in terminal (python / py -i), or save them as python files and run them with python script.py / py script.py.
Remember to activate the virtual environment, and never work outside of it. To create a virtual environment for session 2 exercises, you can do for example:

Mac:
```
$ python3 -m venv session2_exercises 
$ source session2_exercises/bin/activate

```
Windows:
```
$ py -3 -m venv session2_exercises 
$ source session2_exercises/Scripts/activate

```

You need to create the virtual environment only once, after that you just use source to activate it.

### Exercise 1

Try loops and conditionals! Create a list with different numbers. Print the list, and then loop through the list:
- if number is over than 10, print something like "The number is over 10!"
- if number is exactly 10, print something like "The number is 10!"
- if number is less than 10, print something like "Small number!"

Example output:
```
$ python numbers.py
My list is [1, 5, 3, 7, 10, 11, 45, 2, 14]
Small number!
Small number!
Small number!
Small number!
The number is 10!
The number is over 10!
The number is over 10!
Small number!
The number is over 10!
```

### Exercise 2

Check how to research, install and import a module with the module Netmiko.
1. Check the documentation: https://github.com/ktbyers/netmiko
2. Install Netmiko in your virtual environment
3. Import Netmiko connect handler in a python script as shown in the documentation
4. Add the info of the device you want to connect to, check the example in the documentation. For example, if you want to connect to the DevNet always on CSR1000 router, use the following credentials: Device type: cisco_xe, Host: ios-xe-mgmt-latest.cisco.com, SSH Port: 8181, Username: developer, Password and secret: C1sco12345
5. Create the connection with ConnectHandler (see the documentation)
6. Run some show commands with send_command method, such as "show ip int brief"
7. Print the response on CLI
8. Make file safer by taking the credentials to another python file, and importing that file to your script. Instead of host, username and password text, you can now use variables that point to your credentials file.

Example output:
```
$ python netmiko_test.py
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       10.10.20.48     YES NVRAM  up                    up
GigabitEthernet2       20.20.20.254    YES manual up                    up
GigabitEthernet3       30.30.30.254    YES manual up                    up
Loopback21             10.0.0.21       YES manual up                    up
Loopback22             1.1.1.22        YES manual up                    up
Loopback23             19.19.19.19     YES manual up                    up
Loopback24             unassigned      YES unset  up                    up
Loopback25             unassigned      YES unset  up                    up
Loopback26             unassigned      YES unset  up                    up
Loopback27             unassigned      YES unset  up                    up
Loopback28             unassigned      YES unset  up                    up
Loopback29             unassigned      YES unset  up                    up
Loopback30             unassigned      YES unset  up                    up
Loopback31             unassigned      YES unset  up                    up
Loopback32             unassigned      YES unset  up                    up
Loopback33             unassigned      YES unset  up                    up
Loopback34             unassigned      YES unset  up                    up
Loopback35             unassigned      YES unset  up                    up
Loopback37             unassigned      YES unset  up                    up
Loopback38             unassigned      YES unset  up                    up
Loopback39             unassigned      YES unset  up                    up
Loopback40             unassigned      YES unset  up                    up
Loopback41             unassigned      YES unset  up                    up
Loopback42             unassigned      YES unset  up                    up
Loopback108            unassigned      YES unset  up                    up
```

### Exercise 3
See the mission_response.xml file? Write a script where you first open this file, create a dictionary out of the information, and print out the different interfaces.

**Example output:**
```
$ python xml_information.py
1/0/1
1/0/2
1/0/3
1/0/4
1/0/5
1/0/6
1/0/7
1/0/8
```

**Tip:** You can use the following to change the XML to easier readable dictionary:
```Python
data = json.loads(json.dumps(xmltodict.parse(string)))
```

Remember to import both json and xmltodict
```Python
import json, xmltodict
```

### Exercise 4
Try out REST APIs. This is important, as we will go directly to the use of the REST APIs in the lesson 3, and not cover the basics. After studying the DevNet material for REST APIs defined in the beginning of this document, download Postman to try out APIs. You can also use cURL, but we will be using Postman during the Session 3. Both are important tools to understand, but for now we focus on Postman.

Check the documentation and try out in Postman based on what you learned from the DevNet Learning Labs. No authentication needed.
- Countries: http://restcountries.eu/
- NumbersAPI: http://numbersapi.com/
- Chuck Norris API: https://api.chucknorris.io/

You can also check the DevNet Sandboxes and try out APIs, these require authentication. Always-on labs have authentication information ready, reservable labs’ are available through VPN once reserved.


## Mission 2/3

In the mission 1/3 we started creating a simple app which changes a single interface status and VLAN. This week, lets use a JSON file with interface information, and let the user choose which interface they want to work with. We only work with access links, in this case those are the Gigabit links. You can continue with the file you created last time, or use the solution file provided on this page (mission1_solution.py).

Remember: Don't try to create the whole application on one go, rather create some of the parts, test it by running the it, and then add more.

1. First, create a function that reads the information from mission_response.json file (you can find this file from this github page) and returns the JSON text. Check that the function works for example by printing the outcome.
2. Create a function for parsing the JSON (remember to import the module). Use the JSON text gotten from the function created in the previous step. From each  interface, save name, vlan, and port status into a list. You can for example create a list, and add dictionaries for each interface (see example below) in a loop. Try first just looping through the interfaces to see that the loop works. Return the final list, so it can be used outside of the function.
3. [OPTIONAL] I mentioned that we would want to focus only on the access ports (Gigabit). How would you create a conditional that would take only Gigabit ports into account and skip others? What about the VLAN interface, how would you leave that out?
4. Last time, we created a string to print out the status and VLAN of the interface. Print out to the user the information of the interfaces. Add a running number in front, so we can refer to that number when user chooses which interface they would like to configure.
5. Ask from the user, which interface they would like to work with, and print the response. Remember! Index counting starts from 0, so if the user asks for first item in the list, the index is 0, not 1.
6. Now, utilise what we created las time: Ask them if they would want to change the status of the interface (user needs to type 1) or VLAN of the interface (user needs to type 2)
7. If the user types 1, change the value of the status to opposite what it is currently. Check first the status with conditionals, and act accordingly.
8. If the user types 2, ask them what value they would like to have for the VLAN. Save this input to the right dictionary in the interface_list.
9. If the user types anything else than 1 or 2, let them know that this is an invalid selection.
10. In the end, tell the user what the status and the VLAN of the interface are after the changes.
11. [OPTIONAL] Lets move the file and JSON handling to a separate module! Create the module, import it and make necessary changes so that the app still continues to work.

**Example for list creation:**
What should you save into the interface_list?
```python
interface_list.append({"name":name, "vlan":vlan, "status":status})
```

Final list after looping through the interfaces could look for example like:
```python
[{'name': 'GigabitEthernet0/0', 'vlan': '0', 'status': 'down'}, {'name': 'GigabitEthernet1/0/1', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/2', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/3', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/4', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/5', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/6', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/7', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/8', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/9', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/10', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/11', 'vlan': '1', 'status': 'down'}, {'name': 'GigabitEthernet1/0/12', 'vlan': '1', 'status': 'down'}]
```

### Example output:
```
$ python mission.py
1. The interface GigabitEthernet0/0 has status down and VLAN 0.
2. The interface GigabitEthernet1/0/1 has status down and VLAN 1.
3. The interface GigabitEthernet1/0/2 has status down and VLAN 1.
4. The interface GigabitEthernet1/0/3 has status down and VLAN 1.
5. The interface GigabitEthernet1/0/4 has status down and VLAN 1.
6. The interface GigabitEthernet1/0/5 has status down and VLAN 1.
7. The interface GigabitEthernet1/0/6 has status down and VLAN 1.
8. The interface GigabitEthernet1/0/7 has status down and VLAN 1.
9. The interface GigabitEthernet1/0/8 has status down and VLAN 1.
10. The interface GigabitEthernet1/0/9 has status down and VLAN 1.
11. The interface GigabitEthernet1/0/10 has status down and VLAN 1.
12. The interface GigabitEthernet1/0/11 has status down and VLAN 1.
13. The interface GigabitEthernet1/0/12 has status down and VLAN 1.
which interface do you want to work with? 3
Got it, configuring interface GigabitEthernet1/0/2!
Select 1 to change status and 2 to change VLAN: 2
Which VLAN would you like to have? 30
The interface GigabitEthernet1/0/2 has status down and VLAN 30.
Thank you for using the application!
```

### Solution to mission 1/3
[Mission 1/3](./mission1_solution.py)
