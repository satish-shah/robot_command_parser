#initial commit
data=[]
data = input("Enter Commands for the Robot [comma separated]");
command_list = data.split(",")

print(command_list)

#now declaring the DIRECTION array

current_pos=0
direction={"F":1j,
       "B":-1j,
       "L":-1,
       "R":1
       }