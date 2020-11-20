# Functions to modify the dictionary
def modify_dict(dictionary):
	dictionary["name"] = "Ville"

def modify_dict_with_kwargs(**dictionary):
	dictionary["name"] = "Ronja"

# Main function
def main():
	my_dictionary = {"name":"Juulia", "company":"Cisco"}

	print("sanakirja alussa: {}".format(my_dictionary))

	modify_dict(my_dictionary)
	print("sanakirja muokkauksen jälkeen: {}".format(my_dictionary))

	modify_dict_with_kwargs(**my_dictionary)
	print("Koska sijoitimme vain avain-arvo -parin, muutokset eivät vaikuta sanakirjaan: {}".format(my_dictionary))

# Running the main function
main()