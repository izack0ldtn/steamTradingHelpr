import steamWeaponReceiver as csgostash
from bs4 import BeautifulSoup
import requests
import os
from functools import lru_cache
import json
###########################################
collection_cases_database = {}
###########################################

csgostash_link_database = {} #CSGOSTASH collection and cases link eg - https://www.csgostash.com/The+Control+Collection

@lru_cache(maxsize=10)
def mainWebLinkScrapper():  ## Updates database with link 
	htmlFile = requests.get("https://csgostash.com/").text
	soup = BeautifulSoup(htmlFile,'lxml')
	dropdownList = soup.find_all('li',class_= "dropdown") # 5th index dropdown of cases and 6th index dropdown of collection
	linkForCases = dropdownList[5].find_all('a',href= True)
	linkForCollection = dropdownList[6].find_all('a',href= True)
	for z in linkForCollection:
		if z.get('href') != "#":
			# print(f"{z.text} - {z.get('href')}")
			csgostash_link_database.update({f"{csgostash.keyHandler(None,z.text)}" : f"{z.get('href')}"})
	for x in linkForCases:
		if x.get('href') != "#":
			# print(f"{x.text} - {x.get('href')}")
			csgostash_link_database.update({f"{csgostash.keyHandler(None,x.text)}" : f"{x.get('href')}"})

def databaseFeeder(*link):  ## Updates / Pushes collection_cases_collection_database with collection and cases with collection link.
	if len(link)== 0:
		print("No Link Passed!")
		return None
	for eachLink in link:
		if csgostash.keyHandler(eachLink) not in collection_cases_database:
			collection_cases_database.update({f"{csgostash.keyHandler(eachLink)}":f"{csgostash.collectionDatabaseCreator(eachLink)}"})
		else:
			pass
def jsonStorer():
	mainWebLinkScrapper()
	with open('links.json','w') as linkfile:
		linkfile.write(json.dumps(csgostash_link_database))


def linkStorageHandler():
	if os.path.isfile('links.json'):
		with open('links.json','r') as linkFile:
			try:
				tempMainLinkDict = json.loads(linkFile.read())
			except Exception as e:
				print(e)
				print ("No Proper JSON file")
				jsonStorer()
				tempMainLinkDict = json.loads(linkFile.read())
			if len(tempMainLinkDict) != 70:
				print("JSON file has been modified. Rewriting links.json")
				jsonStorer()
			else:
				csgostash_link_database = tempMainLinkDict
	else:
		mainWebLinkScrapper()
		jsonStorer()


