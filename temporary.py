# all possibilities for phases set
def phasecreator(nums):
    from itertools import permutations
    phasepossibilities=[]
    for value in permutations(nums, len(nums)):
        phasepossibilities.append(list(value))
    return phasepossibilities

def memory(Intcode,phase,outputs,opcode3,pointer): 
    NewIncode=[]
    # print("Input",Intcode)
    for item in Intcode:
        if int(item)<0:
            NewIncode.append(int(item))
        else:
            if len(str(item))==1:
                new_item='000'+str(item)
                NewIncode.append(new_item)
            elif len(str(item))==2:
                new_item='00'+str(item)
                NewIncode.append(new_item)
            elif len(str(item))==3:
                new_item='0'+str(item)
                NewIncode.append(new_item)
            else:
                NewIncode.append(item)
    NewIncode.append(0) # add one '0' at the end to support the system pointer
    # print("Revised digits",NewIncode, len(NewIncode))
    eachRun={'opcode3':opcode3,'status':0}
    while True:
        instruction=NewIncode[pointer] 
        if int(instruction)!=99:
            # print('Pointer#',pointer)
            parameters1=int(NewIncode[pointer+1])
            parameters2=int(NewIncode[pointer+2]) 
            parameters3=int(NewIncode[pointer+3])
            forH=int(str(instruction)[-3])     
            forT=int(str(instruction)[-4])
            if forH==0 and forT==0:
                if str(instruction)[-1]=='1':
                    add4=int(NewIncode[parameters1])+int(NewIncode[parameters2])
                    NewIncode[parameters3]=int(add4)
                    pointer+=4 
                elif str(instruction)[-1]=='2':
                    multiply4=int(NewIncode[parameters1])*int(NewIncode[parameters2])
                    NewIncode[parameters3]=int(multiply4)
                    pointer+=4
                elif str(instruction)[-1]=='3':
                    if str(instruction)[-1]=='3' and eachRun['opcode3']==0:
                        ACuser=int(phase)
                        eachRun['opcode3']=1
                        # ACuser=input('enter phase: ')
                        parameters1=int(NewIncode[pointer+1])     
                        NewIncode[parameters1]=int(ACuser) 
                        # print('1st 3',NewIncode)  
                        pointer+=2
                    elif str(instruction)[-1]=='3'and eachRun['opcode3']==1:
                        ACuser=int(outputs)
                        eachRun['opcode3']=2
                        # ACuser=input('enter input: ')
                        parameters1=int(NewIncode[pointer+1])     
                        NewIncode[parameters1]=int(ACuser) 
                        # print('2nd 3',NewIncode)
                        pointer+=2
                    elif str(instruction)[-1]=='3'and eachRun['opcode3']==2:
                        pointerlater=pointer
                        amplifier=NewIncode
                        break
                elif str(instruction)[-1]=='4': 
                    # print('opcode4-0 pre-pointer',pointer)
                    printout=int(NewIncode[parameters1])  #forH=0
                    pointer+=2
                    # print('opcode4-0 post-pointer',pointer)
                elif str(instruction)[-1]=='5':
                    if int(NewIncode[parameters1]) is 0:
                        pointer+=3
                    else:
                        pointer+=3
                        pointer=int(NewIncode[parameters2])
                        if pointer>len(Intcode):
                            print('something too big1')
                            break
                elif str(instruction)[-1]=='6':
                    if int(NewIncode[parameters1]) is 0:
                        pointer=int(NewIncode[parameters2])
                        if pointer>len(Intcode):
                            print('something too big5')
                            break
                    else:
                        pointer+=3
                elif str(instruction)[-1]=='7':
                    if int(NewIncode[parameters1])<int(NewIncode[parameters2]):
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4
                elif str(instruction)[-1]=='8':
                    if int(NewIncode[parameters1])==int(NewIncode[parameters2]):
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4 
            elif forH==1 and forT==0:  
                if str(instruction)[-1]=='1':
                    add4=parameters1+int(NewIncode[parameters2])
                    NewIncode[parameters3]=int(add4)
                    pointer+=4 
                elif str(instruction)[-1]=='2':
                    multiply4=parameters1*int(NewIncode[parameters2])
                    NewIncode[parameters3]=int(multiply4)
                    pointer+=4
                elif str(instruction)[-1]=='3':
                    if str(instruction)[-1]=='3' and eachRun['opcode3']==0:
                        ACuser=int(phase)
                        # ACuser=input('enter phase: ')
                        eachRun['opcode3']=1
                        parameters1=int(NewIncode[pointer+1])     
                        NewIncode[parameters1]=int(ACuser)   
                        pointer+=2
                    elif str(instruction)[-1]=='3'and eachRun['opcode3']==1:
                        ACuser=int(outputs)
                        # ACuser=input('enter input: ')
                        eachRun['opcode3']=2
                        parameters1=int(NewIncode[pointer+1])     
                        NewIncode[parameters1]=int(ACuser) 
                        pointer+=2
                    elif str(instruction)[-1]=='3'and eachRun['opcode3']==2:
                        pointerlater=pointer
                        amplifier=NewIncode
                        break
                elif str(instruction)[-1]=='4':
                    # print('opcode4-1 pre-pointer',pointer)
                    printout=int(parameters1)  #forH=1
                    pointer+=2
                    # print('opcode4-1 post-pointer',pointer)
                elif str(instruction)[-1]=='5':
                    if parameters1 is 0:
                        pointer+=3
                    else:
                        pointer=int(NewIncode[parameters2])
                        if pointer>len(Intcode):
                            print('something too big2')
                            break
                elif str(instruction)[-1]=='6':
                    if parameters1 is 0:
                        pointer=int(NewIncode[parameters2])
                        if pointer>len(Intcode):
                            print('something too big6')
                            break
                    else:
                        pointer+=3
                elif str(instruction)[-1]=='7':
                    if parameters1<int(NewIncode[parameters2]):
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4
                elif str(instruction)[-1]=='8':
                    if parameters1==int(NewIncode[parameters2]):
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4 
            elif forH==0 and forT==1:
                if str(instruction)[-1]=='1':
                    add4=int(NewIncode[parameters1])+parameters2
                    NewIncode[parameters3]=int(add4)
                    pointer+=4 
                elif str(instruction)[-1]=='2':
                    multiply4=int(NewIncode[parameters1])*parameters2
                    NewIncode[parameters3]=int(multiply4)
                    pointer+=4
                elif str(instruction)[-1]=='5':
                    if int(NewIncode[parameters1]) is 0:
                        pointer+=3
                    else:
                        pointer=parameters2
                        if pointer>len(Intcode):
                            print('something too big3')
                            break
                elif str(instruction)[-1]=='6':
                    if int(NewIncode[parameters1]) is 0:
                        pointer=parameters2
                        if pointer>len(Intcode):
                            print('something too big7')
                            break
                    else:
                        pointer+=3
                elif str(instruction)[-1]=='7':
                    if int(NewIncode[parameters1])<parameters2:
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4
                elif str(instruction)[-1]=='8':
                    if int(NewIncode[parameters1])==parameters2:
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4 
            elif forH==1 and forT==1:  
                if str(instruction)[-1]=='1':
                    add4=parameters1+parameters2
                    NewIncode[parameters3]=int(add4)
                    pointer+=4 
                elif str(instruction)[-1]=='2':
                    multiply4=parameters1*parameters2
                    NewIncode[parameters3]=int(multiply4)
                    pointer+=4
                elif str(instruction)[-1]=='5':
                    if parameters1 is 0:
                        pointer+=3
                    else:
                        pointer=parameters2
                        if pointer>len(Intcode):
                            print('something too big4')
                            break
                elif str(instruction)[-1]=='6':
                    if parameters1 is 0:
                        pointer=parameters2
                        if pointer>len(Intcode):
                            print('something too big8')
                            break
                    else:
                        pointer+=3
                elif str(instruction)[-1]=='7':
                    if parameters1<parameters2:
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4  
                elif str(instruction)[-1]=='8':
                    if parameters1==parameters2:
                        NewIncode[parameters3]=1
                    else:
                        NewIncode[parameters3]=0
                    pointer+=4   
        elif int(instruction)==99:
            # print('Stop for 99 at',pointer,'\n')
            eachRun['status']=1
            amplifier='stop'
            pointerlater='stop'
            break
        else:
            print('Something went wrong.')
            break
    # print('The pointer becomes',pointerlater)
    # print('One round ended.')
    return amplifier,printout,pointerlater,eachRun['status']


with open('D7-data.txt','r') as intcode:
    int_data=intcode.read()
upgradeAC=list(int_data.split(','))
# print('Length of AC',len(upgradeAC))

phase_list=[5,6,7,8,9]
signals=[]
confirmset=0
for phaseset in phasecreator(phase_list):
    # print("Phase set",phaseset)
    repeat=0
    inputA=[0]
    inputB=[]
    inputC=[]
    inputD=[]
    inputE=[]
    while repeat==0 or repeat==1:
        if repeat==0:
            # print('Repeat#',repeat)
            # print('Input A',inputA[-1])
            amplifierA,outputA,pointerA,statusA=memory(upgradeAC,phaseset[0],inputA[-1],0,0)
            inputB.append(outputA)
            # print(inputB[-1])
            amplifierB,outputB,pointerB,statusB=memory(upgradeAC,phaseset[1],inputB[-1],0,0)
            inputC.append(outputB)
            # print(inputC[-1])
            amplifierC,outputC,pointerC,statusC=memory(upgradeAC,phaseset[2],inputC[-1],0,0)
            inputD.append(outputC)
            # print(inputD[-1])
            amplifierD,outputD,pointerD,statusD=memory(upgradeAC,phaseset[3],inputD[-1],0,0)
            inputE.append(outputD)
            # print(inputE[-1])
            amplifierE,outputE,pointerE,statusE=memory(upgradeAC,phaseset[4],inputE[-1],0,0)
            inputA.append(outputE)
            # print('OutputE',outputE)
            repeat=1
        else:
            # print('Repeat#',repeat)
            # print('Input A',inputA[-1])
            amplifierA1,outputA,pointerA,statusA=memory(amplifierA,phaseset[0],inputA[-1],1,pointerA)
            # print('StatusA changes',statusA)
            inputB.append(outputA)
            # print(inputB[-1])
            amplifierB1,outputB,pointerB,statusB=memory(amplifierB,phaseset[1],inputB[-1],1,pointerB)
            # print('StatusB changes',statusB)
            inputC.append(outputB)
            # print(inputC[-1])
            amplifierC1,outputC,pointerC,statusC=memory(amplifierC,phaseset[2],inputC[-1],1,pointerC)
            # print('StatusC changes',statusC)
            inputD.append(outputC)
            # print(inputD[-1])
            amplifierD1,outputD,pointerD,statusD=memory(amplifierD,phaseset[3],inputD[-1],1,pointerD)
            # print('StatusD changes',statusD)
            inputE.append(outputD)
            # print(inputE[-1])
            amplifierE1,outputE,pointerE,statusE=memory(amplifierE,phaseset[4],inputE[-1],1,pointerE)
            # print('StatusE changes',statusE)
            inputA.append(outputE)
            # print('OutputE',outputE)
            # Re-name the amplifier to trigger the next round
            amplifierA=amplifierA1
            amplifierB=amplifierB1
            amplifierC=amplifierC1
            amplifierD=amplifierD1
            amplifierE=amplifierE1
            if statusA==1 and statusB==1 and statusC==1 and statusD==1 and statusE==1:
                repeat=2
                # print('Repeat#',repeat)
                # print('Final outputE',outputE)
                signals.append(outputE)
                break
            # else:
                # print('Something wrong.')
    confirmset+=1
         
# print('Total number of set',confirmset)
print("Signals collection",signals)
print('The highest signal is',max(signals))

intcode.close()