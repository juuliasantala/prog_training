import xmltodict, pprint

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

def print_interface_names(data):
    '''
    Get interface names and print them out on CLI.
    Argument: interfaces (OrderedDictionary or Dictionary)
    '''
    interfaces = data["rpc-reply"]["data"]["native"]["interface"]["GigabitEthernet"]
    for interface in interfaces:
        print(interface["name"])


def main():
    '''
    Main function, executed when the code is run.
    '''
    contents = get_xml("xml_example2.xml")

    if contents == 0: #Error handling
        print("File reading did not succeed")
    else:
        print_interface_names(xmltodict.parse(contents))

#Check if this is the file that is being executed, vs. this being
#imported to some other code. If we are executing this specific
#file, the __name__ will automatically get value "__main__".
if __name__ == "__main__":
    main()

##
