# Hands-on material for session 2
Exercises to be defined after the session 2.

**Reading material:**
- Recap info covered in the session 2:
  - DevNet: [Intro to Python part 2](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/intro-python-part2/step/1)
  
**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)

You can try the excercises with interactice python shell in terminal (python / py -i), but I recommend you to save the final code as a Python file (run with python script.py / py script.py).
Remember to activate the virtual environment, and never work outside of it. You can use the same environment through out the sessions, and activate it by using source together with the part to your environments "activate" functionality. Here is an example of creating a virtual environment and activating it:

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
4. Add the info of the device you want to connect to, check the example in the documentation. For example, if you want to connect to the DevNet always on CSR1000 router, use the following credentials: Device type: cisco_xe, Host: ios-xe-mgmt.cisco.com, SSH Port: 8181, Username: developer, Password and secret: C1sco12345
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

We worked last week to create a simple application to change the status and vlan of an interface (session 1, excercise 4). Lets optimise that code and add functionalities! Check the output to see what kind of things are expected, but also if you come up with some additional features, try them out as well :)

There are quite a lot of things to work on here, so take them one at a time and remember to test a lot before proceeding. The task's order is somewhat from easier to harder.

1. **Create the data structure**: Previously, we had three different variables. Create this time a dictionary instead, in which you define those interface features: name, status and vlan. In addition, add the interface mode: it could be trunk  or access. In case of a trunk, there might be more than one vlan supported. Adjust the data structure of vlan to match this.

2. **Texts**: Adjust what we print on the CLI UI: Now you also need to check from the user if they want to change the mode of the interface, so add this to your menu. Also, when printing the current information, the amount of vlans depend on the mode of the interface, so you can adjust the text you print based on that.

3. **Loop**: Adjust the program so that it doesn't automatically end when the user has done a change. Ask if the user wants to continue using the program, and if yes, give them again option to choose what they can do.

4. **Functionality 1: close the program**: Start with creating a functionality to break the loop when user so asks.

5. **Functionality 2: status**: This is the simplest of the actions to modify the interface. You can use almost exactly the script that you created for this functionality in session 1 exercise.

6. **Functionality 3: change vlans**: Create functionality to either directly just change the vlan (in case of access port) or give option to add multiple vlans or delete vlans from existing list (in case of trunk port).

7. **Functionality 4: change mode**: Similarly as with changing status, you can just simple change it to opposite to what it is right now. However, the rules for how many vlans can be used (one vs. multiple) is different depending on the mode, so utilise what you did in previous step to give the person option to add more vlans in case of changing to trunk, or select what vlan to keep when changing to access.

8. If you have not yet done it, place as many of the functionalities in functions to be called when they are needed. Add modularity by placing those functions in other files and importing to the main code.

Example output:
```
$ python exercise4.py

The interface GigabitEthernet1/0/1 has status up.
The mode is access and VLAN 20.

Menu:
1. Close the program
2. Change status
3. Change vlan(s)
4. Change mode
Your selection: 4
Changing the mode from access to trunk.
Current supported vlan is: 20
Do you want to remove it? yes
Add a vlan (or continue with 0): 46
Add a vlan (or continue with 0): 53
Add a vlan (or continue with 0): 21
Add a vlan (or continue with 0): 0

The interface GigabitEthernet1/0/1 has status up.
The mode is trunk and the supported VLANs:
46
53
21

Menu:
1. Close the program
2. Change status
3. Change vlan(s)
4. Change mode
Your selection: 3
Current VLANs:
1. 46
2. 53
3. 21
1. Add VLANs, 2. Remove VLANs? 2
Select from the index of which VLAN you want to remove! 3

The interface GigabitEthernet1/0/1 has status up.
The mode is trunk and the supported VLANs:
46
53

Menu:
1. Close the program
2. Change status
3. Change vlan(s)
4. Change mode
Your selection: 4
Changing the mode from trunk to access.
Removing the support for current vlans:
1. 46
2. 53
Which VLAN would you like to have? 14

The interface GigabitEthernet1/0/1 has status up.
The mode is access and VLAN 14.

Menu:
1. Close the program
2. Change status
3. Change vlan(s)
4. Change mode
Your selection: 2

The interface GigabitEthernet1/0/1 has status down.
The mode is access and VLAN 14.

Menu:
1. Close the program
2. Change status
3. Change vlan(s)
4. Change mode
Your selection: 1
Thank you for using the program!
```