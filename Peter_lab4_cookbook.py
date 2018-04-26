# Week 4 Code book. 
# Topics:  Paths and filenames, 
#          Try-except-else blocks, 
#          reading and writing simple text files, 
#          finding files on the file system. 



# Define a function to read a file and display what it finds
# there. This uses the "open()" function, one of the built-in
# functions within Python.  However, first we need to build 
# a function that checks to make sure that the user passes legitimate
# path and file

def concatenate_path_and_filename(path, filename):
    
    #Input:  path and filename tuple of strings
    #Output:  tuple of (indicator, fullpathname)
    #    where:  indicator is a boolean telling whether the proposed
    #           name is valid
    #           fullpathname is the concatenated path and filename
    
    
    # When working with file I/O, it's important to test early and
    # and often.  Is the filename right? Does it exist? Are the
    # delimiters right for the full path?  We'll be working with
    # files a lot, so we need to set good habits now. 
    
      
    #First, we need to make sure that the path actually ends with 
    # the current operating system's path delimiter.  On Windows
    # machines, it's the \ slash, and on Macs and Unix/Linux it's
    # a / slash. Fortunately, the "os" module keeps track of this 
    # for us! 
    
    import os
    
    # test if path ends appropriately.  Of course, if the 
    # user passes something weird (like a number) for the path
    # we need to handle this gracefully
    
    try: 
        if path[-1] != os.path.sep: #if the user did not put a delimiter at the end, then we try adding it
            try: 
                path=path+os.path.sep   #use the operating system's separator
            except: 
                #if that throws an exception, then the path must be an inappropriate type
                print("Error concatenate_path_and_filename:  the path appears to not be a string type")
                return False, None  # return a tuple that will be caught by caller
    except:
        #if we get here, that means that path[-1] didn't even work
        #   So, we have to alert the user of that too
        print("Error concatenate_path_and_filename:  path appears to be non-indexable type")
        return False, None

    # whew.  So, at this point we hope we have a path variable that 
    #  appears to be promising. We still don't know if the filename
    #  portion is okay. 
    
    if type(filename) != str:
        print("Error concatenate_path_and_filename:  filename must be a string")
        return False, None
    
    #Now we hope we can glue them together into a full pathname
    print("Putting together path and filename")
    
    fn = path + filename
    
    #Now, we can finally check to see if this file really exists
    # What if this file does not exist?  How do we check?
    # We can again use the "os" module -- check the existence of a file. 
    # (alert:  we'll run into a similar functionality later in ArcPy)
    
    if os.path.isfile(fn):  #os.path.isfile() returns True if fn really exists
        return True, fn # return "true" and the filename
    else: 
        print("Error in concatenate_path_and_filename: File does not exist")        
        return False, None    #if the file doesn't exist, return false.
     

  
# That was painful.  Is there an easier way? 
#  Yes!  At least some of this can be handled by a built-in os function 

def check_filename(path, filename):
    
    #To be safe, we need to import the os namespace here locally
    
    import os
    
    #here, we use the os.path.join module to take away having to deal with the
    #   delimiter ourselves. However, if we pass nonsense to the os., it will
    #   still crash.   So we have to embed it in a try/except block
    
    try:
        #this will handle the delimiter for us.          
        fn = os.path.join(path, filename) 
        
        
    except IOError as e:
        print("Error in check filename:  Problem with either the path or the filename")        
        print("I/O error {0}: {1}".format(e.errno, e.strerror))        
        return False, None
    except:
        print("Error in check filename:  Undetermined.")
        
        return False, None
        
    
    print("No problem with the path and filename concatenation")
    
    #If we get here, then presumably we have a filename.  Now, let's 
    #  see if it's actually an existing file.  
    
    if os.path.isfile(fn):#os.path.isfile() returns True if fn really exists
        return True, fn # return "true" and the filename
    else: 
        print("Error in check filename: The file does not exist")
        return False, None    #if the file doesn't exist, return false.
    
    # This was much simpler, but the error catching in the first step was a bit
    #  less clear.  We could be more specific in the try/except block by 
    #  setting up multiple except blocks that handle different exceptions



#Define a function that reads a file and writes out a new file with 
# a simple header and footer based on the date and time stamp.  


def headfootfile(path,filename):    #---------------------------------------------Name error 'file' should be 'filename"
 
    test = check_filename(path, filename)

    
    if not(test[0]):    # if the path/filename doesn't test out, get out
        print("Error:  headfootfile cannot operate on the path, file you gave")
        print path
        print filename
        return False, None #return the bad news. 
        
    fn = test[1]    
    
    file_in_object = open(fn)    
        
   
    outfn = fn[:-4]+'_headfoot'+fn[-4:] #Interpose the headfoot! 

    try: 
        file_out_object = open(outfn, 'w')  #NOTE the 'w' syntax.  
        #Again, check out the Python.org site to see that this means 
        # "open the file for writing"
    except:
    
        print("Error:  problem writing the file:")
        print(outfn)    #show the user what was tried


        file_in_object.close()  #closes the file we opened earlier
        
        #Now we can return.         
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

    for line in file_in_object:
        try:
            file_out_object.write(line) #just write the line
        except:
            print("Error:  Error writing the file.")
            #Clean both up by closing
            
            file_in_object.close()
            file_out_object.close()
            return False, None            
         
    
    try:
        message = "\nA parting thought:  Have a great day coding!" 
        file_out_object.write(message) 
        
    except:
        print("Error:  Error writing the file.")
        #Clean both up by closing
        file_in_object.close()
        file_out_object.close()
        return False, None 

    
    print("Successfully wrote the file")
    print(outfn)    
    
    file_in_object.close()
    file_out_object.close()

    return True, outfn


def find_files(path, searchterm):

    import re
    
    import os
    
    try:
        files = os.listdir(path)   #try listing the files in the directory
        
    except:  #bring in the exception
        
        print("Error in find_files: Path did not appear to work")
        print("The path used was:")
        print path
        return False, None
    

    
    matchlist = []  # set up an empty list to keep track of things
    
    for file in files:           
    
        if (re.match(searchterm, file)):
            matchlist.append(file)

    if len(matchlist) != 0:  return matchlist
    else:  return False, None

def check_path(path):
    import os
    if path[-1] == "\\":
        path[:-1]
    if os.path.isdir(path):
        print('No problem with the path.')
        return True, path
    else:
        return("Error: The path does not exist or worng format")
        
    
