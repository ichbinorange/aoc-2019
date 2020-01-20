with open('D2-data.txt','r') as intcode:
    int_data=intcode.read()
#print(int_data)
#print(type(int_data))  -->str  
code=int_data.split(',')
print(code)
print(len(code),'\n')
#for i in code:
#    if i==',':
#        code.remove(i)

#print(code)

code[1]=12
code[2]=2

#print(type(code[1])) --> int
#print(code)

#test=code[1]
#print(code[1])
#print(test)
#if test==12:        --> True
#    print(True)
#else:
#    print(False)

print(code[0])
print(len(code))
num=0
print(num,'\n')
while True:
    #print(num)
    a=code[num]
    #print(code[num])
    #print(type(a))   --> str
    if int(a)==1:
        #print('a is',a)
        print(num)
        p1=int(code[num+1])
        print('p1=',p1)
        p2=int(code[num+2])  
        print('p2=',p2)          
        #print('code p1',code[p1],'and code p2',code[p2])
        add=int(code[p1])+int(code[p2])
        #print('add is',add)
        p3=int(code[num+3])
        print('p3=',p3)
        code[p3]=int(add) 
        print('code[p3] is',add,'\n')  
        #print(code,'\n')          
    elif int(a)==2:
        #print('a is',a)
        print(num)
        p4=int(code[num+1])
        print('p4=',p4)
        p5=int(code[num+2])
        print('p5=',p5)
        multiply=int(code[p4])*int(code[p5])
        #print('multiply is',multiply)
        p6=int(code[num+3])
        print('p6=',p6)
        code[p6]=int(multiply)
        print('code[p6] is',multiply,'\n') 
        #print(code,'\n') 
    elif int(a)==99:
        print('Stop fo 99 at',num,'\n')
        break
    else:
        print(num)
        print(code[num])
        print('Something wrong')
        break
    num+=4


print('\n')  
print(code[0])

intcode.close()