import json

def get_json(filename):
    '''
    Reading json file and returning its contents
    Argument: filename (String)
    Return: json contents (String)
    '''
    try:
        with open(filename) as file:
            contents = file.read()
        return contents
    except:
        return 0

def print_documentation(data):
    '''
    Get neighbour relations and print documentation on CLI.
    Argument: device data (List)
    '''
    neighbors = data[0]["deviceDetails"]["neighborTopology"][0]

    # Initialise the structures to save Node and Link information:
    my_nodes = {}
    my_links = []

    # Scan through all of the nodes that are listed in the json file.
    # For each node, we save the ID and the name of the platform(=platformId).
    # We save info in a dictionary so that ID is the key and platform the value.
    # In the end, the library is something like:
    #     {
    #         "id1": "platform1",
    #         "id2": "platform2",
    #         "id3": "platform3"
    #     }
    # Now, we will be able to access the platform name by using the ID as a key.
    # --> my_nodes["id1"] will give us "platform1".
    for node in neighbors["nodes"]:
        my_nodes[node["id"]] = node["platformId"]


    # Scan through all the links that are listed in the json file.
    # For each link, we save the source and target device ID and interface name.
    # The IDs listed for source and target refer to the nodes that we handled
    # in the previous for-loop.
    # In the end, the link list well look something like:
    #     [
    #         {"source": "source ID",
    #         "source_name": "interface name",
    #         "target": "target ID",
    #         "target_name": "interface name"},
    #
    #         {
    #          ...
    #         },
    #
    #         {
    #          ...
    #         },
    #
    #         {
    #          ...
    #         },
    #     ]
    for link in neighbors["links"]:
        my_link = {
            "source": link["source"],
            "source_name": link["sourceInterfaceName"],
            "target": link["target"],
            "target_name": link["targetInterfaceName"]
        }
        my_links.append(my_link)

    # Take the link list created in previous step.
    # Print out the preferred documentation.
    # You can comnbine this third loop with the previous loop, and skip the
    # creation of my_links -list. However, if and when you want to take this
    # code further in modularity and create separate function for printing the
    # information out, you could just return the my_links -list from this
    # function and utilise in the printing-out function.
    for link in my_links:
        print("{} {} --> {} {}".format(
            my_nodes[link["source"]],
            link["source_name"],
            my_nodes[link["target"]],
            link["target_name"]
        ))

def main():
    '''
    Main function, executed when the code is run.
    '''
    contents = get_json("json_example.json")

    if contents == 0: #Error handling
        print("File reading did not succeed")
    else:
        print_documentation(json.loads(contents))

#Check if this is the file that is being executed, vs. this being
#imported to some other code. If we are executing this specific
#file, the __name__ will automatically get value "__main__".
if __name__ == "__main__":
    main()
