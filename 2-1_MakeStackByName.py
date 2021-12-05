import os
import re
from ij.io import DirectoryChooser
from ij import IJ, ImagePlus, Prefs
from ij.io import FileSaver

dcS = DirectoryChooser("Choose a folder to read from")  
sourceDir = dcS.getDirectory()  

dcT = DirectoryChooser("Choose a folder to save to")
targetDir = dcT.getDirectory()

def MakeStack(sourceDir, file_i):
 		path_maker = lambda file_i: os.path.join(sourceDir, file_i)
		image_list = map(path_maker, file_i)
		print image_list

		k = 0
		while k < len(image_list):
			imp = IJ.open(image_list[k])
			k += 1
		
		IJ.run("Images to Stack", "method=[Copy (center)] name=Stack")
	
		targetpath = os.path.join(targetDir, os.path.commonprefix(file_i))	
		if not targetpath.endswith(".tif"):
     			targetpath += ".tif"  
    		IJ.saveAsTiff(imp, targetpath)
    		IJ.run("Close", imp) 

def loadProcessAndSave(sourcepath, fn):
	list = os.listdir(sourceDir)
	number_files = len(list)
	number_slides = number_files / 4 #enter series number

	i = 1
	while i <= number_slides:
		file_i = []
		pattern = "^" + str(i) + " -.+.tif$"
		for filename in list:
			if re.search(pattern, filename):
				file_i.append(filename)
		MakeStack(sourceDir, file_i) 
		i += 1

loadProcessAndSave(sourceDir, MakeStack)
IJ.log("finish!")
