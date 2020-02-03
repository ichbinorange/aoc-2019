import cProfile
import numpy 

def memory(Intcode):
    upgradeAC=Intcode
    instruction_pointer=0
    relative_base=0
    # for Emergency hull painting robot
    Xcoordinate=0
    Ycoordinate=0
    mapCollect={}  # Ex: mapCollect={(X,Y):[color]}
    step=-1
    facingDirection='up'
    while True:
        instruction=upgradeAC[instruction_pointer]
        parameters1=int(upgradeAC[instruction_pointer+1])
        parameters2=int(upgradeAC[instruction_pointer+2]) 
        parameters3=int(upgradeAC[instruction_pointer+3]) 
        if parameters1>100000000 or parameters2>100000000 or parameters3>100000000:
            modeH={'0':0,'1':parameters1,'2':0}
            modeT={'0':0,'1':parameters2,'2':0}
            forH=modeH[str(instruction)[-3]]    
            forT=modeT[str(instruction)[-4]]
        else:
            modeH={'0':int(upgradeAC[parameters1]),'1':parameters1,'2':int(upgradeAC[parameters1+relative_base])}
            modeT={'0':int(upgradeAC[parameters2]),'1':parameters2,'2':int(upgradeAC[parameters2+relative_base])}
            forH=modeH[str(instruction)[-3]]    
            forT=modeT[str(instruction)[-4]]
        if str(instruction)[3:]=='01':
            add4=forH+forT
            if str(instruction)[0]=='0':
                upgradeAC[parameters3]=int(add4)
            elif str(instruction)[0]=='2':
                upgradeAC[parameters3+relative_base]=int(add4)
            instruction_pointer+=4 
        elif str(instruction)[3:]=='02':
            multiply4=forH*forT
            if str(instruction)[0]=='0':
                upgradeAC[parameters3]=int(multiply4)
            elif str(instruction)[0]=='2':
                upgradeAC[parameters3+relative_base]=int(multiply4)
            instruction_pointer+=4
        elif str(instruction)[3:]=='03':
            # print('(X,Y) = (',Xcoordinate,',',Ycoordinate,')')
            step+=1
            opcode4output=0   # to re-collect opcode 4 output twice (color and direction) 
            if step==0: # initial input must be white(1)
                # print('Step0:',step)
                ACuser=1
                # print('Input:',ACuser)
                if str(instruction)[-3]=='0':
                    upgradeAC[parameters1]=int(ACuser) 
                elif str(instruction)[-3]=='2':
                    upgradeAC[parameters1+relative_base]=int(ACuser) 
            elif step!=0:
                # print('Stpe:',step)
                if mapCollect.get((Xcoordinate,Ycoordinate)) == None:  
                    ACuser=0
                    # print('Input color',ACuser)
                    if str(instruction)[-3]=='0':
                        upgradeAC[parameters1]=int(ACuser) 
                    elif str(instruction)[-3]=='2':
                        upgradeAC[parameters1+relative_base]=int(ACuser) 
                else:
                    ACuser=mapCollect[(Xcoordinate,Ycoordinate)]
                    # print('Input color(already existed)',ACuser)
                    if str(instruction)[-3]=='0':
                        upgradeAC[parameters1]=int(ACuser) 
                    elif str(instruction)[-3]=='2':
                        upgradeAC[parameters1+relative_base]=int(ACuser) 
            instruction_pointer+=2
        elif str(instruction)[3:]=='04': 
            opcode4output+=1
            if opcode4output==1:
                mapCollect[(Xcoordinate,Ycoordinate)]=forH 
                # print('opcode 4H-color',forH) 
            elif opcode4output==2:
                # print('opcode 4H-direction',forH)
                if (step % 2) == 0:   # even step: 0,2,4  
                    if facingDirection=='up':    
                        if forH==0:
                            Xcoordinate-=1
                            facingDirection='left'
                        elif forH==1:
                            Xcoordinate+=1
                            facingDirection='right'
                    elif facingDirection=='down':    
                        if forH==0:
                            Xcoordinate+=1
                            facingDirection='right'
                        elif forH==1:
                            Xcoordinate-=1
                            facingDirection='left'
                else:   # odd step: 1,3,5
                    if facingDirection=='left':   
                        if forH==0:
                            Ycoordinate-=1
                            facingDirection='down'
                        elif forH==1:
                            Ycoordinate+=1
                            facingDirection='up'
                    elif facingDirection=='right':   
                        if forH==0:
                            Ycoordinate+=1
                            facingDirection='up'
                        elif forH==1:
                            Ycoordinate-=1
                            facingDirection='down'
            else:
                print('something too big4-2')
                break
            instruction_pointer+=2
        elif str(instruction)[3:]=='05':
            if forH is 0:
                instruction_pointer+=3
            else:
                instruction_pointer=forT
                if instruction_pointer>len(Intcode):
                    print('something too big5')
                    break
        elif str(instruction)[3:]=='06':
            if forH is 0:
                instruction_pointer=forT
                if instruction_pointer>len(Intcode):
                    print('something too big6')
                    break
            else:
                instruction_pointer+=3
        elif str(instruction)[3:]=='07':
            if forH<forT:
                if str(instruction)[0]=='0':
                    upgradeAC[parameters3]=1
                elif str(instruction)[0]=='2':
                    upgradeAC[parameters3+relative_base]=1
            else:
                if str(instruction)[0]=='0':
                    upgradeAC[parameters3]=0
                elif str(instruction)[0]=='2':
                    upgradeAC[parameters3+relative_base]=0
            instruction_pointer+=4
        elif str(instruction)[3:]=='08':
            if forH==forT:
                if str(instruction)[0]=='0':
                    upgradeAC[parameters3]=1
                elif str(instruction)[0]=='2':
                    upgradeAC[parameters3+relative_base]=1
            else:
                if str(instruction)[0]=='0':
                    upgradeAC[parameters3]=0
                elif str(instruction)[0]=='2':
                    upgradeAC[parameters3+relative_base]=0
            instruction_pointer+=4 
        elif str(instruction)[3:]=='09':
            relative_base=forH+relative_base
            instruction_pointer+=2
        elif str(instruction)[3:]=='99':
            print('Stop for 99 at',instruction_pointer,'\n')
            break
        else:
            print('Something went wrong.')
            break
    return mapCollect

with open('D11-data.txt','r') as intcode:
    int_data=intcode.read()

# def start():
upgradeAC=list(int_data.split(','))

def addZeroSpots(oldAC):
    numerise = list(map(int, oldAC))
    # print(max(numerise))  -->988648461076
    outputAC=[]
    for item in numerise:
        new_item='%05d' % item  # build 5-digits item
        outputAC.append(new_item)  # str in the list
    # print(len(outputAC))
    outputAC=outputAC+['00000']*98864846
    # print(len(outputAC))
    return outputAC

final=memory(addZeroSpots(upgradeAC))
# print(len(final))

dictlist=[]
for key, value in final.items():
    if value==1:
        # temp = [key,value]
        temp = key
        dictlist.append(temp)
print(dictlist)
# print(len(dictlist)) -->96

# cProfile.run("start()")
        