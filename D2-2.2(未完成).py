def memory(Intcode,position0):
    address=Intcode.split(',')
    print(address)
    print(len(address),'\n')
    instruction_pointer=0
    for noun in range(99):
        for verb in range(99):
            noun=int(address[1])
            verb=int(address[2])
            while True:
                instruction=address[instruction_pointer]
                if int(instruction)==1:
                    parameters1=int(address[instruction_pointer+1])
                    parameters2=int(address[instruction_pointer+2])           
                    add=int(address[parameters1])+int(address[parameters2])
                    parameters3=int(address[instruction_pointer+3])
                    address[parameters3]=int(add)        
                elif int(instruction)==2:
                    parameters4=int(address[instruction_pointer+1])
                    parameters5=int(address[instruction_pointer+2])
                    multiply=int(address[parameters4])*int(address[parameters5])
                    parameters6=int(address[instruction_pointer+3])
                    address[parameters6]=int(multiply)
                elif int(instruction)==99:
                    print('Stop fo 99 at',instruction_pointer,'\n')
                    break
                else:
                    print(instruction_pointer)
                    print(address[instruction_pointer])
                    print('Something wrong')
                    break
                instruction_pointer+=4
                if int(address[0])==position0:
                    print('address[0]=',position0)
                    break            
    answer=100*noun+verb
    print(answer)
    print(noun,'\n',verb)


with open('D2-data.txt','r') as intcode:
    int_data=intcode.read()
memory(int_data,19690720)
