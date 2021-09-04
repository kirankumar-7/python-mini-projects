print("Welcome to the Treasure map: ")

row1=[" "," "," "]                                          # to store multiple datas create a list 
row2=[" "," "," "]
row3=[" "," "," "]

#nested list
map=[row1,row2,row3]                                        #indices are 0,1,2

print(f"{row1}\n{row2}\n{row3}\n")
position=input("Where do you want to put the treasure? : ")            
   
#vertical-columns
#horizontal-rows
horizontal=int(position[0])                         #for example if we give (19) the indices 1 is '0' and 9 is '1' 
vertical=int(position[1])                            #if we pass 3 in vertical without(vertical-1) then get error since index starts from 0,1,2

map[horizontal-1][vertical-1]= "X"
print(f"{row1}\n{row2}\n{row3}\n")
