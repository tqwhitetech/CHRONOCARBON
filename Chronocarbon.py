import os
from shutil import copy
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askdirectory

# Variables
subfolders = []
files = []
filestocopy = []


# Functions


def getListOfFiles(dirName):
    listofFiles = os.listdir(dirName)
    allFiles = list()
    for entry in listofFiles:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


def main():

    # Get user input on the folder with the data to be copied
    dirName = filedialog.askdirectory(title="Select Folder to Scan")
    listofFiles = getListOfFiles(dirName)

    # Have user specify a new folder for the data
    destDir = filedialog.askdirectory(title="Select Destination Folder")

    # Get list of all files (some sort of recursion error is happening here
    listofFiles=list()
    for (dirpath, dirnames, filenames) in os.walk(dirName):
        listofFiles += [os.path.join(dirpath, file) for file in filenames]
       

    # Check file size
    for elem in listofFiles:
        size = os.path.getsize(elem)
        if size > 1000 and elem.endswith('.txt'):
            print("Copying " + elem)
            filestocopy.append(elem)


    # Copy the files to the folder
    for large in filestocopy:
        try:
            copy(large, destDir)
        except OSError:
            pass

if __name__ == '__main__':
    main()