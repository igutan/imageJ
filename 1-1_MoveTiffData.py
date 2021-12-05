import os, shutil, glob
from ij.io import DirectoryChooser
from ij import IJ

dcS = DirectoryChooser("Choose a folder for raw files")  
sourceDir = dcS.getDirectory()  

dcT = DirectoryChooser("Choose a folder to copy to")
targetDir = dcT.getDirectory()

tiff_files = glob.iglob(os.path.join(sourceDir, "*.tif"))

for filename in tiff_files:		
		if os.path.isfile(filename):
			shutil.copy(filename, targetDir)

IJ.log("finish!")
