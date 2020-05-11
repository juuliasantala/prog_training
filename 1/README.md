# Hands-on material for session 1
While going through the reading material from DevNet learninglabs marked for this session, try things out in the interactive python shell in terminal! Try out what happens when you change values. Then practice with the following exercises. For the practice exercises, try first to solve by yourself. If you get stuck or want to compare your code to an example solution code, check the solution files. Remember, these are just examples on how you could solve the exercises, there are different ways to do things!

Finally, last part is the start of the mission, that we will continue working on after the two next sessions, building on what we start today.

**Reading material:**
- Self-study, will not be covered in the lesson
  - DevNet: [Brief intro to GIT](https://developer.cisco.com/learning/modules/programming-fundamentals/git-basic-workflows/step/1)
  - DevNet: [Intro to coding and APIs](https://developer.cisco.com/learning/devnet-express/dnav4-track/intro-python/intro-coding-and-apis/step/1)

- Main reading material to study
  - DevNet: [Intro to Python part 1](https://developer.cisco.com/learning/modules/programming-fundamentals/intro-python-part1/step/1)

**Exercises**
- [Exercise 1](#exercise-1)
- [Exercise 2](#exercise-2)
- [Exercise 3](#exercise-3)
- [Mission 1/3](#mission-13)

---

## Small exercises

You can work on the small exercises on either interactive python shell in terminal (python / py -i), or save them as python files and run them with python script.py / py script.py.
It is recommended to start already now using the virtual environments, and never work outside of it. To create a virtual environment for session 1 exercises, you can do for example:

Mac:
```
$ python3 -m venv session1_exercises 
$ source session1_exercises/bin/activate

```
Windows:
```
$ py -3 -m venv session1_exercises 
$ source session1_exercises/Scripts/activate

```


### Exercise 1

Save some values to three variables. Print out the variables together with their type.
Example output:
```
$ python exercise1.py
The first variable is 9000 and the type is <class 'int'>
The second variable is Catalyst and the type is <class 'str'>
The third variable is 3.5 and the type is <class 'float'>
```


### Exercise 2

Try out the conditionals. We will cover them in the session 2, but it is good to try out them already now!
Create a script where you first ask user for a number, and provided is 10, the script prints out a congratulation message for the user. If the number is not 10, the script tells the user that they guessed the wrong number.

Example output:
```
$ python exercise2.py
Play a game!
Choose a number: 2
Bad luck, that was not the correct number!
```

```
$ python exercise2.py
Play a game!
Choose a number: 10
Congratulations, you chose the correct number!
```

**Hints:**
Using input returns a string. To be able to compare with the numbers, you need to change the datatype to int with int(). For example:
```python
number_as_a_string = input("What is your favourite number?")
number_as_a_number = int(number_as_a_string)
```

Note that when you assing a variable, you use "=", for example:
```python
number = 20
```
But when you compare if something is equal, you use "==", for example:
```python
if number == 20:
    print("number is 20!")
```


### Exercise 3
Create a simple calculator that takes two numbers as user input and returns a sum of these two numbers. The idea is that when the script is run in the terminal, the script will ask the user to provide first one number and then a second number, and use those two numbers for the calculation.

Example output:
```
$ python exercise3.py
Welcome! This application lets you calculate the sum of two numbers.
Enter the first number: 24
Enter the second number: 13
The sum of numbers 24 and 13 is 37
```

**Hint:**
Using input returns a string. To be able to calculate with the numbers, you need to change the datatype to int with int(). For example:
```python
number_as_a_string = input("What is your favourite number?")
number_as_a_number = int(number_as_a_string)
```

---

## Mission 1/3

The idea of the mission is to build a simple, working application during the training. We will start with some simple features, and continue working on the code in the next session. An example solution for the Mission 1 will be provided later.

Lets start by creating a simple application to change either the status or the VLAN of one interface. Don't try to create the whole application on one go, rather create some of the parts, test it by running the it, and then add more.

1. First, define three variables: one for the name of the interface (for example: "GigabitEthernet1/0/1"), one for the status (for example: "up"), and one for the VLAN (for example: "30").
2. Print this information out to user, and ask them if they would want to change the status of the interface (user needs to type 1) or VLAN of the interface (user needs to type 2).
3. If the user types 1, change the value of the status to opposite.
4. If the user types 2, ask them what value they would like to have for the VLAN. Save this input to the VLAN variable.
5. If the user types anything else than 1 or 2, let them know that this is an invalid selection.
6. In the end, tell the user what the status and the VLAN of the interface are after the changes.

Example output:
```
$ python mission.py
The interface GigabitEthernet1/0/1 has status up and VLAN 20.
Select 1 to change status and 2 to change VLAN: 2
Which VLAN would you like to have? 30
Now the interface GigabitEthernet1/0/1 has status up and VLAN 30.
Thank you for using the application!
```
