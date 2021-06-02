import requests
from bs4 import BeautifulSoup
from functools import lru_cache

print("Please Ignore all the ('NoneType' object has no attribute 'find_all') error! Dev dont want to touch the working code!")
FinalLister = []
def Handler(ambo):
	if ambo == "No Recent Price" or ambo == "Not Possible":
		return"N/A"
	else:
		return ambo

def priceGet(linkVar):
	tempList = []
	lamodom = requests.get(linkVar).text
	storageUnit = BeautifulSoup(lamodom,'lxml')
	priceStore = storageUnit.find('div',id="prices")
	priceStore = priceStore.find_all('div',class_= "btn-group-sm btn-group-justified")

	# print(priceStore)
	for x in priceStore:
		lmao = x.find_all('span')
		if len(lmao) == 2:
			tempList.append(Handler(lmao[1].text))
	return tempList


@lru_cache(maxsize = None)
def collectionDatabaseCreator(link):
	lamo = requests.get(link).text
	soup = BeautifulSoup(lamo,'lxml')
	for grd in soup.find_all('div',class_ ="well result-box nomargin"): ## Gets every division having class well result-box....

		tempoText = [] 										# For the concatination of weapon and skin name
		try: 												# to prevent error caused by souvenier packages on the front page of collection
			name = grd.h3 									# gets h3 tag of grd (grd = each single division with class well result-box.... )
			fina = name.find_all('a') 						# Gets the name of weapon and skins
			for lol in fina: 								# gets weapon and skin name and append it to tempoText
				tempoText.append(lol.text)

			tier = grd.find('a',class_= "nounderline")		# getting tier class and stuff
			finalTier = tier.div.p.text 
			strippedFinalTier = finalTier.strip()			# Stripped \n from those tiers
			tempoText.append(strippedFinalTier)

			priceLink = grd.find_all('a',href=True)
			priceLink = priceLink[3].get('href')
			priceList = priceGet(priceLink)
			tempoText.append(priceList)

			if tempoText[0] != "'NoneType' object has no attribute 'find_all'" or tempoText[0] != None: # Checks for any exception raised by try get 
				FinalLister.append(tempoText) 			# Pusing weapon , skin name into the list

		
		except Exception as exc: #EZPZ
			pass
			print(exc)
	return FinalLister
command = input("Enter Link : ")
for x in collectionDatabaseCreator(command):
	print(x)
	print()
print(len(collectionDatabaseCreator(command)))