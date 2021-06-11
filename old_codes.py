#data base#
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




def jsonStorer():
    MainWebLinkScrapper()
    with open('links.json','w') as linkfile:
        linkfile.write(json.dumps(csgostash_link_database))


def LinkStorageHandler():
    if os.path.isfile('links.json'):
        with open('links.json','r') as linkFile:
            try:
                tempMainLinkDict = json.loads(linkFile.read())
            except Exception as e:
                print(e)
                print ("No Proper JSON file")
                jsonStorer()
                tempMainLinkDict = json.loads(linkFile.read())
            if len(tempMainLinkDict) != 70:
                print("JSON file has been modified. Rewriting links.json")
                jsonStorer()
            else:
                csgostash_link_database = tempMainLinkDict
    else:
        MainWebLinkScrapper()
        jsonStorer()
