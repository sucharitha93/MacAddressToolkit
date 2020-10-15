'''
https://api.macaddress.io/v1?
Validate command line argument input
Send the argument to the requests function
Get the response object
Process the response and return the output
'''
import sys
import requests
import re

def main(mac):
   if re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac.lower()):
      print("Mac address syntax validation SUCCESSFULL.")
      params = {"apiKey": 'at_wznlDXH3lQTDWBcvesbY8dcplfuim', "output": 'json', "search": mac}
      response = requests.get('https://api.macaddress.io/v1', params)
      if response.status_code == 200:
         response = response.json()
         print("\nManufacturer's Details\n")
         print("Name:",response["vendorDetails"]["companyName"])
         print("Address:", response["vendorDetails"]["companyAddress"])
         print("OUI:", response["vendorDetails"]["oui"])
         print("\nMAC Address Details\n")
         print("Is Valid:", response["macAddressDetails"]["isValid"])
         print("Is virtualMachine:", response["macAddressDetails"]["virtualMachine"])
         print("Applications:", response["macAddressDetails"]["applications"])
         print("Creation Date:", response["blockDetails"]["dateCreated"])
         print("Last Updated:", response["blockDetails"]["dateUpdated"])
      elif response.status_code == 401:
         print("Access restricted. Enter the correct API key.")
      elif response.status_code == 402:
         print("Access restricted. Check the credits balance.")
      elif response.status_code == 422:
         print("Invalid MAC or OUI address was received.")
      elif response.status_code == 429:
         print("Too many requests. Try your call again later.")
      elif response.status_code == 500:
         print("Internal server error. Try your call again or contact us.")
      elif response.status_code == 400:
         print("Invalid parameters")
   else:
      print("Invalid Mac Address")

if __name__ == "__main__":
   mac = sys.argv[1]
   main(mac)

