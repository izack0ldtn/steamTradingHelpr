import steamWeaponReceiver as csgostash
from steamWeaponReceiver import collection_database,csgostash_link_database
import os
from functools import lru_cache
import time
from rich.console import Console
from rich.table import Table 
from consoleMenu import Menu_CheckBox, Menu_RadioButton
import pyfiglet
from sys import exit
from msvcrt import getch
console = Console()

temporal_dataset_collection = {} #stores the data that collection_database data and can be cleared by user


def Key_Decrypter(text): #Decryptes the csgostash_link_database's dictionary's key into normal looking text. For displaying in console.
	textList = text.split("_")
	textList.pop(0)
	for x in range(len(textList)): textList[x] = textList[x].capitalize() 
	return " ".join(textList)

def Usercall_Passed_Link(link):
	os.system("cls")
	with console.status("Downloading Contents from CS:GO Stash ....",spinner="point"):
		csgostash.Collection_Database_Feeder(link)
	for eachKey in collection_database:
		if eachKey not in temporal_dataset_collection:
			temporal_dataset_collection[eachKey] = collection_database[eachKey]

def Usercall_Clear_Tempdb():
	global temporal_dataset_collection
	temporal_dataset_collection.clear()


###########################
# Console Interface Below #
###########################
print(pyfiglet.figlet_format("+[--| s t m v2 |--]+",justify="center",width = 160))
console.rule()
console.print("steamTradingHelprV2",style = "black on white",justify = 'center')
console.print("Powered By CSGOSTASH®",justify ="center")
console.rule()
time.sleep(2)

def MainMenu():

	header = ("[bold green]Welcome to steamTradingHelprV2 ![/bold green]"
	  "If you already know to use this program, please feel free to continue using this program."
	  "For Begineer, It's real easy, Just select the [black on white][X] Help[/black on white] menu!"
	  "Good Luck and Have Fun! ~ izack0ldtn"
	 )

	menu_list = ["Continue","Help","Exit"]
	statement = "Use Arrow keys (up and down) to move. Hit enter to select!"
	mainmenuobj = Menu_RadioButton(menu_list,statement,header)
	returnValue = mainmenuobj.main()
	if returnValue == menu_list[0]:
		continueMenu()
	elif returnValue == menu_list[1]:
		helper()
	elif returnValue == menu_list[2]:
		exit()

def continueMenu():
	statement = "Select to continue: "
	continue_menu_list = ["All Collection","Specified Collection","Drop Pool Collection","Go Back"]
	continueMenuobj = Menu_RadioButton(continue_menu_list,statement)
	returnValue = continueMenuobj.main()
	if returnValue == continue_menu_list[1]:
		specifiedCollectionMenu()
	elif returnValue == continue_menu_list[0]:
		allCollectionMenu()
	elif returnValue == continue_menu_list[2]:
		specifiedDropCollection()
	elif returnValue == continue_menu_list[3]:
		MainMenu()

def specifiedDropCollection():

	list_of_active_drop_collection = [
	"The 2018 Inferno Collection",
	"The 2018 Nuke Collection",
	"The Bank Collection",
	"The Dust 2 Collection",
	"The Italy Collection",
	"The Lake Collection",
	"The Safehouse Collection",
	"The Train Collection"
	]

	csgostash.MainWebLinkScrapper()

	activeDropPoolCollectionLinks= []
	
	for eachCollectionKey in list_of_active_drop_collection:
		link_to_collection = csgostash_link_database [csgostash.keyHandler(None, eachCollectionKey)]
		activeDropPoolCollectionLinks.append(link_to_collection)
	
	Usercall_Passed_Link(activeDropPoolCollectionLinks)

	all_in_one_specified_droppool_data = []
	for each_collection_key in temporal_dataset_collection:
		for each_item in temporal_dataset_collection[each_collection_key]:
			all_in_one_specified_droppool_data.append(each_item)

	tier = tierMenu()
	if tier == "CLI":
		commandLine()

	wear = wearMenu()
	if wear == "CLI":
		commandLine()
	
	sorting = sortMenu()
	if sorting == "CLI":
		commandLine()

	scale = scaleMenu()
	if isinstance(scale,str):
		commandLine()

	print(all_in_one_specified_droppool_data,wear,tier,scale)
	time.sleep(5)
	displayer(all_in_one_specified_droppool_data,wear,tier,sorting,scale)


def specifiedCollectionMenu(): 

	statement = "Select multiple to continue :"
	header = ("Multiple Selection Enabled!")
	csgostash.MainWebLinkScrapper()
	specified_collection_menu_list =[] 
	for x in csgostash_link_database : specified_collection_menu_list.append(Key_Decrypter(x))
	specifiedCollectionMenuobj = Menu_CheckBox(specified_collection_menu_list,statement,header)
	return_value = specifiedCollectionMenuobj.main()

	link_to_collection_link = []
	if len(return_value) == 0:
		continueMenu()
	elif return_value != "CLI":
		for each_key_of_collection in return_value:
			each_key_of_collection = csgostash.keyHandler(None,each_key_of_collection)
			# print(csgostash_link_database[each_key_of_collection])
			link_to_collection_link.append(csgostash_link_database[each_key_of_collection])
		Usercall_Passed_Link(link_to_collection_link)
	
		all_in_one_data = []
		for each_data_of_collections in temporal_dataset_collection:
			for each_item in temporal_dataset_collection[each_data_of_collections]:
				all_in_one_data.append(each_item)
		
		tier = tierMenu()
		if tier == "CLI":
			commandLine()

		wear = wearMenu()
		if wear == "CLI":
			commandLine()
		sorting = sortMenu()
		if sorting == "CLI":
			commandLine()
		scale = scaleMenu()
		if isinstance(scale,str):
			commandLine()
		
		displayer(all_in_one_data,wear,tier,sorting,scale)
	else :
		commandLine()

def allCollectionMenu():
	
	print("All Collection feature coming soon!")
	time.sleep(1)
	continueMenu()

def scaleMenu():
	statement = "Please Select the scale of table : "
	list_of_scales = [1,5,10,20]
	listOfScalesobj = Menu_RadioButton(list_of_scales,statement)
	# print(type(listOfScalesobj.main()))
	return listOfScalesobj.main()

def sortMenu():
	statement = "Please Select the sorting order:"
	list_of_sorting_order = ["Tier : High to Low","Price : Low to High"]
	listOfSortingOrderobj = Menu_RadioButton(list_of_sorting_order,statement)
	return listOfSortingOrderobj.main()

def tierMenu():
	statement = "Please Select the tier : "
	list_of_tier = ["Covert","Classified","Restricted","Mil-Spec","Industrial Grade","Consumer Grade"]
	listOfTierobj = Menu_RadioButton(list_of_tier,statement)
	return listOfTierobj.main()

def wearMenu():
	statement = "Please Select the Wear : "
	list_of_wear = ["Factory New","Minimal Wear","Field-Tested","Well-Worn","Battle-Scarred"]
	listOfWearobj = Menu_RadioButton(list_of_wear,statement)
	return listOfWearobj.main()

def helper():
	os.system("cls")
	console.print("Trade up Helper for Counter Strike :Global Offensive",style = "green",justify="center")
	console.print("Please help me to add help. Send the difficulties you face on Discord : [red]Ol'SdudeNT#6969[/red]")
	print()
	print("Press any key to continue...")
	if getch():
		MainMenu()

def displayer(listOfData, wear = "Minimal Wear", tier = "Mil-Spec", sortOrder = "default",scale = 10):

	# print(f"Datas : {listOfData}, {wear}, {tier}, {sortOrder}, {scale}")
	headerText = (f"Sorting Order : {sortOrder}, Quality : {tier}, Wear : {wear}")
	footerText = "*N/A means the item(s) has no available price on SCM or the item(s) doesn't exist(s)." 
	table = Table(title = headerText,width=80,caption =footerText )
	table.add_column("Skin")
	table.add_column("Collection")
	table.add_column("Price")

	if scale > len(listOfData):
		scale = len(listOfData)
	
	if sortOrder == "Price : Low to High":
		new_sorted_list = listSorter(listOfData,wear,tier)
		if scale > len(new_sorted_list):
			scale = len(new_sorted_list)
		for index in range(scale):
			table.add_row(listOfData[new_sorted_list[index][0]][0]+' | '+listOfData[new_sorted_list[index][0]][1],listOfData[new_sorted_list[index][0]][4],listOfData[new_sorted_list[index][0]][3][wearIndex(wear)])
	else:
		tierformattedlist = TierFilter(listOfData,tier)
		if scale > len(tierformattedlist):
			scale = len(tierformattedlist)
		for x in range(scale):
			table.add_row(tierformattedlist[x][0]+' | '+tierformattedlist[x][1],tierformattedlist[x][4], tierformattedlist[x][3][wearIndex(wear)])
	os.system('cls')
	console.rule()
	console.print(table,justify="center")
	console.rule()

	print("Press ESC to quit or any key to return to menu..")
	key = ord(getch())
	if key == 27:
		exit()
	else:
		Usercall_Clear_Tempdb()
		print(temporal_dataset_collection)
		listOfData = []
		print(listOfData)
		# time.sleep(10)
		MainMenu()

def TierFilter(datalist,tier):
	list_of_new_data = []
	for eachElement in datalist:
		if eachElement[2] == tier:
			list_of_new_data.append(eachElement)
	return list_of_new_data


def listSorter(datas,wear,tier):
	list_of_indices = []
	sorted_list_indices = []
	weapon_wear_index = wearIndex(wear) 

	for eachItem in datas:
		if eachItem[2] == tier:
			list_of_indices.append((datas.index(eachItem),priceStripper(eachItem[3][weapon_wear_index])))
	
	while list_of_indices:
		minimun_value_tuple = list_of_indices[0]
		# print(minimun_value_tuple)
		for secindex in range(len(list_of_indices)):
			# print(list_of_indices[secindex][1])
			try:
				if minimun_value_tuple[1] > list_of_indices[secindex][1]:
						minimun_value_tuple = list_of_indices[secindex]
			except:
				pass
		sorted_list_indices.append(minimun_value_tuple)
		list_of_indices.remove(minimun_value_tuple)
	return sorted_list_indices

	
def priceStripper(text):
	if text == "N/A":
		return text
	else:
		return float(text.strip("$"))

def wearIndex(wear):
	if wear == "Factory New":
		return 0
	elif wear == "Minimal Wear":
		return 1
	elif wear == "Field-Tested":
		return 2
	elif wear == "Well-Worn":
		return 3
	elif wear == "Battle-Scarred":
		return 4
	else:
		return 0

def commandLine():
	pass

MainMenu()


