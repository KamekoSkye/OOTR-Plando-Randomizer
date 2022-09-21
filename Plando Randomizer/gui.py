from tkinter import *
from tkinter import messagebox, filedialog, ttk
import os
import main, filesmanager


loadupLoc = filesmanager.loadupStuff()
if loadupLoc["base"] == os.getcwd():
    filltemp = ""
else:
    filltemp = "anything"

# some code that is needed to be able to run commands from buttons
def getBase():
    global loadupLoc
    x = loadupLoc["base"].split("/")
    del x[len(x)-1]
    loc = "/".join(x)
    fileGet = filesmanager.getPlando(loc)
    if len(fileGet) > 0:
        fileText.delete(0,len(fileText.get()))
        fileText.insert(END, fileGet)
        loadupLoc["base"] = fileGet
        filesmanager.saveSettings(loadupLoc, loadupLoc["filename"])

def changeloadupLoc(a):
    global loadupLoc
    loadupLoc["defOpt"] = randoVar.get()
    loadupLoc["genOptions"] = genVar.get()
    filesmanager.saveSettings(loadupLoc, loadupLoc["filename"])
    

def finishFile():
    global randoVar, genVar
    baseFile = fileText.get()
    xyz = baseFile
    baseDir = xyz.split("/")
    try:
        baseCheck = baseDir[-1].split(".")
    except:
        baseCheck = ["none"]
    if baseFile == "" or baseCheck[-1] != "json":
        messagebox.showerror("No Plando File", "No plando file selected. Please select a plando file to continue")
        return
    r, g = randoVar.get(), genVar.get()
    item = main.mainCode(baseFile, r, g)
    if item == "error":
        messagebox.showerror("No Plando File", "Invalid directory. Please select a plando file to continue")
    baseName = baseDir.pop().split(".json")[0]
    filesmanager.printPlando(
        item,
        "/".join(baseDir),
        baseName,
        outputText.get()
        )
    messagebox.showinfo("Complete", "File generated. You are free to Rando! Note that I do not check to see if the music is valid, so any errors check your files")

# lists for the program
randoOptions = [
    "Choose from List",
    "Unique preferred, duplicates ok",
    "Skip in Output file",
    "Replace with Vanilla",
    "Replace with None"
    ]

genOptions = [
    "Order of List",
    "\"Smart\" Order",
    "Random Order"
    ]

root = Tk()
root.title("Music Cosmetics Plando selector")

loadup = Frame(root)

loadupLabels = Frame(loadup)
loadupText = Frame(loadup)
loadupButtons = Frame(loadup)

fileLabel = Label(loadupLabels, text="Base Cosmetics Plando File:")                  
fileLabel.pack(side=TOP, anchor=E)

fileText = Entry(loadupText)
fileText.configure(width=50)
fileText.pack(side=TOP, fill=X, expand=True ,padx=5)
fileButton = Button(loadupButtons,
                    command = getBase,
                    text = "Select Base Plando File",
                    width = 20)
fileButton.pack(side=TOP, anchor=N)

outputLabel = Label(loadupLabels, text="New File Name:")
outputLabel.pack(side=TOP, anchor=E, pady=5)

outputText = Entry(loadupText)
if filltemp != "":
    fileText.insert(END,loadupLoc["base"])
outputText.configure(width=50)
outputText.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)

loadupLabels.pack(side=LEFT)
loadupText.pack(side=LEFT,expand=True, fill=X)
loadupButtons.pack(side=LEFT, anchor=N)
loadup.pack(side=TOP, anchor=N, padx=5, pady=5, expand=True, fill=X)

optFrame = Frame(root)
randoVar = StringVar(optFrame)
randoVar.set(loadupLoc["defOpt"])
genVar = StringVar(optFrame)
genVar.set(loadupLoc["genOptions"])

randoLabel = Label(optFrame, text="List Handling:")
randoLabel.pack(side=LEFT, anchor=E)
randoBox = OptionMenu(optFrame, randoVar, *randoOptions, command=changeloadupLoc)
randoBox.pack(side=LEFT, anchor=W, padx=5)
genLabel = Label(optFrame, text="Selection Order:")
genLabel.pack(side=LEFT, anchor=E)
genBox = OptionMenu(optFrame, genVar, *genOptions, command=changeloadupLoc)
genBox.pack(side=LEFT, anchor=W, padx=5)

optFrame.pack(side=TOP, anchor=N, padx=5, pady=5, fill=X)

generateButton = Button(root,
                        command=finishFile,
                        text = "Generate File")
generateButton.pack(side=TOP, anchor=NE, padx = 10, pady = 10)

root.minsize(800,10)
root.mainloop()
