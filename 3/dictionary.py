# This example shows you how you can play around with OrderedDict and "normal"
# dictionary. You can use JSON module: use "dumps" to make the OrderedDict into
# json string, and then "loads" to change it into "normal" dictionary. This
# way when you print the dictionary out, it will look "cleaner."

import xmltodict, json, pprint

def get_xml(filename):
    '''
    Reading xml file and returning its contents.
    Argument: filename (String)
    Return: xml contents (String)
    '''
    try:
        with open(filename) as file:
            contents = file.read()
        return contents
    except:
        return 0 #return 0 if there was an error


contents = get_xml("xml_example2.xml")

if contents == 0: #Error handling
    print("File reading did not succeed")
else:
    my_ordered_dict = xmltodict.parse(contents)
    #Print out the OrderedDict:
    pprint.pprint(my_ordered_dict)

    #Use JSON to change into dictionary:
    my_dict = json.loads(json.dumps(my_ordered_dict))
    #Print out the "normal" dictionary:
    pprint.pprint(my_dict)
