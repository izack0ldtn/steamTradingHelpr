import steamWeaponReceiver as csgostash
from steamWeaponReceiver import collection_database
import os
from functools import lru_cache
import time
from rich.console import Console
console = Console()

temporal_dataset_collection = {} #stores the data that collection_database data and can be cleared by user


def Key_Decrypter(text): #Decryptes the csgostash_link_database's dictionary's key into normal looking text. For displaying in console.
	textList = text.split("_")
	textList.pop(0)
	for x in range(len(textList)): textList[x] = textList[x].capitalize() 
	return " ".join(textList)

def Usercall_Passed_Link(link):
	csgostash.Collection_Database_Feeder(link)
	for eachKey in collection_database:
		if eachKey not in temporal_dataset_collection:
			temporal_dataset_collection[eachKey] = collection_database[eachKey]

def Usercall_Clear_Tempdb():
	global temporal_dataset_collection
	temporal_dataset_collection = {}


###########################
# Console Interface Below #
###########################

 def main():
	console.print("steamTradingHelprV2",style = "bold red on white",justify = 'center')
	console.print("Powered By CSGOSTASH®",justify ="center")