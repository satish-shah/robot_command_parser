#task is to write a CLI application to parse commands and display the result.
import re
import sys

#since space between the commands is not requird eg 'L 1'
#implemented this function to avoid the space provided by user eg 'L1'
#validating the input command string
def checkInput(data):
    try:
        data = data.strip()
        if(re.search("^[FBLRfblr]",data[0]) and int(data[1:])):
            return ([data[0],data[1:].strip()])
        else:
            raise ValueError(data)
            raise IndexError(data)
    except ValueError:
        print("Invalid input ")
        sys.exit(0) 
    except IndexError:
        print("Invalid error ")
        sys.exit(0)


items = []
command_list = input("Enter the commands for the Robot ")
command_list = list(command_list.strip().split(","))

#print(command_list)

for data in command_list:
    items.append(checkInput(data))

#now declaring the DIRECTION array
#we have also given the vector for the move


direction={"F":1,
       "B":-1,
       "L":-1,
       "R":1
       }

current_pos=0

#we are determining the moves robot have made
# robot on valid moves and the magnitude is calculated

for item in items:
    print(item, " item")
    move = item[0].upper()
    value = item[1]
    current_pos += direction[move]*int(value)

#Getting the  distance     
#Also checking wheather the value has negative magnitude 
# using absolute function and round function 

print('Distance traveled by the robot:', round(abs(current_pos)))
