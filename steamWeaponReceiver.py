import requests
from bs4 import BeautifulSoup
command = input("Enter Link : ")
lamo = requests.get(command).text
soup = BeautifulSoup(lamo,'lxml')

FinalLister = []

def priceGet(linkVar):
	lamodom = requests.get(linkVar).text
	storageUnit = BeautifulSoup(lamodom,'lxml')
	priceStore = storageUnit.find_all('div',class_= "btn-group-sm btn-group-justified")
	for x in priceStore:
		print(x.find_all('span',class_="pull-left"))
		print(x.find_all('span',class_="pull-right"))

		
	print("-----------------------------------------------------------------")


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

		if tempoText[0] != "'NoneType' object has no attribute 'find_all'" or tempoText[0] != None: # Checks for any exception raised by try get 
			FinalLister.append(tempoText) 				# Pusing weapon , skin name into the list
	
	except Exception as exc: #EZPZ
		pass
		# print(exc)

for x in FinalLister:									# Printing the elements/ weapon + skins name
	print(x)
