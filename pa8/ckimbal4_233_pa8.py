#-------------------------------------------------------------------------------
# Author: Craig Kimball 
# Assignment 8
# Date: 11/13/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------


def locateEmergency(hospFile, polFile):
    #retun dictionary
    rtn ={}
    #opens the fist file containing hospital data
    with open(hospFile,'r') as hosp:
        #reads the csv into a list and removes the header
        hosp_list = hosp.readlines()[1:]
        for i in range(len(hosp_list)):
            #changes the hospital list from a string to an array
            hosp_list[i] = hosp_list[i].split(',')
            #zip code
            key = hosp_list[i][7]
            tag = hosp_list[i][0]
            
            #formating the data in the hospital list to match the expected output
            to_add = ['Hospital' if tag == 'HOSP' else 'Urgent Care',hosp_list[i][1].strip(),hosp_list[i][3],hosp_list[i][4].strip()+ ' ' + hosp_list[i][5].strip(),hosp_list[i][8][:len(hosp_list[i][8])-1].strip()]
            #if there is already this key in the dictionary
            if key in rtn:
                #we have to add the new information to the end 
                 rtn[key] = rtn[key] + [to_add]
            else:
                #if theres not already that key we can just set it equal
                rtn[key] = [to_add]
    #opens the police file and does the exact same code as before
    with open(polFile, 'r') as pol:
        pol_list = pol.readlines()[1:]
        for i in range(len(pol_list)):
            pol_list[i] = pol_list[i].split(',')
            
            #zip code in police
            key = pol_list[i][2]
            #formated string for output
            to_add = ['Police Station',pol_list[i][0],pol_list[i][1].strip(),pol_list[i][3][:len(pol_list[i][3])-1].strip()]
            #same logic here as well, adding to the end vs setting equal
            if key in rtn:
                rtn[key] = rtn[key] + [to_add]
            else:
                rtn[key] = [to_add]
    
    #final return statement
    return rtn
# print(locateEmergency('hosp1.csv', 'police1.csv'))
def pollingLocations(precFile, votersFile):
    #list for return
    rtn = []
    #opens the voters file
    with open(votersFile,'r') as vote:
        #reads the data to a list and removes the header
        voters = vote.readlines()[1:]
        #opens the precincts file
        with open(precFile,'r') as prec:
            #reads the data and removes the header in a list
            precincts = prec.readlines()[1:]
            #our voters is our dependent data so we have to iterate through here first
            for v in voters:
                #makes the voters data easier to manipulate when its in an array instead of a string
                voter = v.split(',')
                #precinct of the voter minus the \n
                v_prec = voter[3][:len(voter[3])-1]
                #now we iterate through precints to find the matching one
                for p in precincts:
                    #same concept, makes the data easier to index
                    precinct = p.split(',')
                    #comparing precints of the voter, and the current p
                    if v_prec.upper() == precinct[0]:
                        #adds the string with the correct information to the end of the return array
                        rtn.append('{} can vote at {}\nAddress: {}, VA {}'.format(voter[0],precinct[2],str(precinct[3] +' ' + precinct[4]),precinct[5]))

    #final return statement
    return rtn 
# print(pollingLocations('precincts1.csv', 'voters1.csv'))
def findMyLibrary(libFile, keyword):
    rtn = ''
    #opens the library file
    with open(libFile,'r') as libraryFile:
        #removes the header and stores data
        libraries = libraryFile.readlines()[1:]
        #checks every library in the csv
        for lib in libraries:
            #makes the data easier to subscript
            library = lib.split(',')
            #checks for comparison
            library_name = library[0].lower()
            key = keyword.lower()
            #is keyword in my title
            is_in = False
            #loop to see if the keyword string is in the title at any point
            for i in range(len(library_name)):
                #substringing pulls the starting index i and the length of keyword to compare them
                if library_name[i:i+len(keyword)] == key:
                    #sets a flag to true
                    is_in = True
            #same flag as earlier, I think this code could be consolidated but it works currently
            if is_in:
                #modifies string to output
                rtn += 'Library: {} Website: {}\nAddress: {}, VA {}\n'.format(library[0],library[2],str(library[3]+' ' +library[4] + ' ' +library[5]),library[6].strip('\n'))
    # print(rtn,end='')
    #final return statement   
    return rtn
# print(findMyLibrary('libraries.csv', 'iCk'))
def findPools(poolFile, aZip):
    #initial header for output string
    rtn = '{} pools in zip code ' + str(aZip) + ':\n'
    #used to label each pool in the string
    count= 0
    #list to save pool names to for sorting
    matching = []
    #open file of pools
    with open(poolFile,'r') as pool_file:
        #removes header
        pools = pool_file.readlines()[1:]
        #increments through every pool
        for p in pools:
            # print(pool)
            #gets the zip code of the current pool
            zip = p[len(p)-20:len(p)-15]
            # print(zip)
            #checks if the current pool's zip and target zip are matching
            if zip == str(aZip):
                #adds pool name to list
                matching.append(p.split(',')[0])
    #increments through the sorted list
    matching.sort()
    for p in matching:
        #adds count
        count+=1
        #adds the pool to the string for output
        rtn += '{}){}\n'.format(count,p)
    #final return statement
    return rtn.format(count)
    
# print(findPools('pools.csv', 22030))   
    
    
    
    
    
    
    
    