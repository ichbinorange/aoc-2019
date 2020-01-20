## puzzle 1
#with open('D1-data.txt','r') as f:
#   read_data=f.read().splitlines()

#sum=0
#for data in read_data:
#    num=int(data) 
#    print(num) 
#    fuel=num//3-2
#    sum+=fuel
#    print(sum,'\n')
    
#print(sum)

#f.close()

## puzzle 2
with open('D1-data.txt','r') as f2:
    read_data2=f2.read().splitlines()

sum2=0
new_list2=[]
for data2 in read_data2:
    num2=int(data2)
    print(num2)
    each_sum=0 
    if num2>0:
        fuel2=num2//3-2
        each_sum+=fuel2
        print(each_sum)
        while fuel2>0:
            fuel2=fuel2//3-2
            if fuel2<=0:
                break
            each_sum+=fuel2

    sum2+=each_sum
    print(sum2,'\n')
    
print(sum2)

f2.close()