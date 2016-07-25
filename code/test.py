import os  
  
def scan_files(directory,prefix=None,postfix=None):  
    files_list=[]  
      
    for root, sub_dirs, files in os.walk(directory):  
        for special_file in files:  
            if postfix:  
                if special_file.endswith(postfix):  
                    files_list.append(os.path.join(root,special_file))  
            elif prefix:  
                if special_file.startswith(prefix):  
                    files_list.append(os.path.join(root,special_file))  
            else:  
                files_list.append(os.path.join(root,special_file))

	for i in range(len(files_list)):
		print(files_list[i])			
		print os.path.os.path.basename(files_list[i])
		print("\n")
		
							
    return files_list  
	
	
if __name__=="__main__":  
	scan_files("../dango/res/drawable-xhdpi",None,None)
	

