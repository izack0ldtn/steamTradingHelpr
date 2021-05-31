import requests
from bs4 import BeautifulSoup
command = input("Enter Link : ")
lamo = requests.get(command).text
soup = BeautifulSoup(lamo,'lxml')
# print(soup.prettify())
collection_dustII = []
for grd in soup.find_all('div',class_ ="well result-box nomargin"): ## Gets every division having class well result-box....

	tempoText = "" # For the concatination of weapon and skin name
	try: # to prevent error caused by souvenier packages on the front page of collection
		name = grd.h3 # gets h3 tag of grd (grd = each single division with class well result-box.... )
		fina = name.find_all('a') # Gets the name of weapon and skins
		for lol in range(len(fina)): # gets weapon and skin name and Kinda concatinates weapon and skin name
			# print(lol.text, end= " ")
			if lol == 0: # checking for text formatting IF ELSE
				tempoText += fina[lol].text
			else:
				tempoText = tempoText + " "+fina[lol].text

		# print(tempoText)
		if tempoText != "'NoneType' object has no attribute 'find_all'" or tempoText != None: # Checks for any exception raised by try get 
			collection_dustII.append(tempoText) # Pusing weapon + skin name into the list
	except Exception as exc: #EZPZ
		pass
		# print(exc)
for x in collection_dustII: # Printing the elements/ weapon + skins name
	print(x)
