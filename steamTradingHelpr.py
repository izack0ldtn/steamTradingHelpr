from sys import exit
import requests
import rich
from tqdm import tqdm
from rich.console import Console 
from rich.table import Table
from functools import lru_cache
import os
import steamWeaponReceiver as scrapper 
os.system('color')
#####################################
cons = Console()
#####################################
globalCollectionList = ("DustII","Safehouse","Train") #Collection Names of those colllec. which has data in proggram
globalWeaponList = ("")
globalWearList = ("Factory New","Minimal Wear","Field-Tested","Well-Worn","Battle-Scarred")
#################################
#Collection Data. Dont Modify . Danger!!!!!!! + To be modified to tuples for memory management
collection_dustII = (
    ["SCAR-20","Sand Mesh",["FN","MW","FT","WW","BS"],"Consumer Grade","1"],    
    ["Nova","Predator",["FN","MW","FT","WW","BS"],"Consumer Grade","2"],
    ["P90","Sand Spray",["FN","MW","FT","WW","BS"],"Consumer Grade","3"],
    ["MP9","Sand Dashed",["FN","MW","FT","WW","BS"],"Consumer Grade","4"],
    ["G3SG1","Desert Storm", ["FN","MW","FT","WW","BS"],"Consumer Grade","5"],
    ["P250","Sand Dune",["FN","MW","FT","WW","BS"],"Consumer Grade","6"],
    ["Sawed-Off","Snake Camo",["FN","MW","FT","WW","BS"],"Industrial Grade","7"],
    ["Tec-9","VariCamo",["FN","MW","FT","WW","BS"],"Industrial Grade","8"],
    ["Five-SeveN","Orange Peel",["FN","MW","FT","WW","BS"],"Industrial Grade","9"],
    ["MAC-10","Palm",["FN","MW","FT","WW","BS"],"Industrial Grade","10"],
    ["AK-47","Safari Mesh",["FN","MW","FT","WW","BS"],"Industrial Grade","11"],
    ["PP-Bizon","Brass",["FN","MW","FT","WW","BS"],"Mil-Spec","12"],
    ["M4A1-S","VariCamo",["FN","MW","FT","WW","BS"],"Mil-Spec","13"],
    ["SG 553","Damascus Steel",["FN","MW","FT","WW","BS"],"Mil-Spec","14"],
    ["P2000","Amber Fade",["FN","MW","FT","WW","BS"],"Restricted","15"],
    ["R8 Revolver","Amber Fade",["FN","MW","FT","WW","BS"],"Classified","16"]
)

collection_safehouse = (
    ["SCAR-20","Contractor", ["FN","MW","FT","WW","BS"],"Consumer Grade","17"],
    ["Tec-9","Army Mesh",["FN","MW","FT","WW","BS"],"Consumer Grade","18"],
    ["SSG 08","Blue Spruce",["FN","MW","FT","WW","BS"],"Consumer Grade","19"],
    ["MP7", "Army Recon", ["FN","MW","FT","WW","BS"],"Consumer Grade","20"],
    ["Dual Berettas","Contractor", ["FN","MW","FT","WW","BS"],"Consumer Grade","21"],
    ["MP9","Orange Peel", ["FN","MW","FT","WW","BS"],"Industrial Grade","22"],
    ["Galil AR","VariCamo",["FN","MW","FT","WW","BS"],"Industrial Grade","23"],
    ["G3SG1", "VariCamo", ["FN","MW","FT","WW","BS"],"Industrial Grade","24"],
    ["AUG","Condemned",["FN","MW","FT","WW","BS"],"Industrial Grade","25"],
    ["USP-S","Forest Leaves",["FN","MW","FT","WW","BS"],"Industrial Grade","26"],
    ["M249","Gator Mesh",["FN","MW","FT","WW","BS"],"Industrial Grade","27"],
    ["Five-SeveN","Silver Quartz",["FN","MW","FT","WW"],"Mil-Spec","28"],
    ["FAMAS","Teardown",["FN","MW","FT","WW","BS"],"Mil-Spec","29"],
    ["SSG 08","Acid Fade",["FN"],"Mil-Spec","30"],
    ["M4A1-S","Nitro",["FN","MW","FT","WW","BS"],"Restricted","31"]
)

collection_train = (
    ["Nova","Polar Mesh",["FN","MW","FT","WW","BS"],"Consumer Grade","32"],
    ["Dual Berettas","Colony",["FN","MW","FT","WW","BS"],"Consumer Grade","33"],
    ["PP-Bizon","Urban Dashed",["FN","MW","FT","WW","BS"],"Consumer Grade","34"],
    ["UMP-45","Urban DDPAT",["FN","MW","FT","WW","BS"],"Consumer Grade","35"],
    ["Five-SeveN","Forest Night",["FN","MW","FT","WW","BS"],"Consumer Grade","36"],
    ["G3SG1","Polar Camo",["FN","MW","FT","WW","BS"],"Consumer Grade","37"],
    ["P90","Ash Wood",["FN","MW","FT","WW","BS"],"Industrial Grade","38"],
    ["MAG-7","Metallic DDPAT",["FN","MW","FT","WW","BS"],"Industrial Grade","39"],
    ["SCAR-20","Carbon Fiber",["FN","MW","FT","WW","BS"],"Industrial Grade","40"],
    ["P250","Metallic DDPAT",["FN","MW","FT","WW","BS"],"Industrial Grade","41"],
    ["MAC-10","Candy Apple",["FN","MW","FT","WW","BS"],"Industrial Grade","42"],
    ["M4A4","Urban DDPAT",["FN","MW","FT","WW","BS"],"Industrial Grade","43"],
    ["Sawed-Off","Amber Fade",["FN","MW","FT","WW"],"Mil-Spec","44"],
    ["Desert Eagle","Urban Rubble",["FN","MW","FT","WW","BS"],"Mil-Spec","45"],
    ["Tec-9","Red Quartz",["FN","MW","FT","WW","BS"],"Restricted","46"]
)
#####################################
#####################################
def getStyle(tier): #Returns coloured text using colored module. Initially made for displaycollection func. Added to getskinsbyweapon

    if tier == "Consumer Grade":
        return "white"
    elif tier == "Industrial Grade":
        return "bright_cyan"
    elif tier == "Mil-Spec":
        return "bright_blue"
    elif tier == "Restricted":
        return "purple"
    elif tier == "Classified":
        return "bright_magenta"


def getSkinsByWeapon(weaponName):
    tempAppender = []
    for x in collection_dustII:
        if x[0] == weaponName:
            #return (f"{x[0]} | {x[1]}",x[3])
            tempStore = colorProvider(f"{x[0]} | {x[1]}",x[3])
            tempAppender.append(tempStore)
    for x in collection_safehouse:
        if x[0] == weaponName:
            tempStore = colorProvider(f"{x[0]} | {x[1]}", x[3])
            tempAppender.append(tempStore)
    for x in collection_train:
        if x[0] == weaponName:
            tempStore = colorProvider(f"{x[0]} | {x[1]}", x[3])
            tempAppender.append(tempStore)
    if len(tempAppender)!=0:
        return tempAppender
    else:
        return f"{weaponName} not in database."
@lru_cache(maxsize = None)
def linkBuilder(weaponName,weaponSkinName, weaponWear): #as fine as the 1st code
    firstHolder = "https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name="
    if wearBuilder(weaponWear) in globalWearList:
        weaponWear = wearBuilder(weaponWear)
    if weaponWear not in globalWearList:
        return f"{weaponWear} or {weaponName} {weaponSkinName} is not valid."
    else:
        return f"{firstHolder}{weaponName}%20%7C%20{weaponSkinName}%20%28{weaponWear}%29"
@lru_cache(maxsize = None)
def getWeaponPrice(weaponName,weaponSkinName,weaponWear):
    dictForPrice = requests.get(linkBuilder(weaponName,weaponSkinName,weaponWear)).json()
    # print (dictForPrice)
    if dictForPrice['success'] == True:
            tempPrice = dictForPrice['lowest_price']
            return float(tempPrice.strip("$"))
    else:
        raise Exception ("Failed to retrive data from steam's server! Please try again!")

def wearBuilder(str):
    localWears =("FN","MW","FT","WW","BS")
    if str not in  localWears:
        return None
    elif str == "FN":
        return "Factory New"
    elif str == "MW":
        return "Minimal Wear"
    elif str == "FT":
        return "Field-Tested"
    elif str == "WW":
        return "Well-Worn"
    elif str == "BS":
        return "Battle-Scarred"
    return None
        
def sorter(listR):
    n =1
    le = len(listR)
    cons.print("Sorting Lists .....",style ="red",justify = "center")
    for x in tqdm(range(le)):
        if n<le:
            for y in range(n,le):
                if listR[x][1] > listR[y][1]:
                    listR[x],listR[y] = listR[y],listR[x]
        n+= 1
    return listR

def tableSorter(listR,collectionName,sortingForm):
    if sortingForm == "cf":
        sortedList = sorter(listR)
    elif sortingForm == "n":
        sortedList = listR
    else:
        raise Exception(f"{sortingForm} is not sorting order.")
        
    if collectionName == "DustII":
        localCollectionList = collection_dustII
    elif collectionName == "Train":
        localCollectionList = collection_train
    elif collectionName == "Safehouse":
        localCollectionList = collection_safehouse
    else:
        raise Exception("Error: Collection Name is not available.")
    table_dust =Table(title = collectionName)
    table_dust.add_column("sn.")
    table_dust.add_column("Weapon")
    table_dust.add_column("Skin")
    table_dust.add_column("Price",justify = "right")
    for x in range(len(sortedList)):
        for y in range(len(localCollectionList)):
            # print(sortedList[x][0],collection_dustII[y][4])
            if sortedList[x][0] == localCollectionList[y][4]:
                table_dust.add_row(str(x+1),localCollectionList[y][0],localCollectionList[y][1],str(sortedList[x][1]),style= getStyle(localCollectionList[y][3]))
    console = Console()
    console.print(table_dust,justify="center")


def helper():
    cons.rule("[green]FOR WEAPON COLLECTION")
    print("type d2 for dustII collection")
    print("type sh for Safehouse collection")
    print("type tr for Train collection")
    print(f"Available collecetion : {globalCollectionList}")
    cons.rule("[blue]FOR SORTING ORDER")
    print("type n for sorting accourding to tier")
    print("type cf for the cheapest first sorting")
    cons.rule("[yellow]FOR WEAPON WEARS")
    print("Type FN for Factory New")
    print("Type MW for Minimal Wear")
    print("Type FT for Field-Tested")
    print("Type WW for Well-Worn")
    print("Type BS for Battle-Scarred")
    cons.rule("[red]OTHER FUCNTIONS")
    print("type end to quit the program.")
    print("type back to return back")
#####################################
#####################################


class parentWeapon: # Base Class for Holding Skins. Made for inheritance.
    def __init__(self,weName,weSName,weSWear,weSTier):
        self.weName = weName
        self.weSName = weSName
        self.weSWear = weSWear
        self.weSTier = weSTier

class Dust_II(parentWeapon): # For D2 Collc. JUST FOR OBJECT #TBD
    collectionName = "The Dust II Collection"
class safehouse(parentWeapon): # For SF Collc. JUST FOR OBJ #TBD
    collectionName = "The Safehouse Collection"
class Train(parentWeapon):
    collectionName = "The Train Collection"



def displayCollection(globalCollectionName,wearPass): #Displays Collection skins by taking argument as collection name. if passed allCol then displays all available collecotion
    dataHolder =[]
    if  globalCollectionName not in globalCollectionList: #Displays Error if not in Global Collection Lists
        print (f"{globalCollectionName} not in collection")
    cons.print("Fecthing Data from Steam's Server...",style ="red",justify="center")
    if globalCollectionName == "DustII" or globalCollectionName == "all" :
        for x in tqdm(range(len(collection_dustII))):
            weC_dustII = Dust_II(collection_dustII[x][0],collection_dustII[x][1],collection_dustII[x][2],collection_dustII[x][3])
            dataHolder.append((collection_dustII[x][4],getWeaponPrice(weC_dustII.weName,weC_dustII.weSName,wearPass)))
        if globalCollectionName == "all":
            pass
        else:
            return dataHolder
        print()

    if globalCollectionName == "Safehouse" or globalCollectionName == "all" :
        for x in tqdm(range (len(collection_safehouse))):
            weC_safehouse = safehouse(collection_safehouse[x][0],collection_safehouse[x][1],collection_safehouse[x][2],collection_safehouse[x][3])
            dataHolder.append((collection_safehouse[x][4],getWeaponPrice(weC_safehouse.weName,weC_safehouse.weSName,wearPass)))
        if globalCollectionName == "all":
            pass
        else:
            return dataHolder
        print()
    if globalCollectionName == "Train" or globalCollectionName == "all" :
        for x in tqdm(range (len(collection_train))):
            weC_train = Train(collection_train[x][0],collection_train[x][1],collection_train[x][2],collection_train[x][3])
            dataHolder.append((collection_train[x][4],getWeaponPrice(weC_train.weName,weC_train.weSName, wearPass)))
        if globalCollectionName == "all":
            pass
        else:
            return dataHolder
        print()
    if globalCollectionName == "all": #TODO
        return dataHolder

cons.rule()
cons.print("STEAM TRADING HELPR ALPHA 0.0.1",justify = "center",style= "black on white")
cons.rule()
cons.print("Welcome to STEAM TRADING HELPR. THIS IS THE FIRST VERSION OF THE PROGRAM. WARNING! ITS UNSTABLE. SURPLUS THIS PROGRAM DOESN'T HAVE THE FUCTION ITS CREATOR MENTIONED. THIS IS JUST PRE-ALPHA RELEASE. TO START UP PRESS '-h' FOR HELP AND COMMANDS.",overflow= "fold",style= "bold red")
# while True:
#     commandInput = input("STEAM TRADING HELPR 0.0.1 : ")
#     if commandInput == "-h"or commandInput == "-H":
#         helper()
#     elif commandInput == "-v" or commandInput == "-V":
#         cons.print("[bold red]Version PRE-ALPHA 0.0.1")
#     elif commandInput == "end" or commandInput == "END":
#         exit()
#     elif commandInput == "d2" or commandInput == "d2 cf":
#         wearStore = input("Enter the wear : ")
#         if wearStore == "back" or wearBuilder(wearStore) not in globalWearList:
#             pass
#         elif commandInput == "d2 cf":
#             tableSorter(displayCollection("DustII",wearBuilder(wearStore)),"DustII","cf")
#         else:
#             tableSorter(displayCollection("DustII",wearBuilder(wearStore)),"DustII","n")
#     elif commandInput == "sf" or commandInput == "sf cf":
#         wearStore = input("Enter the wear : ")
#         if wearStore == "back" or wearBuilder(wearStore) not in globalWearList:
#             pass
#         if commandInput == "sf cf":
#             tableSorter(displayCollection("Safehouse",wearBuilder(wearStore)),"Safehouse","cf")
#         else:
#             tableSorter(displayCollection("Safehouse",wearBuilder(wearStore)),"Safehouse","n")
#     elif commandInput == "tr" or commandInput == "tr cf":
#         wearStore = input("Enter the wear: ")
#         if wearStore == "back" or wearBuilder(wearStore) not in globalWearList:
#             pass
#         elif commandInput == "tr cf":
#             tableSorter(displayCollection("Train",wearBuilder(wearStore)),"Train","cf")
#         else:
#             tableSorter(displayCollection("Train",wearBuilder(wearStore)),"Train","n")
#     else:
#         cons.print("[bold red] Keyword error. please write in correct form.")
collectionDustII = scrapper.collectionDatabaseCreator("https://csgostash.com/collection/The+Dust+2+Collection")
for x in collectionDustII:
    print(x)