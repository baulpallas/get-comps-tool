import requests
import sys
from pprint import pprint
import xlsxwriter
from decouple import config


ZWSID = config('ZWSID')

# Format the arguments
address = sys.argv[1]
cityStateArray = sys.argv[2].split()
cityStateString = f"{cityStateArray[0][:-1]}+{cityStateArray[1]}"
print(cityStateString)


def getSearchResults(address=None, cityState=None):

    url = "http://www.zillow.com/webservice/GetSearchResults.htm"

    querystring = {"address2": "4330 Lake Forest Ct, Finksburg, MD, 21048"}

    headers = {
        'accept': "application/json",
        'x-rapidapi-key': "6e67d3dce0msh3ba8e8e0a96998fp1e6905jsnb8731a1369a4",
        'x-rapidapi-host': "attomdatasolutions-attom-property-v1.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.json())


# def getPropertyId(address=None, cityState=None):

#     url = "https://realtor.p.rapidapi.com/locations/auto-complete"

#     querystring = {"input": "4330 Lake Forest Ct, Finksburg, MD, 21048"}

#     headers = {
#         'x-rapidapi-key': "95ceb00e07msh97ffc2966d50762p1de79ajsne7f972cd2d9a",
#         'x-rapidapi-host': "realtor.p.rapidapi.com"
#     }

#     response = requests.request(
#         "GET", url, headers=headers, params=querystring)
#     pprint(response.json())
#     return response.json()["autocomplete"][0]['mpr_id']


def getMLSData(mlsId=None):
    url = "https://realtor.p.rapidapi.com/properties/list-by-mls"

    querystring = {"mls_id": "<REQUIRED>", "offset": "0", "limit": "10"}

    headers = {
        'x-rapidapi-key': "95ceb00e07msh97ffc2966d50762p1de79ajsne7f972cd2d9a",
        'x-rapidapi-host': "realtor.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    print(response.json())


getPropertyId()

# mpr_Id = getPropertyId()
# getMLSData(mpr_Id)
