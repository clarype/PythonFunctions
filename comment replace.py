''' this function will take a python and change the comments'''
import Peter_lab4_cookbook as papa
def PyComChan(path, filename):   
    test = papa.check_filename(path, filename)
    if not(test[0]):    # if the path/filename doesn't test out, get out
        print("Error:  headfootfile cannot operate on the path, file you gave")
        print path
        print filename
        return False, None #return the bad news.         
    fn = test[1]       
    file_in_object = open(fn)             
    outfn = path + '/' + filename[:-4] + '_Comment_chage' + filename[-4:] 
    try: 
        file_out_object = open(outfn, 'w')       
    except:    
        print("Error:  problem writing the file:")
        print(outfn)  
        file_in_object.close()                   
        return False, None   
    for line in file_in_object:
        try:
            j = line.find('#')  
            H = line.replace(line[j:], '\n')         
            file_out_object.write(H) #just write the line
        except:
            print("Error:  Error writing the file.")
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
a = raw_input('Path name ')
b = raw_input('file name ')
print PyComChan(a, b)

