# A fairly easy treasure finder game which allows you to work 
# with cooridinates system in python
# given the number of columns and rows below mark the coordinate
#where the treasure is present

row1 = [" " ," ", " "]
row2 = [" " ," ", " "]
row3 = [" " ," ", " "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
position=input("enter the treasure mark cordinates ")
if int(position[1])> 3 or int(position[0]) > 3:
  print("only allowed numbers are below 3")
else:  
  column= int(position[0])#3
  row=int(position[1])
  map[row-1][column-1] = "*"
  print("treasured marked as *")
  print(f"{row1}\n{row2}\n{row3}\n")
  
# when run below is the o/p
#  [' ', ' ', ' ']
#  [' ', ' ', ' ']
#  [' ', ' ', ' ']

#enter the treasure mark cordinates
#if we enter 33 as the corrdinates the i/p

#enter the treasure mark cordinates 33
#treasured marked as *
#[' ', ' ', ' ']
#[' ', ' ', ' ']
#[' ', ' ', '*']
