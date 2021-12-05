import os
from ij.io import DirectoryChooser
from ij import IJ, ImagePlus, Prefs
from ij.io import FileSaver
from ij.plugin.frame import RoiManager

dcS = DirectoryChooser("Choose a folder to read from")  
sourceDir = dcS.getDirectory()  

dcT = DirectoryChooser("Choose a folder to save to")
targetDir = dcT.getDirectory()

def AreaAnalyzer(sourceDir, filename):
 	imp = IJ.openImage(os.path.join(sourceDir,filename))
 	IJ.run(imp, "Smooth", "")
	IJ.run(imp, "Convert to Mask", "")
	IJ.run(imp, "Measure", "")

	IJ.selectWindow("Results")
	resultpath = os.path.join(targetDir, os.path.basename(filename))
	newresultpath = resultpath.replace(".tif", "_result.csv")	 
    	IJ.saveAs("Results", newresultpath)
	
	targetpath = os.path.join(targetDir, os.path.basename(filename))
	newtargetpath = targetpath.replace(".tif", "_result")
	if not newtargetpath.endswith(".tif"):
     		newtargetpath += ".tif"  
     	IJ.saveAsTiff(imp, newtargetpath)
     	IJ.run("Close", "imp")

def loadProcessAndSave(sourcepath, fn):  
	for filename in os.listdir(sourceDir):
    	 if filename.endswith(".tif"):
    		AreaAnalyzer(sourceDir, filename) 

loadProcessAndSave(sourceDir, AreaAnalyzer)
IJ.log("finish!")
