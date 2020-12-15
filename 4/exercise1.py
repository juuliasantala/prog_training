import requests

def select_country():
    '''
    Ask for the user which country they would like information of.
    Returns the name of the country as the user has written it.
    If user wants to stop using the program, they can also write 'end'.
    '''
    print("Please select country or write 'end'")
    country = input("What country would you like to know more about? ")
    return country

def get_country_info(country_name):
    '''
    Make an API call to get information about a country.
    Country provided as an argument for the function.
    Response returned together with status code.
    If there is an error, return 0.
    '''
    url = "https://restcountries.eu/rest/v2/name/{}".format(country_name)
    try:
        response = requests.request("GET", url)
        return {
            "response": response.json(),
            "status_code": response.status_code
            }
    except:
        print("API call was not successful.")
        return 0

def print_country_info(country_info):
    '''
    Print the information of the country in the CLI.
    Country info provided as argument, this is a list of 1 or more countries.
    '''
    print("Found {} countries:\n".format(len(country_info)))
    for item in country_info:
        print("{} ({})".format( item["name"],
                                item["nativeName"]))
        print("Capital: {}".format(item["capital"]))
        print("Population: {}".format(item["population"]))
        print("Languages:", end=" ")
        for index, language in enumerate(item["languages"]):
            print("{}. {}".format(index+1,
                            language["name"]), end=" ")
        print("\n")

def main():
    while True:
        country = select_country()
        if country == "end":
            break

        response = get_country_info(country)
        if response == 0:
            continue
        elif response["status_code"] == 404:
            print("404 not a valid country code.")
            continue
        else:
            print_country_info(response["response"])


if __name__ == "__main__":
    main()
