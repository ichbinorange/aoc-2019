# based on D10-1 result, (23,19) is the new monitoring station
import numpy as np
import operator, math, cmath

# angle = atan2( y2-y1, x2-x1 )
# print(math.degrees(b)) -->convert from radian to angle

def vaporization(station,asteroid):  # asteroids = 325 stars
    anglecollect={}
    quadrant1={}
    quadrant2={}
    quadrant3={}
    quadrant4={}
    for star1 in asteroid:
        radian=math.atan2(star1[1]-station[1],star1[0]-station[0])
        angle=(math.degrees(radian))
# adjust "up" as 0 degree & one circle as 360 degrees
        if 0<=angle<=90:
            angle=angle+90
            # quadrant2[star1]="%.2f" % float(angle)
        elif 90<angle<=180:
            angle=angle+90
            # quadrant3[star1]="%.2f" % float(angle)
        elif -90<=angle<0:
            angle=90+angle
            # quadrant1[star1]="%.2f" % float(angle)
        elif -180<angle<-90: 
            angle=(180+angle)+270 
            # quadrant4[star1]="%.2f" % float(angle) 
        else:
            print('Something wrong.')  
        anglecollect[star1]="%.2f" % float(angle)
    ''' using quadrants
    print('Quadrant1:',quadrant1,'\n')
    print('Quadrant2:',quadrant2,'\n')
    print('Quadrant3:',quadrant3,'\n')
    print('Quadrant4:',quadrant4,'\n')
    items1=quadrant1.items()
    backitems1=[[value[1],value[0]] for value in items1]
    backitems1.sort()
    print('After sorted quadrant1:',backitems1,'\n')
    items2=quadrant2.items()
    backitems2=[[value[1],value[0]] for value in items2]
    backitems2.sort()
    print('After sorted quadrant2:',backitems2,'\n')
    items3=quadrant3.items()
    backitems3=[[value[1],value[0]] for value in items3]
    backitems3.sort()
    print('After sorted quadrant3:',backitems3,'\n')
    items4=quadrant4.items()
    backitems4=[[value[1],value[0]] for value in items4]
    backitems4.sort()
    print('After sorted quadrant4:',backitems4,'\n')'''
    items=anglecollect.items()
    backitems=[[value[1],value[0]] for value in items]
    backitems.sort()
    return backitems

with open('D10-data.txt','r') as Position:
    data=Position.read().splitlines()

''' To confirm the number of asteroids (#)
calculate=0
for item in data:
    for poundkey in item:
        if poundkey=='#':
            calculate+=1
print(calculate)'''

def twoD(oneD):
    pre_belt=[]
    a=0
    for row in oneD:
        pre_belt.insert(a,[])
        for line in list(row):
            pre_belt[a].append(line)
        a+=1
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

def newStation(findasteroid):
    detection={}
    for value1 in findasteroid:   # value is coordinate with '#' symbol, x=value[0] & y=value[1]
        briefcollectR=[]
        briefcollectC=[]
        briefcollectT=[]
        briefnum=0
        for value2 in findasteroid:
            if int(value1[0])==int(value2[0]) and int(value1[1])!=int(value2[1]):   # same column
                if value2[1]>=value1[1]:
                    samecolumn=(value2[1]-value1[1])/(value2[1]-value1[1])
                else:
                    samecolumn=(value2[1]-value1[1])/(-(value2[1]-value1[1]))
                if samecolumn not in briefcollectR:
                    briefcollectR.append(samecolumn)
                    briefnum+=1
            elif int(value1[0])!=int(value2[0]) and int(value1[1])==int(value2[1]): # same row
                if value2[0]>=value1[0]:
                    samerow=(value2[0]-value1[0])/(value2[0]-value1[0])
                else:
                    samerow=(value2[0]-value1[0])/(-(value2[0]-value1[0]))
                if samerow not in briefcollectC:
                    briefcollectC.append(samerow)
                    briefnum+=1
            elif int(value1[0])!=int(value2[0]) and int(value1[1])!=int(value2[1]): # triangle
                triangleX=value2[0]-value1[0]
                triangleY=value2[1]-value1[1]
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
            else:
                continue
        detection[value1]=briefnum
    # print(detection,'\n')
    # print(max(detection.items(), key=operator.itemgetter(1))[0],detection[max(detection.items(), key=operator.itemgetter(1))[0]])
    return list(max(detection.items(), key=operator.itemgetter(1))[0]) # return a list: [23,19]

print(vaporization(newStation(findasteroid(twoD(data))),findasteroid(twoD(data))))

Position.close()