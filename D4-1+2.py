# range: 367479-893698

possibilities=0
results=[]
# passwords=x
for password in range(367479,892698):
    x=str(password)
    if x[0]==x[1]:
        if x[1]<=x[2]<=x[3]<=x[4]<=x[5]:
            possibilities+=1
            results.append(x)
    elif x[1]==x[2]:
        if x[2]<=x[3]<=x[4]<=x[5] and x[0]<=x[1]:
            possibilities+=1
            results.append(x)
    elif x[2]==x[3]:
        if x[3]<=x[4]<=x[5] and x[0]<=x[1]<=x[2]:
            possibilities+=1
            results.append(x)
    elif x[3]==x[4]:
        if x[4]<=x[5] and x[0]<=x[1]<=x[2]<=x[3]:
            possibilities+=1
            results.append(x)
    elif x[4]==x[5]:
        if x[0]<=x[1]<=x[2]<=x[3]<=x[4]:
            possibilities+=1
            results.append(x)

print('Total possibilities',possibilities,'\n')

# --------- part2 ----------

round2=[]
possibilities2=0
for y in results:
    if (y[0]==y[1] and y[1]!=y[2]) or (y[1]==y[2] and y[0]!=y[1] and y[2]!=y[3]) or (y[2]==y[3] and y[1]!=y[2] and y[3]!=y[4]) or (y[3]==y[4] and y[2]!=y[3] and y[4]!=y[5]) or (y[4]==y[5] and y[3]!=y[4]):
        possibilities2+=1
        round2.append(y)

print('Total possibilities2',possibilities2)      
        
print(round2)
    
        
        