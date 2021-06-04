import requests
from bs4 import BeautifulSoup
from functools import lru_cache


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
	else:
		return "N/A"


def keyHandler(link = None,fText = None):
	if link != None:
		htmlFile = requests.get(link).text
		ransoup = BeautifulSoup(htmlFile,'lxml')
		scrapper = ransoup.find('div',class_ = "inline-middle collapsed-top-margin")
		text = scrapper.h1.text
		textList = text.split()
	elif fText != None:
		textList = fText.split()
	elif link == None and fText == None:
		raise Exception("Function requires at least a valid argument!")
	for x in range(len(textList)):
		textList[x] = textList[x].lower()
	text = "_".join(textList)
	# print(text)
	return text

@lru_cache(maxsize = None)
def collectionDatabaseCreator(link):
	FinalLister = []
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
			tempoText.append(tierHandler(strippedFinalTier))

			priceLink = grd.find_all('a',href=True)
			priceLink = priceLink[3].get('href')
			priceList = priceGet(priceLink)
			tempoText.append(priceList)

			if tempoText[0] != "'NoneType' object has no attribute 'find_all'" or tempoText[0] != None: # Checks for any exception raised by try get 
				FinalLister.append(tempoText) 			# Pusing weapon , skin name into the list

		
		except Exception as exc: #EZPZ
			pass
			
	return FinalLister
