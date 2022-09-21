# OOTR Cosmetics Plando Randomizer
A program for OOTR that allows you to create a valid cosmetics plandomizer file if you want locations to have a random choice of songs

## What does this program do?
This program takes a .json file that you would use as a cosmetics plandomizer for OOTR, and looks for any lists in the "bgm" section of the file. If any exists, it will randomly select a song to be placed there based on what order the program is told to turn lists into one option, and how you want to handle duplicates.

The different options for duplicate handling are as follows:
### Vanilla Music
Will replace impossible to place locations with the vanilla music for that area or fanfare.
### No Music
Will change the list to the string "None", meaning no music will play for that area or fanfare.
### Skip that location
Will skip that location, removing it from the plando file so that any music can be placed there
### Unique preferred
This option will try to put an unique song in the location. When this is impossible, it will place any song in the list for that area or fanfare
### Duplicates ok
It doesn't matter if a duplicate shows up or not, it'll just choose an item from the list.

### Wait, duplicates??
When you use a cosmetics plandomizer, the OOTR program can place the same song or fanfare on multiple locations (provided you don't but a bgm sound on a fanfare, or vice versa). This program takes advantage of that so that it can always generate a valid .json file.

## Generation ordering
The program comes with three methods for choosing which order to choose which location or fanfare is done:

### Random order
While there is a list in the `bgm` section of the plando file, it will choose a location at random to select a song from the list

### In order
The program will assign each location its option based on the internal order that a typical cosmetics spoiler would show it in.

### Smart order
The program works in a smart manner - it'll take the smallest sized list and assign the song to it first, reducing the size of each other list by 1 if it contained the chosen song. This allows for potentially the most number of unique songs if that is what you are after.

## How to use this program
1) Download all the python files to an accessible location on your computer. Please make sure that whatever folder you download the files into, that `data.json` does not exist.
2) Create your cosmetics plandomizer file. This can be done with a program, or by taking an older cosmetics spoiler and adding a list (done by, next to an option you want multiple options, putting square brackets around each song separated by a comma) as the option. PLEASE REMEMBER THE LIST NEEDS TO BE FOLLOWED BY A COMMA.
3) Load up `gui.py` and, using the interface, select the original plandomizer file.
4) After selecting the options present, hit `Generate File` and it'll create a new .json file for you to use as your cosmetics plandomizer file.
5) Next time you want to shuffle up the songs, just hit `Generate File` again - the program stores the last used base file and randomization options in `data.json` for quick setup.
