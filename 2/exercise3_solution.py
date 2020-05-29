# an example solution for exercise 3, session 2

import json
import xmltodict

# Here are two functions for two different syntax in reading a file.
# See the commented out function for the second way.
# When using with-as, you do not need to remember to close the file.
# When you do as on the second option, you need to remember to close
# the file once you have read to content.
# I personally prefer using with-as.
def read_file(filename):
    with open(filename) as file:
        return file.read()

# def read_file(filename):
#     file = open(filename)
#     content = file.read()
#     file.close()
#     return content

def get_xml_data(xml_file):
    xml_text = read_file(xml_file)
    data = json.loads(json.dumps(xmltodict.parse(xml_text)))
    # On next line we already parse the information a little bit, to get the
    # exact section of the dictionary that we need returned.
    # Try also dust printing out data, and see what the structure is there.
    interfaces = data["rpc-reply"]["data"]["native"]["interface"]["GigabitEthernet"]
    return interfaces

xml_file = "mission_response.xml"

# Because we parse the information in the function, the loop is much simpler as we
# do not need to do that parsing here.
for interf in get_xml_data(xml_file):
    print(interf["name"])
