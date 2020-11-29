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

### Postman exercise

Try out REST APIs. This is important, as we will go directly to the use of the REST APIs in the lesson 3, and not cover the basics. After studying the DevNet material for REST APIs defined in the beginning of this document, [download Postman](https://www.postman.com/downloads/) to try out APIs. You can also use cURL, but we will be using Postman during the Session 4. Both are important tools to understand, but for now we focus on Postman.

Play with APIs! Check the documentation and try out in Postman based on what you learned from the DevNet Learning Labs. Some examples of APIs that do not require authentication:
- Deck of cards: https://deckofcardsapi.com/
- Countries: http://restcountries.eu/
- NumbersAPI: http://numbersapi.com/
- Chuck Norris API: https://api.chucknorris.io/

### Exercise 1

TBD

### Exercise 2

TBD

### Exercise 3

TBD

## Exercise 4

TBD
