import steamWeaponReceiver as csgostash
from bs4 import BeautifulSoup
import requests
###########################################
collection_cases_database = {}
###########################################

csgostash_link_database = {
	

}


def mainWebLinkScrapper():
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

def databaseFeeder(link):
    collection_cases_database.update({f"{csgostash.keyHandler(link)}":f"{csgostash.collectionDatabaseCreator(link)}"})
    
def main():
	mainWebLinkScrapper() ## Backs csgostash_link_database with collection and cases links. access through key of each
	databaseFeeder(csgostash_link_database['bank_collection'])
	for x in collection_cases_database:
		print(f"{x} : {collection_cases_database[x]}")