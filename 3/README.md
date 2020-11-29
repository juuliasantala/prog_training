# Hands-on material for session 3

Please note that this time there is also a preparation task for next session! As we will go into REST APIs next time, I would like to skip the basic theory, and go directly to working with real APIs and their documentation.

Additionally, we will not cover Netconf / Restconf in this course. However, after this session is the natural moment to read about them, as they also utilise JSON and XML. Netconf and Restconf might come up with your Blackbelt exam, and are also a part of the DevNet associate certification exam.

**Reading material:**

- DevNet: [Parsing JSON with Python](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/parsing-json-python/step/1)
- Error handling: https://realpython.com/python-exceptions/

- Self-study, recommended to check before doing Blackbelt exam:
  - DevNet: [What and why of Model Driven Programmability](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-why-mdp/step/1)
  - DevNet: [Exploring IOS XE YANG Data Models with NETCONF](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-intro-netconf/step/1)
  - DevNet: [Exploring IOS XE YANG Data Models with RESTCONF](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav3-intro-mdp/dnav3-intro-restconf/step/1)

**Prepare for session 4**
- DevNet: [What is REST? What are REST APIs?](https://developer.cisco.com/learning/devnet-express/dnav4-track/rest-api-fundamentals/what-are-rest-apis/step/1)
- DevNet: [Getting started with REST APIs](https://developer.cisco.com/learning/devnet-express/dnav4-track/rest-api-fundamentals/getting-started-rest-apis/step/1)
- Install Postman: https://www.postman.com/downloads/
- [Postman exercise](#postman-exercise)

**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)

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

## Postman exercise

Try out REST APIs. This is important, as we will go directly to the use of the REST APIs in the lesson 4, and not cover the basics. After studying the DevNet material for REST APIs defined in the beginning of this document, [download Postman](https://www.postman.com/downloads/) to try out APIs. You can also use cURL, but we will be using Postman during the Session 4. Both are important tools to understand, but for now we focus on Postman.

Play with APIs! Check the documentation and try out in Postman based on what you learned from the DevNet Learning Labs. Some examples of APIs that do not require authentication:
- Deck of cards: https://deckofcardsapi.com/
- Countries: http://restcountries.eu/
- NumbersAPI: http://numbersapi.com/
- Chuck Norris API: https://api.chucknorris.io/

## Exercise 1

Read the json_example2.json in your code, transform the content into Python data structure and print out all the interface names!

**Example output:**
```
$ python exercise1.py
FortyGigabitEthernet1/1/1
FortyGigabitEthernet1/1/2
GigabitEthernet0/0
GigabitEthernet1/0/1
GigabitEthernet1/0/10
GigabitEthernet1/0/11
GigabitEthernet1/0/12
GigabitEthernet1/0/13
GigabitEthernet1/0/14
GigabitEthernet1/0/15
GigabitEthernet1/0/16
GigabitEthernet1/0/17
GigabitEthernet1/0/18
GigabitEthernet1/0/19
GigabitEthernet1/0/2
GigabitEthernet1/0/20
GigabitEthernet1/0/21
GigabitEthernet1/0/22
GigabitEthernet1/0/23
GigabitEthernet1/0/24
GigabitEthernet1/0/3
GigabitEthernet1/0/4
GigabitEthernet1/0/5
GigabitEthernet1/0/6
GigabitEthernet1/0/7
GigabitEthernet1/0/8
GigabitEthernet1/0/9
GigabitEthernet1/1/1
GigabitEthernet1/1/2
GigabitEthernet1/1/3
GigabitEthernet1/1/4
LISP0
Loopback0
TenGigabitEthernet1/1/1
TenGigabitEthernet1/1/2
TenGigabitEthernet1/1/3
TenGigabitEthernet1/1/4
TenGigabitEthernet1/1/5
TenGigabitEthernet1/1/6
TenGigabitEthernet1/1/7
TenGigabitEthernet1/1/8
TwentyFiveGigE1/1/1
TwentyFiveGigE1/1/2
Vlan1
Vlan1021
Vlan1023
Vlan1024
Vlan1025
Vlan2045
Vlan2508
```

## Exercise 2

Read the json_example.json in your code. Create a "documentation" of what links the switch has towards the neighbors. Note that you will have to check the id of the source and target and match it with the nodes. Get creative and add more relevant info to your script!

**Example output:**
```
$ python exercise2.py
C9300-24T GigabitEthernet2/0/7 --> WS-C3850-48P-E GigabitEthernet1/0/7
C9300-24T TenGigabitEthernet2/1/2 --> C9500-40X TenGigabitEthernet1/0/40
C9300-24T GigabitEthernet2/0/3 --> WS-C3850-48P-E GigabitEthernet1/0/3
C9300-24T GigabitEthernet2/0/5 --> WS-C3850-48P-E GigabitEthernet1/0/5
```

## Exercise 3

Read the xml_example2.xml in your code. Print all the names of the interfaces!
Note, when taking the xml-format into Python data structure with xmltodict, we got Ordered Dictionary instead of the normal dictionary. This data structure behaves like normal dictionary, the main difference is that it keeps the order in which the keys have been inserted.

**Example output:**
```
$ python exercise3.py
1/0/1
1/0/2
1/0/3
1/0/4
1/0/5
1/0/6
1/0/7
1/0/8
```
