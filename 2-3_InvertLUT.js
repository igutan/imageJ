importClass(Packages.ij.IJ);
importClass(Packages.ij.ImagePlus);
importClass(Packages.ij.io.FileSaver);

imp = IJ.getImage();

// change image to 8-bit and invert color
IJ.run("8-bit");
IJ.run("Invert LUT");
IJ.run("Brightness/Contrast...");
IJ.run("Enhance Contrast", "saturated=0.05");
IJ.run("Apply LUT");
IJ.run("Close");

// save image
IJ.saveAsTiff(imp,"");
IJ.run("Close");