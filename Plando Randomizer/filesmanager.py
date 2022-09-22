from tkinter import filedialog
import json, os

# gets the initial data needed
def loadupStuff():
    dataLoc = os.getcwd() + "/data.json"
    try:
        settings = open(dataLoc, "r")
        i = json.load(settings)
        settings.close()
        return i
    except:
        settings = open(dataLoc, "w")
        settings.close()
        return {"filename":dataLoc, "base":os.getcwd(), "defOpt":"Choose from List", "genOptions":"Order of List"}

def saveSettings(dictItem, baseLoc):
    json_file = json.dumps(dictItem, indent=4)
    outfile = open(baseLoc, "w+")
    outfile.write(json_file)
    outfile.close()
    

# Command to read the json file
def getPlando(c):
    fileLoc = filedialog.askopenfilename(filetypes=[("JSON files", ".json")], title="Select json File", initialdir=c)
    return fileLoc

# Command to write the json file
def printPlando(item, location, base, name):
    if name == "" or name == base or name == "data":
        name = base + " randomized"
    json_file = json.dumps(item, indent=4)
    outfile = open(location + "/" + name + ".json", "w+")
    outfile.write(json_file)
    outfile.close()
