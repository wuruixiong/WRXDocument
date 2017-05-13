import os
import sys
import shutil

originFilesPath = ""
xhdpiFilesPath = ""
xxhdpiFilesPath = ""

	
if __name__=="__main__":
	originFilesPath = sys.argv[1]
	xhdpiFilesPath = originFilesPath + "/drawable-xhdpi"
	xxhdpiFilesPath = originFilesPath + "/drawable-xxhdpi"
	os.makedirs(xhdpiFilesPath)
	os.makedirs(xxhdpiFilesPath)
	
	for root, sub_dirs, files in os.walk(originFilesPath):  
		for special_file in files:  
			if special_file.endswith("@2x.png"): 
				targetFile = originFilesPath+"/"+special_file
				sourceFile = xhdpiFilesPath+"/"+special_file			
				shutil.copy(targetFile, sourceFile)
			elif special_file.endswith("@3x.png"):  
				targetFile = originFilesPath+"/"+special_file
				sourceFile = xxhdpiFilesPath+"/"+special_file
				shutil.copy(targetFile, sourceFile)
	
	for root, sub_dirs, files in os.walk(xhdpiFilesPath):  
		for special_file in files:  
			newname = special_file.replace("@2x.png", ".png")
			os.rename(os.path.join(xhdpiFilesPath,special_file),os.path.join(xhdpiFilesPath, newname))

	for root, sub_dirs, files in os.walk(xxhdpiFilesPath):  
		for special_file in files:  
			newname = special_file.replace("@3x.png", ".png")
			os.rename(os.path.join(xxhdpiFilesPath,special_file),os.path.join(xxhdpiFilesPath, newname))