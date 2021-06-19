import requests
from bs4 import BeautifulSoup
from functools import lru_cache
import time

def priceHandler(ambo):
	if ambo == "No Recent Price" or ambo == "Not Possible":
		return"N/A"
	else:
		return ambo

def priceListMaker(priceList):
	tempList = []
	for x in priceList:
		lmao = x.find_all('span')
		if len(lmao) == 2:
			tempList.append(priceHandler(lmao[1].text))
	return tempList

def tierHandler(tier):
	nlist = tier.split()
	if nlist[0] == "Consumer":
		return "Consumer Grade"
	elif nlist[0] == "Industrial":
		return "Industrial Grade"
	elif nlist[0] == "Mil-Spec":
		return "Mil-Spec"
	elif nlist[0] == "Restricted":
		return "Restricted"
	elif nlist[0] == "Classified":
		return "Classified"
	elif nlist[0] == "Covert":
		return "Covert"
	elif nlist[0] == "Contraband":
		return "Contraband"
	else:
		return "N/A"


def keyHandler(link = None,fText = None):
	if link != None:
		try:
			htmlFile = requests.get(link).text
			ransoup = BeautifulSoup(htmlFile,'lxml')

			scrapper = ransoup.find('div',class_ = "inline-middle collapsed-top-margin")
			text = scrapper.h1.text

			textList = text.split()
		except Exception as e:
			print (e)

	elif fText != None:
		textList = fText.split()
		if textList[0].lower() != "the":
			textList = ["The"] + textList

	elif link == None and fText == None:
		raise Exception("Function requires at least a valid argument!")

	for x in range(len(textList)):
		textList[x] = textList[x].lower()
	text = "_".join(textList)
	# print(text)
	return text

def Collection_weapon_link_scrapper(urls):  #Passed a weapon skin link, Returns a list with its detail i.e name price rarity

	#Creating List to store weapon details and html scrapper
	weapon_skin_data = []
	# print(f"Requesting : {urls}") #Debugger
	htmlFile = requests.get(urls).text
	soup = BeautifulSoup(htmlFile,'lxml')
	# print(f"Got HTML : {urls}") #Debugger

	#Append Weapon Name and Skin Name of the given weapon URL
	weapon_name = soup.find('div',class_="well result-box nomargin")
	weapon_name = weapon_name.h2.find_all('a',href=True)
	for x in weapon_name:
		weapon_skin_data.append(x.text)

	#Appends skin rarity to weapon list
	weapon_rarity = soup.find('p',class_="nomargin").text
	weapon_skin_data.append(tierHandler(weapon_rarity.strip()))

	#Appends pricelist of the skin to weapon list
	priceStore = soup.find('div',id="prices")
	priceStore = priceStore.find_all('div',class_= "btn-group-sm btn-group-justified")
	weapon_skin_data.append(priceListMaker(priceStore))

	parent_collection = soup.find("p",class_="collection-text-label").text
	weapon_skin_data.append(parent_collection)

	return weapon_skin_data


@lru_cache(maxsize = 15)
def collectionDatabaseCreator(link): # Passed a Collection link, returns a list with its weapons' data
	local_collection_weapon_links = [] #Lists of weapon skin link in the given collection
	returning_collection_data_list = [] #Returns the list with data in the collection
	lamo = requests.get(link).text
	soup = BeautifulSoup(lamo,'lxml')

	# print(soup.find_all('div',class_="well result-box nomargin"))

	for grd in soup.find_all('div',class_ ="well result-box nomargin"): ## Gets every division having class well result-box....			
		try:						
			priceLink = grd.find_all('a',href=True)
			priceLink = priceLink[3].get('href')
			local_collection_weapon_links.append(priceLink)
		except Exception as e:
			pass

	# Concurrently appends data to local_ smth 
	import concurrent.futures
	with concurrent.futures.ThreadPoolExecutor() as executor:
		var_of_concurrents = executor.map(Collection_weapon_link_scrapper,local_collection_weapon_links)
	for x in var_of_concurrents:
		returning_collection_data_list.append(x)

	return returning_collection_data_list


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
			csgostash_link_database.update({f"{keyHandler(None,z.text)}" : z.get('href')})

	#Scrapping Cases link! (below)

	# for x in linkForCases:
	# 	if x.get('href') != "#":
	# 		# print(f"{x.text} - {x.get('href')}")
	# 		csgostash_link_database.update({f"{keyHandler(None,x.text)}" : x.get('href')})



@lru_cache(maxsize=None)
def Search_for_key(link): #Gets a collection's link and search for key in csgostash_link_database
	for key in csgostash_link_database:
		if csgostash_link_database[key] == link:
			return key


collection_database = {}


def Collection_Database_Feeder(link):  ## Updates / Pushes collection_cases_collection_database with collection and cases with collection link.
	# t1 = time.time() # Time Debugger
	if len(link)== 0:
		print("No Link Passed!")
		return None
	for eachLink in link:
		if Search_for_key(eachLink) not in collection_database:
			collection_database.update({f"{keyHandler(eachLink)}":collectionDatabaseCreator(eachLink)})
		else:
			pass
	# t2 = time.time()
	# print(f"Feeding the collection/cases database : {int(t2-t1)} sec(s)") # Time Debugger




