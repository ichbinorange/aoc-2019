def memory(Intcode,phase,outputs): 
    # print(Intcode,'\n', type(Intcode), len(Intcode))
    upgradeAC=[]
    amplifier=[]
    for item in Intcode:
        if '-' in item:
            #print(item)
            upgradeAC.append(int(item))
        else:
            if len(str(item))==1:
                new_item='000'+str(item)
                #print(new_item)
                upgradeAC.append(new_item)
            elif len(item)==2:
                new_item='00'+item
                #print(new_item)
                upgradeAC.append(new_item)
            elif len(item)==3:
                new_item='0'+item
                #print(new_item)
                upgradeAC.append(new_item)
            else:
                #print(item)
                upgradeAC.append(int(item))
    # print(upgradeAC, len(upgradeAC))
    instruction_pointer=0
    while True:
        instruction=upgradeAC[instruction_pointer]
        # print('Pointer is',instruction_pointer)
        # print(instruction)
        # print('Opcode is',str(instruction)[-2]+str(instruction)[-1])
        if str(instruction)[-1]=='1':
            # print('Run opcode 1')
            # print('instruction pointer is',instruction_pointer)
            parameters1=int(upgradeAC[instruction_pointer+1])
            parameters2=int(upgradeAC[instruction_pointer+2]) 
            parameters3=int(upgradeAC[instruction_pointer+3]) 
            forH1=int(str(instruction)[-3])     
            forT1=int(str(instruction)[-4])
            if forH1==0 and forT1==0:
                add4=int(upgradeAC[parameters1])+int(upgradeAC[parameters2])
                upgradeAC[parameters3]=int(add4)
            elif forH1==1 and forT1==0:   
                add4=parameters1+int(upgradeAC[parameters2])
                upgradeAC[parameters3]=int(add4)
            elif forH1==0 and forT1==1:
                add4=int(upgradeAC[parameters1])+parameters2
                upgradeAC[parameters3]=int(add4)
            elif forH1==1 and forT1==1:   
                add4=parameters1+parameters2
                upgradeAC[parameters3]=int(add4)
            # print('Data following 1 is',parameters1,parameters2,parameters3)
            # print('Original p3 is',upgradeAC[parameters3],'upgrade to',add4) 
            instruction_pointer+=4        
        elif str(instruction)[-1]=='2':
            # print('Run opcode 2')
            # print('instruction pointer is',instruction_pointer)
            parameters4=int(upgradeAC[instruction_pointer+1])
            parameters5=int(upgradeAC[instruction_pointer+2])
            parameters6=int(upgradeAC[instruction_pointer+3]) 
            forH2=int(str(instruction)[-3])  
            forT2=int(str(instruction)[-4])
            if forH2==0 and forT2==0:
                multiply4=int(upgradeAC[parameters4])*int(upgradeAC[parameters5])
                upgradeAC[parameters6]=int(multiply4)
            elif forH2==1 and forT2==0:   
                multiply4=parameters4*int(upgradeAC[parameters5])
                upgradeAC[parameters6]=int(multiply4)
            elif forH2==0 and forT2==1:
                multiply4=int(upgradeAC[parameters4])*parameters5
                upgradeAC[parameters6]=int(multiply4)
            elif forH2==1 and forT2==1:   
                multiply4=parameters4*parameters5
                upgradeAC[parameters6]=int(multiply4)
            # print('Data following 2 is',parameters4,parameters5,parameters6)
            # print('Original p6 is',upgradeAC[parameters6],'upgrade to',multiply4)
            instruction_pointer+=4
        elif str(instruction)[-1]=='3' or str(instruction)[-1]=='4':    # opcode 3 or 4 
            if str(instruction)[-1]=='3' and instruction_pointer==0:
                # print('Run opcode 3')
                # print('instruction pointer is',instruction_pointer)
                ACuser=int(phase)
                # ACuser=input('enter')
                parameters7=int(upgradeAC[instruction_pointer+1])     
                upgradeAC[parameters7]=int(ACuser) 
                # print('Change position',parameters7,'to',int(ACuser))  
            elif str(instruction)[-1]=='3':
                # print('Run opcode 3')
                # print('instruction pointer is',instruction_pointer)
                ACuser=int(outputs)
                # ACuser=input('enter')
                parameters7=int(upgradeAC[instruction_pointer+1])     
                upgradeAC[parameters7]=int(ACuser) 
                # print('Change position',parameters7,'to',int(ACuser))  
            elif str(instruction)[-1]=='4':
                # print('Run opcode 4')
                # print('instruction pointer is',instruction_pointer)
                # print(instruction)
                forH4=int(str(instruction)[-3]) 
                # print('H position is',forH4)
                parameters8=int(upgradeAC[instruction_pointer+1])
                if forH4==0:
                    parameters9=int(upgradeAC[parameters8])
                    if parameters9==0:
                        print('Test40 pass (0)') 
                        
                    else:
                        print('Test failed bcz number',parameters9)
                        amplifier.append(parameters9)
                elif forH4==1:   
                    if parameters8==0:
                        print('Test41 pass (0)') 
                        
                    else:
                        print('Test failed bcz position number',parameters8)
                        amplifier.append(parameters9)
            instruction_pointer+=2
            # print('After opcode 3 or 4, instruction pointer is',instruction_pointer)
        elif str(instruction)[-1]=='5' or str(instruction)[-1]=='6':    # opcode 5 or 6 
            if str(instruction)[-1]=='5':
                # print('Run opcode 5')
                # print('instruction pointer is',instruction_pointer)
                parameters10=int(upgradeAC[instruction_pointer+1])
                # print('p10',parameters10,upgradeAC[parameters10])
                parameters11=int(upgradeAC[instruction_pointer+2])  
                # print('p11',parameters11) 
                forH5=int(str(instruction)[-3])     
                forT5=int(str(instruction)[-4])
                if forH5==0 and forT5==0:
                    if int(upgradeAC[parameters10]) is 0:
                        instruction_pointer+=3
                    else:
                        instruction_pointer+=3
                        instruction_pointer=int(upgradeAC[parameters11])
                        if instruction_pointer>len(Intcode):
                            # print('something too big1')
                            break
                elif forH5==1 and forT5==0:   
                    if parameters10 is 0:
                        instruction_pointer+=3
                    else:
                        instruction_pointer=int(upgradeAC[parameters11])
                        if instruction_pointer>len(Intcode):
                            # print('something too big2')
                            break
                elif forH5==0 and forT5==1:
                    if int(upgradeAC[parameters10]) is 0:
                        instruction_pointer+=3
                    else:
                        instruction_pointer=parameters11
                        if instruction_pointer>len(Intcode):
                            # print('something too big3')
                            break
                elif forH5==1 and forT5==1:   
                    if parameters10 is 0:
                        instruction_pointer+=3
                    else:
                        instruction_pointer=parameters11
                        if instruction_pointer>len(Intcode):
                            # print('something too big4')
                            break
                # print('Data following 5 is',parameters10,parameters11)
                # print('Pointer jumps to',instruction_pointer)    
            elif str(instruction)[-1]=='6':
                # print('Run opcode 6')
                # print('instruction pointer is',instruction_pointer)
                parameters12=int(upgradeAC[instruction_pointer+1])
                # print('p12',parameters12,upgradeAC[parameters12])
                parameters13=int(upgradeAC[instruction_pointer+2])   
                # print('p13',parameters13)
                forH6=int(str(instruction)[-3])     
                forT6=int(str(instruction)[-4])
                if forH6==0 and forT6==0:
                    if int(upgradeAC[parameters12]) is 0:
                        instruction_pointer=int(upgradeAC[parameters13])
                        if instruction_pointer>len(Intcode):
                            # print('something too big5')
                            break
                    else:
                        instruction_pointer+=3
                elif forH6==1 and forT6==0:   
                    if parameters12 is 0:
                        instruction_pointer=int(upgradeAC[parameters13])
                        if instruction_pointer>len(Intcode):
                            # print('something too big6')
                            break
                    else:
                        instruction_pointer+=3
                elif forH6==0 and forT6==1:
                    if int(upgradeAC[parameters12]) is 0:
                        instruction_pointer=parameters13
                        if instruction_pointer>len(Intcode):
                            # print('something too big7')
                            break
                    else:
                        instruction_pointer+=3
                elif forH6==1 and forT6==1:   
                    if parameters12 is 0:
                        instruction_pointer=parameters13
                        if instruction_pointer>len(Intcode):
                            # print('something too big8')
                            break
                    else:
                        instruction_pointer+=3
                # print('Data following 6 is',parameters12,parameters13)
                # print('Pointer jumps to',instruction_pointer) 
        elif str(instruction)[-1]=='7' or str(instruction)[-1]=='8':    # opcode 7 or 8 
            if str(instruction)[-1]=='7':
                # print('Run opcode 7')
                # print('instruction pointer is',instruction_pointer)
                parameters14=int(upgradeAC[instruction_pointer+1])
                parameters15=int(upgradeAC[instruction_pointer+2]) 
                parameters16=int(upgradeAC[instruction_pointer+3]) 
                forH7=int(str(instruction)[-3])     
                forT7=int(str(instruction)[-4])
                if forH7==0 and forT7==0:
                    if int(upgradeAC[parameters14])<int(upgradeAC[parameters15]):
                        upgradeAC[parameters16]=1
                    else:
                        upgradeAC[parameters16]=0
                elif forH7==1 and forT7==0:   
                    if parameters14<int(upgradeAC[parameters15]):
                        upgradeAC[parameters16]=1
                    else:
                        upgradeAC[parameters16]=0
                elif forH7==0 and forT7==1:
                    if int(upgradeAC[parameters14])<parameters15:
                        upgradeAC[parameters16]=1
                    else:
                        upgradeAC[parameters16]=0
                elif forH7==1 and forT7==1:   
                    if parameters14<parameters15:
                        upgradeAC[parameters16]=1
                    else:
                        upgradeAC[parameters16]=0
                # print('Data following 7 is',parameters14,parameters15,parameters16)
                instruction_pointer+=4  
            elif str(instruction)[-1]=='8':
                # print('Run opcode 8')
                # print('instruction pointer is',instruction_pointer)
                parameters17=int(upgradeAC[instruction_pointer+1])
                parameters18=int(upgradeAC[instruction_pointer+2]) 
                parameters19=int(upgradeAC[instruction_pointer+3]) 
                forH8=int(str(instruction)[-3])     
                forT8=int(str(instruction)[-4])
                if forH8==0 and forT8==0:
                    if int(upgradeAC[parameters17])==int(upgradeAC[parameters18]):
                        upgradeAC[parameters19]=1
                    else:
                        upgradeAC[parameters19]=0
                elif forH8==1 and forT8==0:   
                    if parameters17==int(upgradeAC[parameters18]):
                        upgradeAC[parameters19]=1
                    else:
                        upgradeAC[parameters19]=0
                elif forH8==0 and forT8==1:
                    if int(upgradeAC[parameters17])==parameters18:
                        upgradeAC[parameters19]=1
                    else:
                        upgradeAC[parameters19]=0
                elif forH8==1 and forT8==1:   
                    if parameters17==parameters18:
                        upgradeAC[parameters19]=1
                    else:
                        upgradeAC[parameters19]=0
                # print('Data following 8 is',parameters17,parameters18,parameters19)
                instruction_pointer+=4  
            # print('After opcode 7 or 8, instruction pointer is',instruction_pointer)
        elif int(instruction)==99:
                print('Stop for 99 at',instruction_pointer,'\n')
                if amplifier==[]:
                    amplifier.append(0)   
                break
        else:
            # print(instruction_pointer)
            # print(upgradeAC[instruction_pointer])
            # print('Something went wrong.')
            break
    # print('Amplifier outputs =',amplifier)
    return amplifier


with open('D7-data.txt','r') as intcode:
    int_data=intcode.read()
upgradeAC=list(int_data.split(','))
print(upgradeAC)
#print(type(upgradeAC),len(upgradeAC))  --> list, 678

# memory(upgradeAC)

startA=[]
inputA=0
for a1 in range(5):
    # memory(upgradeAC,a1,inputA)
    outputA=memory(upgradeAC,a1,inputA)
    startA.append([[a1],outputA])
    # print(a1,inputA,outputA)
# print('Outputs from Amplifier A =',startA)
# print('Data length in Amplifier A is',len(startA),'\n')    # List in list

startB=[]
inputB=startA
for a2 in range(5):
    for item2 in inputB:
    # memory(upgradeAC,a2,int(item2[0]))
        outputB=memory(upgradeAC,a2,int(item2[1][0]))
        if a2 in item2[0]:
            pass
        else:
            startB.append([[item2[0][0],a2],outputB])
        # print(a2,int(item2[0]),outputB)
# print('Outputs from Amplifier B =',startB)
# print('Data in Amplifier B is',len(startB),'\n')  

startC=[]
inputC=startB
for a3 in range(5):
    for item3 in inputC:
        # memory(upgradeAC,a3,int(item3[0]))
        outputC=memory(upgradeAC,a3,int(item3[1][0]))
        if a3 in item3[0]:
            pass
        else:
            startC.append([[item3[0][0],item3[0][1],a3],outputC])
        # print(a3,int(item3[0]),outputC)
# print('Outputs from Amplifier C =',startC)
# print('Data in Amplifier C is',len(startC),'\n')  

startD=[]
inputD=startC
for a4 in range(5):
    for item4 in inputD:
        # memory(upgradeAC,a4,int(item4[0]))
        outputD=memory(upgradeAC,a4,int(item4[1][0]))
        if a4 in item4[0]:
            pass
        else:
            startD.append([[item4[0][0],item4[0][1],item4[0][2],a4],outputD])
        # print(a4,int(item4[0]),outputD)
# print('Outputs from Amplifier D =',startD)
# print('Data in Amplifier D is',len(startD),'\n')  

startE=[]
inputE=startD
for a5 in range(5):
    for item5 in inputE:
        # memory(upgradeAC,a5,int(item5[0]))
        outputE=memory(upgradeAC,a5,int(item5[1][0]))
        if a5 in item5[0]:
            pass
        else:
            startE.append([[item5[0][0],item5[0][1],item5[0][2],item5[0][3],a5],outputE])
        # print(a5,int(item5[0]),outputE)
# print('Outputs from Amplifier E =',startE)
# print('Data in Amplifier E is',len(startE),'\n')  

intElist=[]
for data in startE:
    intElist.append(data[1])
print(max(intElist))

intcode.close()