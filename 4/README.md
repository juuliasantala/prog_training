# Hands-on material for session 4

While going through the reading material from DevNet learninglabs marked for this session, try things out in the interactive python shell in terminal! Try out what happens when you change values. Then practice with the following exercises. For the practice exercises, try to solve those by yourself before the Q&A. The solution files will be added here after we have covered them in the Q&A session. Remember, the solutions are just examples on how you could solve the exercises, there are different ways to do things!

**Reading material:**
- DevNet: [Cisco DNA Center API overview](https://developer.cisco.com/learning/devnet-express/dnav4-track/dnav4-intro-dnac/dne-dnac-api-overview/step/1)

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

TBD

## Exercise 4

TBD
