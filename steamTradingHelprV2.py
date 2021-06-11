import steamWeaponReceiver as csgostash
from bs4 import BeautifulSoup
import requests
import os
from functools import lru_cache
import json
import time
###########################################
collection_cases_database = {}
###########################################

csgostash_link_database = {} #CSGOSTASH collection and cases link eg - https://www.csgostash.com/The+Control+Collection

@lru_cache(maxsize=10)
def MainWebLinkScrapper():  ## Updates database with link 
	htmlFile = requests.get("https://csgostash.com/").text
	soup = BeautifulSoup(htmlFile,'lxml')

	dropdownList = soup.find_all('li',class_= "dropdown") # 5th index dropdown of cases and 6th index dropdown of collection
	# linkForCases = dropdownList[5].find_all('a',href= True) # Cases scrapping
	linkForCollection = dropdownList[6].find_all('a',href= True) 

	for z in linkForCollection:
		if z.get('href') != "#":
			# print(f"{z.text} - {z.get('href')}")
			csgostash_link_database.update({f"{csgostash.keyHandler(None,z.text)}" : z.get('href')})

	#Scrapping Cases link! (below)

	# for x in linkForCases:
	# 	if x.get('href') != "#":
	# 		# print(f"{x.text} - {x.get('href')}")
	# 		csgostash_link_database.update({f"{csgostash.keyHandler(None,x.text)}" : x.get('href')})

@lru_cache(maxsize=None)
def Search_for_key(link): #Gets a collection's link and search for key in csgostash_link_database
	for key in csgostash_link_database:
		if csgostash_link_database[key] == link:
			return key
		else:
			return "No Key"


def Collection_Cases_Database_Feeder(*link):  ## Updates / Pushes collection_cases_collection_database with collection and cases with collection link.
	t1 = time.time() # Time Debugger
	if len(link)== 0:
		print("No Link Passed!")
		return None
	for eachLink in link:
		if Search_for_key(eachLink) not in collection_cases_database:
			collection_cases_database.update({f"{csgostash.keyHandler(eachLink)}":csgostash.collectionDatabaseCreator(eachLink)})
		else:
			pass
	t2 = time.time()
	print(f"Feeding the collection/cases database : {int(t2-t1)} sec(s)") # Time Debugger

# def details(key):
# 	for data in collection_cases_database[key]:
# 		print(data)
