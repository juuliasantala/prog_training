# Hands-on material for session 2
Exercises to be defined after the session 2.

**Reading material:**
- Recap info covered in the session 2:
  - DevNet: [Intro to Python part 2](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/intro-python-part2/step/1)
  
**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)
- [Exercise 4](#exercise-4)
- [Exercise 5](#exercise-5)

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

TBD

### Exercise 3

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


### Exercise 4

TBD

## Exercise 5

TBD
