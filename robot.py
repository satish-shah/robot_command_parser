#task is to write a CLI application to parse commands and display the result.




data=[]
data = input("Enter Commands for the Robot [comma separated]");
command_list = data.split(",")

#print(command_list)

#now declaring the DIRECTION array
#we have also given the vector for the move

current_pos=0
direction={"F":1j,
       "B":-1j,
       "L":-1,
       "R":1
       }

#we are determining the moves robot have made
# robot on valid moves and the magnitude is calculated
for command in command_list:
    parts=split(command)    
    move=parts[0]
    value=parts[1]
   
    current_pos += direction[move]*int(value)

#Getting the  distance     
#Also checking wheather the value has negative magnitude 
# using absolute function and round function 

print('Distance traveled by the robot:', round(abs(current_pos)))
