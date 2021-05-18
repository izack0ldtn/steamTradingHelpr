from termcolor import colored #Colouring Text Module. To be replaced by proper module. Proper module as Rich i guess
import requests
import rich
from rich.console import Console 
from rich.table import Table
import os
os.system('color')
#####################################
cons = Console()
#####################################
globalCollectionList = ("DustII","Safehouse") #Collection Names of those colllec. which has data in proggram
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
    ["Galil AR","Vari Camo",["FN","MW","FT","WW","BS"],"Industrial Grade","23"],
    ["G3SG1", "Vari Camo", ["FN","MW","FT","WW","BS"],"Industrial Grade","24"],
    ["AUG","Condemned",["FN","MW","FT","WW","BS"],"Industrial Grade","25"],
    ["USP-S","Forest Leaves",["FN","MW","FT","WW","BS"],"Industrial Grade","26"],
    ["M249","Gator Mesh",["FN","MW","FT","WW","BS"],"Industrial Grade","27"],
    ["Five-SeveN","Silver Quartz",["FN","MW","FT","WW"],"Mil-Spec","28"],
    ["FAMAS","Tear Down",["FN","MW","FT","WW","BS"],"Mil-Spec","29"],
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
def colorProvider(str,tier): #Returns coloured text using colored module. Initially made for displaycollection func. Added to getskinsbyweapon

    if tier == "Consumer Grade":
        return colored(f"{str}", 'grey')
    elif tier == "Industrial Grade":
        return colored(f"{str}", 'cyan')
    elif tier == "Mil-Spec":
        return colored(f"{str}", 'blue')
    elif tier == "Restricted":
        return colored(f"{str}", 'green')
    elif tier == "Classified":
        return colored(f"{str}", 'magenta')


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

def linkBuilder(weaponName,weaponSkinName, weaponWear): #as fine as the 1st code
    firstHolder = "https://steamcommunity.com/market/priceoverview/?currency=1&appid=730&market_hash_name="
    if weaponWear not in globalWearList:
        return f"{weaponWear} or {weaponName} {weaponSkinName} is not valid."
    else:
        return f"{firstHolder}{weaponName}%20%7C%20{weaponSkinName}%20%28{weaponWear}%29"
    ########Below Code was initially made to check this fucntion's functionality########
    # if weaponWear == globalWearList[0] or weaponWear == globalWearList[1]:
    #     tempHolder = weaponWear.split()
    #     fLink = f"{firstHolder}{weaponName}%20%7C%20{weaponSkinName}%20%28{tempHolder[0]}%20{tempHolder[1]}%29"
    #     return fLink

def getWeaponPrice(weaponName,weaponSkinName,weaponWear):
    dictForPrice = requests.get(linkBuilder(weaponName,weaponSkinName,weaponWear)).json()
    # print (dictForPrice)
    if dictForPrice['success'] == True:
        tempPrice = dictForPrice['lowest_price']
        # print (type(tempPrice))
        return tempPrice
    else:
        return None

def wearBuilder(str):
    localWears =("FN","MW","FT","WW","BS")
    if str not in  localWears:
        return None
    elif str == "FN":
        return "Factory New"
    elif str == "MW":
        return "Minimal Wear"
    elif srt == "FT":
        return "Field-Tested"
    elif str == "WW":
        return "Well-Worn"
    elif str == "BS":
        return "Battle-Scarred"
    return None
        

#####################################
#####################################


class parentWeapon: # Base Class for Holding Skins. Made for inheritance.
    def __init__(self,weName,weSName,weSWear,weSTier):
        self.weName = weName
        self.weSName = weSName
        self.weSWear = weSWear
        self.weSTier = weSTier

    # def tableConstructors(self,specifiedWear,weSPrice):
    #     self.specifiedWear = specifiedWear
    #     self.weSPrice = weSPrice

    #     ############################
    #     print(self.weName,self.weSName,self.specifiedWear,self.weSPrice)
    #     table = Table(title = "DustII")
    #     table.add_row(self.weName,self.weSName,self.specifiedWear,self.weSPrice)




class Dust_II(parentWeapon): # For D2 Collc. JUST FOR OBJECT #TBD
    collectionName = "The Dust II Collection"
class safehouse(parentWeapon): # For SF Collc. JUST FOR OBJ #TBD
    collectionName = "The Safehouse Collection"
class Train(parentWeapon):
    collectionName = "The Train Collection"



def displayCollection(globalCollectionName): #Displays Collection skins by taking argument as collection name. if passed allCol then displays all available collecotion

    if  globalCollectionName not in globalCollectionList: #Displays Error if not in Global Collection Lists
        print (f"{globalCollectionName} not in collection")
    if globalCollectionName == "DustII" or globalCollectionName == "all" :
        table = Table(title = "DustII")
        table.add_column("sn. ")
        table.add_column("Weapon")
        table.add_column("Skin name")
        table.add_column("Wear")
        table.add_column("Price")
        for x in range(len(collection_dustII)):
            weC_dustII = Dust_II(collection_dustII[x][0],collection_dustII[x][1],collection_dustII[x][2],collection_dustII[x][3])
            table.add_row(str(x+1),weC_dustII.weName,weC_dustII.weSName,"Factory New",getWeaponPrice(weC_dustII.weName,weC_dustII.weSName,"Factory New"))
            #,.............getWeaponPrice(collection_dustII[x][0],collection_dustII[x][1])
            #..............print (f"{x+1}. {weC_dustII.weName} | {weC_dustII.weSName}")
            # print (f"{collection_dustII[x][0],collection_dustII[x][1],collection_dustII[x][2],collection_dustII[x][3]}")
            # weC_dustII.tableConstructors(wearBuilder("FN"),getWeaponPrice(collection_dustII[x][0],collection_dustII[x][1],wearBuilder("FN")))
            # table.add_row("Hello","Hi","NI","GA")
            # tempText = f"{weC_dustII.weName} | {weC_dustII.weSName}"
            # colorReciever = colorProvider(tempText,weC_dustII.weSTier)
            # print(f"{x+1}. {colorReciever}")
        cons.print(table)
        print()

    if globalCollectionName == "Safehouse" or globalCollectionName == "all" :
        print ("Safehouse Collection : ")
        for x in range (len(collection_safehouse)):
            weC_safehouse = safehouse(collection_safehouse[x][0],collection_safehouse[x][1],collection_safehouse[x][2],collection_safehouse[x][3])
            tempText = f"{weC_safehouse.weName} | {weC_safehouse.weSName}"
            colorReciever = colorProvider(tempText,weC_safehouse.weSTier)
            print(f"{x+1}. {colorReciever}")
        print()
    if globalCollectionName == "Train" or globalCollectionName == "all" :
        print ("Train Collection : ")
        for x in range (len(collection_train)):
            weC_train = Train(collection_train[x][0],collection_train[x][1],collection_train[x][2],collection_train[x][3])
            tempText = f"{weC_train.weName} | {weC_train.weSName}"
            colorReciever = colorProvider(tempText,weC_train.weSTier)
            print(f"{x+1}. {colorReciever}")
        print()
    if globalCollectionName == "": #TODO
        pass

# while True: # Command line tester LMAO
#     command = input("Enter the weapon name: ")
#     if getSkinsByWeapon(command) == None:
#         print(f"{command} not available in collections.")
#     else:
#         for x in range(len(getSkinsByWeapon(command))):
#             print(getSkinsByWeapon(command)[x])


# print (getWeaponPrice("SG 553","Cyrex","Field-Tested"))
# print (linkBuilder("AK-47","Asiimov","Field-Tested"))
displayCollection("DustII")
# print (wearBuilder("FN"))




