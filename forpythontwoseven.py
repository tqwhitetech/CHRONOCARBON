import os
from shutil import copy
import Tkinter as Tk
import tkFileDialog
from tkFileDialog import askdirectory

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
    if os.path.isdur(fullPath):
      allFiles = allFiles + getListOfFiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles

def main():
  # Get user input for folder to scan
  dirName = tkFileDialog.askdirectory(title="Select Folder to Scan")
  listofFiles = getListOfFiles(dirName)
  
  # Have user specify a folder for output
  destDir = tkFileDialog.askdirectory(title="Select Destination Folder")
  
  # Get list of all files
  listofFiles=list()
  for (dirpath, dirname, filenames) in os.walk(dirName):
    listofFiles += [os.path.join(dirpath, file) for file in filenames]
    
  # Check file size
  for elem in listofFiles:
    size = os.path.getsize(elem)
    if size > *INSERT BYTES HERE* and elem.ends with (*INSERT EXTENSION*):
      print("Copying: " + elem)
      filestocopy.append(elem)
      
  # Copy files to folder
  
  for large in filestocopy
    try:
      copy(large, destDir)
    except OSError:
      pass
      
  filecount = len(filestocopy)
  print("Copied " + str(filecount) + " files to the destination")
  
if __name__ == '__main__':
  main()
