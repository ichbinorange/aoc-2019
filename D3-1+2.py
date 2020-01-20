with open('D3-data1.txt','r') as data1:
    wire_data1=data1.read()
wire1=wire_data1.split(',')
#print(wire1)
#print(len(wire1),'\n')
inventory1=[]
x_axis1=0
y_axis1=0
#print(x_axis1,y_axis1)
for move in wire1:
    position1=(x_axis1,y_axis1)
    #print(position1)
    #print(move)
    if 'R' in move:
        moveR=int(move[1:])
        #print(moveR)
        for stepR in range(moveR):
            Radd=x_axis1+(stepR+1)
            position1=(Radd,y_axis1)
            inventory1.append(position1)
        x_axis1=x_axis1+moveR
    elif 'L' in move:
        moveL=int(move[1:])
        #print(moveL)
        for stepL in range(moveL):
            Lminus=x_axis1-(stepL+1)
            position1=(Lminus,y_axis1)
            inventory1.append(position1)
        x_axis1=x_axis1-moveL
    elif 'U' in move:
        moveU=int(move[1:])
        #print(moveU)
        for stepU in range(moveU):
            Uadd=y_axis1+(stepU+1)
            position1=(x_axis1,Uadd)
            inventory1.append(position1)
        y_axis1=y_axis1+moveU
    elif 'D' in move:
        moveD=int(move[1:])
        #print(moveD)
        for stepD in range(moveD):
            Dminus=y_axis1-(stepD+1)
            position1=(x_axis1,Dminus)
            inventory1.append(position1)
        y_axis1=y_axis1-moveD
    #print(position1,'\n')
#print(inventory1)

with open('D3-data2.txt','r') as data2:
    wire_data2=data2.read()
wire2=wire_data2.split(',')
    #print(wire2)
    #print(len(wire2),'\n')
inventory2=[]
x_axis2=0
y_axis2=0
#print(x_axis2,y_axis2)
for move in wire2:
    position2=(x_axis2,y_axis2)
    #print(position2)
    #print(move)
    if 'R' in move:
        moveR=int(move[1:])
        #print(moveR)
        for stepR in range(moveR):
            Radd=x_axis2+(stepR+1)
            position2=(Radd,y_axis2)
            inventory2.append(position2)
        x_axis2=x_axis2+moveR
    elif 'L' in move:
        moveL=int(move[1:])
        #print(moveL)
        for stepL in range(moveL):
            Lminus=x_axis2-(stepL+1)
            position2=(Lminus,y_axis2)
            inventory2.append(position2)
        x_axis2=x_axis2-moveL
    elif 'U' in move:
        moveU=int(move[1:])
        #print(moveU)
        for stepU in range(moveU):
            Uadd=y_axis2+(stepU+1)
            position2=(x_axis2,Uadd)
            inventory2.append(position2)
        y_axis2=y_axis2+moveU
    elif 'D' in move:
        moveD=int(move[1:])
        #print(moveD)
        for stepD in range(moveD):
            Dminus=y_axis2-(stepD+1)
            position2=(x_axis2,Dminus)
            inventory2.append(position2)
        y_axis2=y_axis2-moveD
    #print(position2,'\n')
#print(inventory2)


#def coordinate(wire_data):
    #wire=wire_data.split(',')
    #print(wire)
    #print(len(wire),'\n')
    #inventory=[]
    #x_axis=0
    #y_axis=0
    #for move in wire:
    #    position=(x_axis,y_axis)
        #print(position)
        #print(move)
    #    if 'R' in move:
    #        moveR=int(move[1:])
            #print(moveR)
    #        for stepR in range(moveR+1):
    #            Radd=x_axis+stepR
    #            position=(Radd,y_axis)
    #            inventory.append(position)
    #        x_axis=x_axis+moveR
    #    elif 'L' in move:
    #        moveL=int(move[1:])
            #print(moveL)
    #        for stepL in range(moveL):
    #            Lminus=x_axis-(stepL+1)
    #            position=(Lminus,y_axis)
    #            inventory.append(position)
    #        x_axis=x_axis-moveL
    #    elif 'U' in move:
    #        moveU=int(move[1:])
            #print(moveU)
    #        for stepU in range(moveU+1):
    #            Uadd=y_axis+stepU
    #            position=(x_axis,Uadd)
    #            inventory.append(position)
    #        y_axis=y_axis+moveU
    #    elif 'D' in move:
    #        moveD=int(move[1:])
            #print(moveD)
    #        for stepD in range(moveD):
    #            Dminus=y_axis-(stepD+1)
    #            position=(x_axis,Dminus)
    #            inventory.append(position)
    #        y_axis=y_axis-moveD
    #print(position,'\n')
    #print(inventory)
    
#coordinate(wire_data1)
#coordinate(wire_data2)

set1=set(inventory1)
set2=set(inventory2)
intersection=set1.intersection(set2)
#print(intersection)
for item in intersection:
    print('item is',item)
    print('wire1 inventory index',inventory1.index((item))+1)  
    print('wire2 inventory index',inventory2.index((item))+1)  
    # inventory1 & 2 '+1' to add (0,0) as one item in inventory
    print('Sum of wire1+wire2 inventory index (fewest stpes to intersect)',inventory1.index((item))+1+inventory2.index((item))+1) 
    print('\n')

#print(inventory1.index((1,0)))   -->index 1, means first move, first put in inventory
#print(inventory1.index((item)))  -->min index 444
#print(inventory2.index((item)))  -->min index 18817
# (444, 0) is the "lowest steps" intersection

intersection_list=list(intersection)
#print(type(intersection_list))   -->list
#print(len(intersection_list))   -->78

S_distance=[]
for data in intersection_list:
    #print(data)
    distance=abs(int(data[0]))+abs(int(data[1]))
    S_distance.append(distance)
    #print(distance)
print('The smallest distance of intersection',min(S_distance))

#intersection=[]    --->doesn't work
#for coordinate1 in inventory1:
#    if coordinate1 in inventory2:
#        intersection.append(coordinate1)
#print(intersection)



data1.close()
data2.close()