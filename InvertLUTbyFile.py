import os
from ij.io import DirectoryChooser
from ij import IJ, ImagePlus, Prefs
from ij.io import FileSaver

dcS = DirectoryChooser("Choose a folder to read from")  
sourceDir = dcS.getDirectory()  

dcT = DirectoryChooser("Choose a folder to save to")
targetDir = dcT.getDirectory()

def invertLUT(sourceDir, filename):
 	imp = IJ.openImage(os.path.join(sourceDir,filename))
 	IJ.run(imp, "8-bit", "")
	IJ.run(imp, "Invert LUT", "")
	IJ.run(imp, "Brightness/Contrast...", "")
	IJ.run(imp, "Enhance Contrast", "saturated=0.05")
	IJ.run(imp, "Apply LUT", "")

	targetpath = os.path.join(targetDir, os.path.basename(filename))	
	if not targetpath.endswith(".tif"):
     		targetpath += ".tif"  
    	IJ.saveAsTiff(imp, targetpath) 

def loadProcessAndSave(sourcepath, fn):  
	for filename in os.listdir(sourceDir):
    	 if filename.endswith(".tif"):
    		invertLUT(sourceDir, filename) 

loadProcessAndSave(sourceDir, invertLUT)
IJ.run("Close", "2_InvertLUTbyFile.py")
IJ.log("finish!")
