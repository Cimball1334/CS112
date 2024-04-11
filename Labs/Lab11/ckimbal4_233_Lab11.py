#CS 112 _ 233 Python lab 11
#Author Craig Kimball
#Date 11/9/2021 11:30AM 

def calc_equations(input,output):
    #setup for output text to file
    write = 'Equations\n\n'
    with open(input,'r') as file:
        #grabs each line but ommits the first 2
        text = file.readlines()[2:] 
        
        
        #removes the '\n' from each line
        for i in range(len(text)):
            if(text[i][-1] == '\n'):
                text[i] = text[i][:len(text[i])-1]
            
    
        
        for i in range(len(text)):
            #makes it easier to grab larger integers that are more than a single number ex. 12
            slim = text[i].split()

            #checks the opperand and does the correct math, concatinates things from strings to ints back to strings to do math
            if(slim[1] == '+'):
                write += text[i] + ' = ' + str(int(slim[0]) + int(slim[-1])) + '\n'
            elif(slim[1] == '-'):
                write += text[i] + ' = ' + str(int(slim[0]) - int(slim[-1])) + '\n'
            elif(slim[1] == '*'):
                write += text[i] + ' = ' + str(int(slim[0]) * int(slim[-1])) + '\n'
            else:
                write += text[i] + ' = ' + str(int(slim[0]) / int(slim[-1])) + '\n'
            #close file
            file.close()
            
    with open(output,'w') as file:
        #removes the last '\n' that is added to clean up the file
        file.write(write[:len(write)-1])
        
        #close file
        file.close
        
calc_equations('fileInput.txt','fileOutput.txt')