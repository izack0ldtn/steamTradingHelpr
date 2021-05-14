from termcolor import colored #Colouring Text Module. To be replaced by proper module
#####################################
#####################################
globalCollectionList = ("DustII","Safehouse") #Collection Names of those colllec. which has data in proggram
#################################
#Collection Data. Dont Modify . Danger!!!!!!! + To be modified to tuples for memory management
collection_dustII = (
    ["SCAR 20","Sand Mesh",["FN","MW","FT","WW","BS"],"Consumer Grade","1"],
    ["Nova","Predator",["FN","MW","FT","WW","BS"],"Consumer Grade","2"],
    ["P90","Sand Spray",["FN","MW","FT","WW","BS"],"Consumer Grade","3"],
    ["MP9","Sand Dashed",["FN","MW","FT","WW","BS"],"Consumer Grade","4"],
    ["G3SG1","Desert Strom", ["FN","MW","FT","WW","BS"],"Consumer Grade","5"],
    ["P250","Sand Dune",["FN","MW","FT","WW","BS"],"Consumer Grade","6"],
    ["Sawed-Off","Snake Camo",["FN","MW","FT","WW","BS"],"Industrial Grade","7"],
    ["Tec-9","Vari Camo",["FN","MW","FT","WW","BS"],"Industrial Grade","8"],
    ["Five-SeveN","Orange Peel",["FN","MW","FT","WW","BS"],"Industrial Grade","9"],
    ["MAC-10","Palm",["FN","MW","FT","WW","BS"],"Industrial Grade","10"],
    ["AK-47","Safari Mesh",["FN","MW","FT","WW","BS"],"Industrial Grade","11"],
    ["PP-Bizon","Brass",["FN","MW","FT","WW","BS"],"Mil-Spec","12"],
    ["M4A1-S","Vari Camo",["FN","MW","FT","WW","BS"],"Mil-Spec","13"],
    ["SG 553","Damascus Steel",["FN","MW","FT","WW","BS"],"Mil-Spec","14"],
    ["P2000","Amber Fade",["FN","MW","FT","WW","BS"],"Restricted","15"],
    ["R8 Revolver","Amber Fade",["FN","MW","FT","WW","BS"],"Classified","16"]
)

collection_safehouse = (
    ["SCAR 20","Contractor", ["FN","MW","FT","WW","BS"],"Consumer Grade","17"],
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

)
#####################################
#####################################
def colorProvider(str,tier): #Returns coloured text using colored module. Initially made for displaycollection func.

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

def getSkinsByWeapon(weaponName): #TODO
    pass
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


def displayCollection(globalCollectionName): #Displays Collection skins by taking argument as collection name. if passed allCol then displays all available collecotion

    if  globalCollectionName not in globalCollectionList: #Displays Error if not in Global Collection Lists
        print (f"{globalCollectionName} not in collection")
    if globalCollectionName == "DustII" or globalCollectionName == "allCol" :
        print("Dust II Collection : ")
        for x in range(len(collection_dustII)):
            weC_dustII = Dust_II(collection_dustII[x][0],collection_dustII[x][1],collection_dustII[x][2],collection_dustII[x][3])
            #print (f"{x+1}. {weC_dustII.weName} | {weC_dustII.weSName}")
            tempText = f"{weC_dustII.weName} | {weC_dustII.weSName}"
            colorReciever = colorProvider(tempText,weC_dustII.weSTier)
            print(f"{x+1}. {colorReciever}")
        print()

    if globalCollectionName == "Safehouse" or globalCollectionName == "allCol" :
        print ("Safehouse Collection : ")
        for x in range (len(collection_safehouse)):
            weC_safehouse = safehouse(collection_safehouse[x][0],collection_safehouse[x][1],collection_safehouse[x][2],collection_safehouse[x][3])
            tempText = f"{weC_safehouse.weName} | {weC_safehouse.weSName}"
            colorReciever = colorProvider(tempText,weC_safehouse.weSTier)
            print(f"{x+1}. {colorReciever}")
        print()
    if globalCollectionName == "":
        pass

displayCollection("")





