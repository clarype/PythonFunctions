

import Peter_lab4_cookbook as Pcbk4

a = raw_input('Enter a path to a folder with no spaces. examples. for Mac something like this /Users/katie/Downloads/lab44 or for Windows C:\\\Users\\\clarype\\\Desktop\\\New folder   ')
#


def headfootfile(path,filename):   
    test = Pcbk4.check_filename(path, filename)   #returns a tuple. element 0 tells us
    
    if not(test[0]):    # if the path/filename doesn't test out, get out
        print("Error:  headfootfile cannot operate on the path, file you gave")
        print path
        print filename
        return False, None #return the bad news. 
        
    fn = test[1]    #assign the full path/filename to the variable fn 
    
    file_in_object = open(fn)    #fn becomes the object we operate on 
        
    outfn = fn[:-4]+'_headfoot'+fn[-4:] #Interpose the headfoot! 
    try: 
        file_out_object = open(outfn, 'w')  #NOTE the 'w' syntax.  
    except:
        # A problem!  Report and bail
        print("Error:  problem writing the file:")
        print(outfn)    #show the user what was tried

        file_in_object.close()  #closes the file we opened earlier
                 
        return False, None   #return empty
    
    from datetime import datetime  
    timestamp = datetime.now()
    
    header = "FileWritten on "+str(timestamp.day)+"_"+str(timestamp.month)+"_"+str(timestamp.year)+" at "+ str(timestamp.hour)+"_"+str(timestamp.minute)+".\n"     

    try: 
        file_out_object.write(header)
    except:
        print("Error:  I could open the file, but not write to it.")
        #Clean both up by closing
        file_in_object.close()
        file_out_object.close()
        return False, None
#-----------------------------------problem 4------------------------------------            
    count = 0
    for line in file_in_object:
        try:
            count +=1
            file_out_object.write(str(count)+"\t" + "Hi, we are indented.  :)" + line)
#-----------------------------------------End of Problem-----------------------------------------
        except:
            print("Error:  Error writing the file.")
            
            file_in_object.close()
            file_out_object.close()
            return False, None            
    
    try:
        message = "\nA parting thought:  Have a great day coding!" #again, note the 
        #        \n as a carriage return to add a blank line. 
        
        file_out_object.write(message) #just write the line
    except:
        print("Error:  Error writing the file.")
    
        file_in_object.close()
        file_out_object.close()
        return False, None 
    
    print("Successfully wrote the file")
    print(outfn)    #remember -- this was the filename we constructed
    
    file_in_object.close()
    file_out_object.close()

    return True, outfn




#-------------------------Problem 5-------------------------------


import Peter_lab4_cookbook as pckb # imports codebook 

def folder_dir(path):   # function 
    import os   
    p = pckb.check_path(path) #checks file path     
    if p[0] == True:    #checks to make sure that the imported tulpe from the check_path function is true 
        filelist = []     # creates an empty list for each file in the folder 
        formt = raw_input('Enter a file type. examples .txt, .shp, .pdf, etc.    ')  # user input for type of file to be tested         
        for file in os.listdir(path):  # scan directory for files.
            if file.endswith(formt):    # scan directroy for a type of file 
                filelist.append(file)  # adds found type of file to the empty list 
        if len(filelist) >  0:      # tells users if a file of a type was found 
            print "You have at least one file"
        else:
            return 'There are no files of that format.  '             
        pathlist = []  # creates a empty list for each file path to be used in os.stat().st_size functions
        sizeA = raw_input('Enter the upper end of the file size you are looking for.  example 50000   ')  # user input to help find a certain sized file 
        sizeB = raw_input('Enter the lower end of the file size you are looking for.  example 1   ') # user input to help find a certain sized file
        for i in filelist:     # loops througth filelist to join file name and path    
            dfg = path + "/" + i   # ''
            pathlist.append(dfg)  # adds joined path and file name to empty list 
        for o in pathlist: # loops througth pathlist for file size condistions
            if os.stat(o).st_size < int(sizeA) and os.stat(o).st_size > int(sizeB):    # checks file size with upper and lower condistions       
                tt = open(path + '\WEEE.txt', 'w')  # creates a new doc to write on 
                count = 0 # this is to list each file on the doc 
                for n in range(len(pathlist)): # loop writes each file on to doc 
                    count += 1   # numbering each file 
                    tt.write(str(count) + '. ' + pathlist[n] + ' has a size less then {0} but higher than {1}.'.format(sizeA, sizeB) + '\n')  # message to write on doc                  
                tt.close()         # closes file 
                print "A file meets these qulifcations! And it is printed to a text called WEEE in the folder at the end of the path. "
            else:
                print "A file does not meet these qualifcations"            
    else:
        return "Check your file path format."
#print headfootfile(a, b)
print folder_dir(a)

#------------------------------------------------------------------------------------------------------------------------
