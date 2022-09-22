####################################
# Cosmetics Plando Randomizer      #
# Generates a Cosmetics Plando     #
# if a plando file has two or more #
# options for a location           #
####################################
# Author: SonicRPika               #
####################################

import random, json

bgmDefault = [
    "Hyrule Field",
    "Dodongos Cavern",
    "Kakariko Adult",
    "Battle",
    "Boss Battle",
    "Inside Deku Tree",
    "Market",
    "Title Theme",
    "House",
    "Jabu Jabu",
    "Kakariko Child",
    "Fairy Fountain",
    "Zelda Theme",
    "Fire Temple",
    "Forest Temple",
    "Castle Courtyard",
    "Ganondorf Theme",
    "Lon Lon Ranch",
    "Goron City",
    "Miniboss Battle",
    "Temple of Time",
    "Kokiri Forest",
    "Lost Woods",
    "Spirit Temple",
    "Horse Race",
    "Ingo Theme",
    "Fairy Flying",
    "Deku Tree",
    "Windmill Hut",
    "Shooting Gallery",
    "Sheik Theme",
    "Zoras Domain",
    "Shop",
    "Chamber of the Sages",
    "Ice Cavern",
    "Kaepora Gaebora",
    "Shadow Temple",
    "Water Temple",
    "Gerudo Valley",
    "Potion Shop",
    "Kotake and Koume",
    "Castle Escape",
    "Castle Underground",
    "Ganondorf Battle",
    "Ganon Battle",
    "Fire Boss",
    "Mini-game",
    "Game Over",
    "Ganondorf Appears",
    "Heart Container Get",
    "Master Sword",
    "Boss Defeated",
    "Item Get",
    "Treasure Chest",
    "Spirit Stone Get",
    "Heart Piece Get",
    "Escape from Ranch",
    "Learn Song",
    "Epona Race Goal",
    "Medallion Get",
    "Zelda Turns Around",
    "Door of Time",
    "Prelude of Light",
    "Bolero of Fire",
    "Minuet of Forest",
    "Serenade of Water",
    "Requiem of Spirit",
    "Nocturne of Shadow",
    "Saria's Song",
    "Epona's Song",
    "Zelda's Lullaby",
    "Sun's Song",
    "Song of Time",
    "Song of Storms"
    ]

# Chooses a song based on criterium, and also returns the songs used
def randosong(locList, usedList, randoOpt):
    """locList is the list for the location
usedList is the list of songs currently plando'd to a location
randoOpt is the random option - true, possible, or fail"""

    # failsafe for if a string is parsed instead of a lisf
    if type(locList) == str:
        if locList not in usedList:
            usedList.append(locList)
        return locList, usedList

    # if it doesn't matter how many times a song has been used
    elif randoOpt == "true":
        selection = random.choice(locList)
        if selection not in usedList:
            usedList.append(selection)
        return selection, usedList

    # if an unique option is preferred
    else:
        remainOptions = locList
        for i in usedList:
            if i in remainOptions:
                remainOptions.remove(i)
        if len(remainOptions) == 0:

            # duplicates are possible, but prefer unique
            if randoOpt == "poss":
                selection = random.choice(locList)
                return selection, usedList

            # sets songs to "none" if cannot select a song
            elif randoOpt == "none":
                return "none", usedList

            # sets songs to default if cannot select a song
            elif randoOpt == "fvan":
                return "vanilla", usedList

            # skips the song
            else:
                return "skip", usedList
        
        else:
            selection = random.choice(remainOptions)
            usedList.append(selection)
            return selection, usedList

# Gets data from a .json file inputed, as well as the specific bgm dictionary
def jsonreader(base):
    try:
        originalFile = open(base)
        originalDict = json.load(originalFile)
        originalFile.close()
        return originalDict, originalDict["bgm"]
    except:
        return "error", "error"

# Formats options into a code that the program uses.
def codeGenerator(failList, genList):
    randoOptions = {
    "Choose from List":"true",
    "Unique preferred, duplicates ok":"poss",
    "Skip in Output file":"skip",
    "Replace with Vanilla":"fvan",
    "Replace with None":"None"
    }
    genOptions = {
    "Order of List":"order",
    "\"Smart\" Order":"smart",
    "Random Order":"random"
    }

    return randoOptions[failList], genOptions[genList]

# Special function for if the Generation is to be "smart"
# Basically chooses the location with the least options, to
# give the most potential for 
def smartRando(failOpt, bgm, locRando, locNum):
    """failOpt is what to do if the song is already in use
bgm is the bgm dictionary
locRando is the list of locations to have music randomized
locNum is a dictionary with the number of options in each list"""
    global bgmDefault
    # finds the songs already in use
    usedSongs = []
    for x in bgmDefault:
        try:
            if type(bgm[x]) == str:
                usedSongs.append(bgm[x])
        except:
            a = 1

    while locRando != []:
        locUsed = []
        checkValue = locNum[locRando[0]]
        # finds the location with the least options
        for i in locRando:
            check = locNum[i]
            if check < checkValue:
                locUsed = [i]
            elif check == checkValue:
                locUsed.append(i)

        # chooses a location with the least options and chooses the song for it
        locSelect = random.choice(locUsed)
        select, usedSongs = randosong(bgm[locSelect], usedSongs, failOpt)
        if select == "vanilla":
            bgm[locSelect] = locSelect
        elif select == "skip":
            del bgm[locSelect]
        else:
            bgm[locSelect] = select

        
        # cleans up for the next iteration
        if locNum[locSelect] > 0:
            for j in locRando:
                if select in bgm[j]:
                    locNum[j] = locNum[j] - 1
        del locNum[locSelect]
        a = locRando.remove(locSelect)
    return bgm

# Function to generate the song for each location
def selector(gen, ran, bgm, locRando, locLoc):
    """gen is the gen option
ran is the choice option
bgm is the bgm dictionary
locRando is the locations with multiple options
locLoc is the number of options for that location"""
    if gen == "smart":
        outputBGM = smartRando(ran, bgm, locRando, locLoc)
        return outputBGM
    else:
        global bgmDefault
        usedSongs = []
        for x in bgmDefault:
            try:
                if type(bgm[x]) == str:
                    usedSongs.append(bgm[x])
            except:
                a=1
        if gen == "order":
            for i in locRando:
                select, usedSongs = randosong(bgm[i], usedSongs, ran)
                if select == "vanilla":
                    bgm[i] = locSelect
                elif select == "skip":
                    del bgm[i]
                else:
                    bgm[i] = select
        else:
            while locRando != []:
                i = random.choice(locRando)
                select, usedSongs = randosong(bgm[i], usedSongs, ran)
                if select == "vanilla":
                    bgm[i] = locSelect
                elif select == "skip":
                    del bgm[i]
                else:
                    bgm[i] = select
                j = locRando.remove(i)
        return bgm

# Code that checks if there is any rando needed or not
def checkCode(bgm):
    global bgmDefault
    bgmRando = []
    bgmCount = {}
    for i in bgmDefault:
        try:
            check = bgm[i]
            if type(check) != str:
                bgmRando.append(i)
                bgmCount[i] = len(bgm[i])
        except:
            a = 1
    return bgmRando, bgmCount

# Main command, calls all other commands
def mainCode(f, e, r):
    """f is the original file
e is the rando option
r is the order"""
    allData, bgm = jsonreader(f)
    if allData == "error":
        return "error"
    randoOption, randoOrder = codeGenerator(e,r)
    locRando, locamount = checkCode(bgm)
    if locRando != []:
        bgm = selector(randoOrder, randoOption, bgm, locRando, locamount)
        allData["bgm"] = bgm
        return allData
    else:
        return allData
