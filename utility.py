from random import randint
import os

###########################################################
# function to get user input regardless of python version #
###########################################################
def randomLERS(count):
    file = open("sample1.lers", "w")
    file.write("< a a a a x x d d a a x >\n[ height weight noise price ]\n! comment\n")
    for i in range(0,count):
        attributes = [randint(10,20)+float(randint(0,99))/100, randint(20,30)+float(randint(0,99))/100, randint(30, 40)+float(randint(0,99))/100]
        
        temp = randint(0, 4)
        if temp == 0:
            decision = "low"
        elif temp == 1:
            decision = "med"
        elif temp == 2:
            decision = "very_low"
        elif temp == 3:
            decision = "very_high"
        else:
            decision = "high"
        file.write(str(attributes[0]) + " " + str(attributes[1]) + " " + str(attributes[2]) + " " + decision + "\n")
    file.close()


#####################################################
# resolve version issues between python 2.x and 3.x #
#####################################################
def get_user_input(message):
    try:
        # python 2.x function
        user_input = raw_input(message)
    except:
        # python 3.x function
        user_input = input(message)
    return user_input

###############################################################################
# function to get filename from user (if none specified) and then open a file #
###############################################################################
def openfile(user_input=None):
    
    if user_input == None:
        # Get filename from user
        user_input = input("Filename?\n> ")

    
    while True:
        try:
            # try to open file 
            file = open(user_input, "rU")           
            break
        except:
            # if file doesn't open, re-prompt for filename and try to open again
            print("\nerror: File not found\n")
            user_input = get_user_input("Filename?\n> ")
            
    return file


#######################
# write Table to file #
#######################
def table2file(entries,attributes,cutpoints,decision,datafilename="output.data.txt",intfilename="output.int.txt"):
    d = 1
    
    diag("\nWriting table and cutput info to disk",d)
    datafile = open(datafilename,'w')
    
    # Write attribute identifiers
    datafile.write("[ ")
    for attr in attributes:
        datafile.write(str(attr) + " ")
    datafile.write(str(decision)+" ]")
    
    # Write each entry
    for entry in [entries[i] for i in entries]:
        datafile.write("\n")
        for val in [entry.A[i] for i in entry.A]:
            datafile.write(" " + str(val))
        datafile.write("\t" + str(entry.D))
        
    datafile.close()
    
    
    intfile = open(intfilename,'w')
    
    for i in range(0,len(attributes)):
        intfile.write("cutpoints for " + str(attributes[i]) + ":\n")
        for point in cutpoints[i][0:-1]:
            intfile.write(str(point) + ", ")
        intfile.write(str(cutpoints[i][-1]) + "\n")
    
    
    intfile.close()
    
    return (datafilename,intfilename)


#######################
# diagnostic printing #
#######################
def diag(string,diagnostics=0):
    if diagnostics != 0:
        print(string)
        
       


#############################
# file scanning / selection #
#############################
def selectFile():
    choice = get_user_input("\n\nWould you like to: \n0. Select from a list of files\n1. Enter a filename manually?\n> ")
    
    if choice == "0":
        files = [""]
        i = 1
        print("\nPlease select from files found:")
        for filename in os.listdir("./"):
            if filename.endswith(".txt") or filename.endswith(".lers"):
                files.append(filename)
                print(str(i).rjust(3," ") + ". " + str(filename))
                i+=1
        
        while True:
            choice = get_user_input("> ")
            
            if choice.isdigit():
                choice = int(choice)
                if (choice > i-1) or (choice < 1):
                    print("\nerror: Selection out of bounds, please select a value between 1 and " + str(i-1))
                else: 
                    return files[choice]
            else:
                print("\nerror: Invalid selection, please try again")
    elif choice == "1":
        return openfile()
    else:
        print("\nerror: Invalid selection, defaulting to manual entry\n")
        return openfile()


