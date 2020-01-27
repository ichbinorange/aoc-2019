import numpy as np
import operator

def newStation(findasteroid):
    detection={}
    for value1 in findasteroid:   # value is coordinate with '#' symbol, x=value[0] & y=value[1]
        briefcollectR=[]
        briefcollectC=[]
        briefcollectT=[]
        briefnum=0
        for value2 in findasteroid:
            # print('Value1',value1,'and Value2',value2)
            if int(value1[0])==int(value2[0]) and int(value1[1])!=int(value2[1]):   # same column
                if value2[1]>=value1[1]:
                    samecolumn=(value2[1]-value1[1])/(value2[1]-value1[1])
                else:
                    samecolumn=(value2[1]-value1[1])/(-(value2[1]-value1[1]))
                # print('Column',samecolumn)
                if samecolumn not in briefcollectR:
                    briefcollectR.append(samecolumn)
                    briefnum+=1
                    # print('ColumnAdd',briefnum)
            elif int(value1[0])!=int(value2[0]) and int(value1[1])==int(value2[1]): # same row
                if value2[0]>=value1[0]:
                    samerow=(value2[0]-value1[0])/(value2[0]-value1[0])
                else:
                    samerow=(value2[0]-value1[0])/(-(value2[0]-value1[0]))
                # print('Row',samerow)
                if samerow not in briefcollectC:
                    briefcollectC.append(samerow)
                    briefnum+=1
                    # print('RowAdd',briefnum)
            elif int(value1[0])!=int(value2[0]) and int(value1[1])!=int(value2[1]): # triangle
                triangleX=value2[0]-value1[0]
                triangleY=value2[1]-value1[1]
                # print('Triangle',triangleX/triangleY)
                if triangleX>=0 and triangleY>=0:
                    triangle='UR'+str(triangleX/triangleY)
                elif triangleX>=0 and triangleY<0:
                    triangle='UL'+str(triangleX/triangleY)
                elif triangleX<0 and triangleY>=0:
                    triangle='BR'+str(triangleX/triangleY)
                elif triangleX<0 and triangleY<0:
                    triangle='BL'+str(triangleX/triangleY)
                if triangle not in briefcollectT:
                    briefcollectT.append(triangle)
                    briefnum+=1
                    # print('TriangleAdd',briefnum)
            else:
                continue
        detection[value1]=briefnum
    print(detection)
    print(max(detection.items(), key=operator.itemgetter(1))[0],detection[max(detection.items(), key=operator.itemgetter(1))[0]])

with open('D10-data.txt','r') as Position:
    data=Position.read().splitlines()

def twoD(oneD):
    pre_belt=[]
    a=0
    for row in oneD:
        pre_belt.insert(a,[])
        for line in list(row):
            pre_belt[a].append(line)
        a+=1
    # print(len(pre_belt), len(pre_belt[0]))  --> 36 36
    real_belt = np.array(pre_belt).reshape(len(pre_belt), len(pre_belt[0]))
    return real_belt

def findasteroid(beltmap):
    collection={}
    for y_axis in range(len(beltmap)):
        for x_axis in range(len(beltmap[0])):
            if beltmap[y_axis][x_axis]=='#':
                collection[x_axis,y_axis]='#'
            else:
                x_axis+=1
        y_axis+=1
    return collection

newStation(findasteroid(twoD(data)))

Position.close()