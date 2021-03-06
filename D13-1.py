def memory(Intcode):
    upgradeAC=Intcode
    instruction_pointer=0
    relative_base=0
    output_pool = []
    while True:
        instruction=upgradeAC[instruction_pointer]
        parameters1=int(upgradeAC[instruction_pointer+1])
        parameters2=int(upgradeAC[instruction_pointer+2]) 
        parameters3=int(upgradeAC[instruction_pointer+3]) 
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
            ACuser=input("BOOST program asks for a single input:")   
            if str(instruction)[-3]=='0':
                print('Pointer0',instruction_pointer)
                upgradeAC[parameters1]=int(ACuser) 
            elif str(instruction)[-3]=='2':
                upgradeAC[parameters1+relative_base]=int(ACuser) 
            instruction_pointer+=2
        elif str(instruction)[3:]=='04': 
            # print('opcode 4H0',forH)
            output_pool.append(forH)
            instruction_pointer+=2
        elif str(instruction)[3:]=='05':
            if forH is 0:
                instruction_pointer+=3
            else:
                instruction_pointer=forT
                if instruction_pointer>len(Intcode):
                    print('something too big1')
                    break
        elif str(instruction)[3:]=='06':
            if forH is 0:
                instruction_pointer=forT
                if instruction_pointer>len(Intcode):
                    print('something too big5')
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
    print('The lengh of output:',len(output_pool))
    print('Output:'+'\n', output_pool)

    block = 0
    for tile in range(0,len(output_pool),3):
        if output_pool[tile+2] == 2:
            block+=1
        # elif output_pool[tile+2] == 4:
        #     print('this is ball')       
    print('Total block number is ',block)

with open('D13-data.txt','r') as intcode:
    int_data=intcode.read()
arcade_input=list(int_data.split(','))

numerize=[]
for item in arcade_input:
    numerize.append(int(item))

# print(max(numerize),len(numerize))
for position in range(len(numerize),(max(numerize)+100)):
    numerize.insert(position,0)

# new way to add 0 and become 5-digits
arcade_input=[]
for item in numerize:
    new_item='%05d' % item
    arcade_input.append(new_item)

# print(arcade_input)
# print(len(arcade_input))
memory(arcade_input)

intcode.close()


