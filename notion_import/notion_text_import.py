import os
from datetime import datetime
from re import search
from time import sleep

import clipboard
import pyautogui

def waitForEntry():
    if pyautogui.locateOnScreen('img/created.png') is None:
        # we are outside the bip
        print('outside entry screen, waiting 1s')
        sleep(1)
        waitForEntry()
    else:
        return

entryFiles = os.listdir('entries')
entriesFormatted = []

for entry in entryFiles:
    newEntry = entry.split('-')[0]
    os.rename('./entries/' + entry, './entries/' + newEntry)
    entriesFormatted.append(newEntry)

entriesFormatted = sorted(entriesFormatted)

for entry in entriesFormatted:
    number = int(entry.replace('entry', ''))
    if number < 100:
        if number < 10:
            numberStr = '00' + str(number)
        else:
            numberStr = '0' + str(number)
    else:
        numberStr = str(number)
    filename = './entries/entry' + numberStr
    file = open(filename, 'r').read().split('\n\n', 1) # create an array, 0 is the entry title (date and number), 1 is the entry content

    # all data formatted, now write into notion

    # get the date of the entry into standard datetime
    if "Journal, " in file[0]:
        date = file[0].split('Journal, ')[1].split(' Ent')[0]
    else:
        firstInt = search(r"\d", file[0]).start()
        secondInt = search(' Entry', file[0]).start()
        print(firstInt)
        date = file[0][firstInt:][:secondInt]
    date = datetime.strptime(date, '%y %B %d')
    dateStr = date.strftime('%b %d, %Y')
    print(f"copying entry {numberStr}, {dateStr}")
    pyautogui.click('img/new.png')
    sleep(.2)
    waitForEntry()
    clipboard.copy(dateStr)
    pyautogui.hotkey('ctrl', 'v')
    sleep(.2)
    pyautogui.click('img/pressenter.png')
    clipboard.copy(file[1])
    pyautogui.hotkey('ctrl', 'v')
    sleep(.2)
    pyautogui.click('img/new.png')

print('fin')
