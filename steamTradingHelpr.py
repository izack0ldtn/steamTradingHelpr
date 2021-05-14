from termcolor import colored

collection_dustII = (
    ["SCAR 20","Sand Mesh",["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["Nova","Predator",["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["P90","Sand Spray",["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["MP9","Sand Dashed",["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["G3SG1","Desert Strom", ["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["P250","Sand Dune",["FN","MW","FT","WW","BS"],"Consumer Grade"],
    ["Sawed-Off","Snake Camo",["FN","MW","FT","WW","BS"],"Industrial Grade"],
    ["Tech-9","Vari Camo",["FN","MW","FT","WW","BS"],"Industrial Grade"],
    ["Five-SeveN","Orange Peel",["FN","MW","FT","WW","BS"],"Industrial Grade"],
    ["MAC-10","Palm",["FN","MW","FT","WW","BS"],"Industrial Grade"],
    ["AK-47","Safari Mesh",["FN","MW","FT","WW","BS"],"Industrial Grade"],
    ["PP-Bizon","Brass",["FN","MW","FT","WW","BS"],"Mil-Spec"],
    ["M4A1-S","Vari Camo",["FN","MW","FT","WW","BS"],"Mil-Spec"],
    ["SG 553","Damascus Steel",["FN","MW","FT","WW","BS"],"Mil-Spec"],
    ["P2000","Amber Fade",["FN","MW","FT","WW","BS"],"Restricted"],
    ["R8 Revolver","Amber Fade",["FN","MW","FT","WW","BS"],"Mil-Spec"]
)
#####################################
class parentWeapon:
    def __init__(self,weName,weSName,weSWear,weSTier):
        self.weName = weName
        self.weSName = weSName
        self.weSWear = weSWeard
        self.weSTier = weSTier
class Dust_II(parentWeapon):
    pass
def displayCollection():
    print("Dust II Collection : ")
    for x in range(len(collection_dustII)):
        weC_dustII = Dust_II(collection_dustII[x][0],collection_dustII[x][1],collection_dustII[x][2],collection_dustII[x][3])
        #print (f"{x+1}. {weC_dustII.weName} | {weC_dustII.weSName}")
        if weC_dustII.weSTier == "Consumer Grade":
            tempText = colored (f"{x+1}. {weC_dustII.weName} | {weC_dustII.weSName}",'grey')d
            print(tempText)
           
displayCollection()