def memory(Intcode):
    # print(Intcode,'\n', type(Intcode), len(Intcode))
    upgradeAC=[]
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
        print(instruction)
        print('Opcode is',str(instruction)[-2]+str(instruction)[-1])
        if str(instruction)[-1]=='1':
            print('Run opcode 1 with 4 digits')
            print('instruction pointer is',instruction_pointer)
            parameters1=int(upgradeAC[instruction_pointer+1])
            parameters2=int(upgradeAC[instruction_pointer+2]) 
            parameters3=int(upgradeAC[instruction_pointer+3])
            # if parameters1<0 or parameters2<0: 
            #     addminus1=parameters1+parameters2
            #     upgradeAC[parameters3]=int(addminus1)
            #     print('Change position',parameters3,'to',addminus1)
            
            # forH/forT is looking for position mode(0) or immediate mode(1)
            # for10T is always position mode(0)    
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
            print('Data following 1 is',parameters1,parameters2,parameters3)
            print('Original p3 is',upgradeAC[parameters3],'upgrade to',add4) 
            instruction_pointer+=4        
        
        elif str(instruction)[-1]=='2':
            print('Run opcode 2 with 4 digits')
            print('instruction pointer is',instruction_pointer)
            parameters4=int(upgradeAC[instruction_pointer+1])
            # print(parameters4)
            parameters5=int(upgradeAC[instruction_pointer+2])
            # print(parameters5)
            parameters6=int(upgradeAC[instruction_pointer+3])
            # print(parameters6)
            # if parameters4<0 or parameters5<0: 
            #     addminus2=parameters4+parameters5
            #     upgradeAC[parameters6]=int(addminus2)
                
            # forH/forT is looking for position mode(0) or immediate mode(1)
            # for10T is always position mode(0)  
            forH2=int(str(instruction)[-3])  
            # print(forH2)   
            forT2=int(str(instruction)[-4])
            # print(forT2)   
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
            print('Data following 2 is',parameters4,parameters5,parameters6)
            print('Original p6 is',upgradeAC[parameters6],'upgrade to',multiply4)
            instruction_pointer+=4
        elif str(instruction)[-1]=='3' or str(instruction)[-1]=='4':    # opcode 3 or 4 
            if str(instruction)[-1]=='3':
                print('Run opcode 3')
                print('instruction pointer is',instruction_pointer)
                ACuser=input("Please enter the ID for the ship's air conditioner unit: ")
                # print('Input is',ACuser)
                if ACuser=='1':
                    parameters7=int(upgradeAC[instruction_pointer+1])
                    print('Data following 3 is',parameters7)
                    print('Original num is',upgradeAC[parameters7])        
                    upgradeAC[parameters7]=int(ACuser) 
                    print('Change position',parameters7,'to',int(ACuser)) 
                else:
                    print('Input',ACuser,'is not corrected.')
                    break  
            elif str(instruction)[-1]=='4':
                print('Run opcode 4')
                print('instruction pointer is',instruction_pointer)
                print(instruction)
                forH4=int(str(instruction)[-3]) 
                print('H position is',forH4)
                if forH4==0:
                    parameters8=int(upgradeAC[instruction_pointer+1])
                    parameters9=int(upgradeAC[parameters8])
                    if parameters9==0:
                        print('Test pass (0)') 
                    else:
                        print('Test failed bcz position',parameters8,'is number',int(upgradeAC[int(parameters8)]))
                        break
                elif forH4==1:   
                    parameters10=int(upgradeAC[instruction_pointer+1])
                    if parameters10==0:
                        print('Test pass (0)') 
                    else:
                        print('Test failed bcz position',parameters8,'is number',int(upgradeAC[int(parameters8)]))
                        break
            instruction_pointer+=2
            print('After opcode 3 or 4, instruction pointer is',instruction_pointer)
        elif int(instruction)==99:
                print('Stop fo 99 at',instruction_pointer,'\n')
                break
        else:
            print(instruction_pointer)
            print(upgradeAC[instruction_pointer])
            print('Something went wrong.')
            break
    print('Position[0] is',upgradeAC[0])


with open('D5-data.txt','r') as intcode:
    int_data=intcode.read()
upgradeAC=list(int_data.split(','))
#print(upgradeAC)
#print(type(upgradeAC),len(upgradeAC))  --> list, 678

memory(upgradeAC)


intcode.close()