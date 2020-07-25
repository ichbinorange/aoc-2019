# I ＝ <x=14, y=4, z=5>
# E = <x=12, y=10, z=8>
# G = <x=1, y=7, z=-10>
# C = <x=16, y=-5, z=3>

moonI = [14,4,5]
moonE = [12,10,8]
moonG = [1,7,-10]
moonC = [16,-5,3]
'''sample 1
moonI = [-1,0,2]
moonE = [2,-10,-7]
moonG = [4,-8,8]
moonC = [3,5,-1]
sample 2
moonI = [-8,-10,0]
moonE = [5,5,10]
moonG = [2,-7,3]
moonC = [9,-8,-3]'''
vI = [0,0,0]
vE = [0,0,0]
vG = [0,0,0]
vC = [0,0,0]
step=1
while True:
    dvI = [0,0,0]
    dvE = [0,0,0]
    dvG = [0,0,0]
    dvC = [0,0,0]
    comparisonX = {'ieX':moonI[0]-moonE[0],'igX':moonI[0]-moonG[0],'icX':moonI[0]-moonC[0],'egX':moonE[0]-moonG[0],'ecX':moonE[0]-moonC[0],'gcX':moonG[0]-moonC[0]}
    comparisonY = {'ieY':moonI[1]-moonE[1],'igY':moonI[1]-moonG[1],'icY':moonI[1]-moonC[1],'egY':moonE[1]-moonG[1],'ecY':moonE[1]-moonC[1],'gcY':moonG[1]-moonC[1]}
    comparisonZ = {'ieZ':moonI[2]-moonE[2],'igZ':moonI[2]-moonG[2],'icZ':moonI[2]-moonC[2],'egZ':moonE[2]-moonG[2],'ecZ':moonE[2]-moonC[2],'gcZ':moonG[2]-moonC[2]}
    # print('Before dV:',dvI,dvE,dvG,dvC)
    if step<=1000:
        print('Step :',step)
        for itemX, value in comparisonX.items():
            if comparisonX[itemX]<0:
                if itemX == 'ieX':
                    dvI[0]+=1
                    dvE[0]-=1
                elif itemX == 'igX':
                    dvI[0]+=1
                    dvG[0]-=1
                elif itemX == 'icX':
                    dvI[0]+=1
                    dvC[0]-=1
                elif itemX == 'egX':
                    dvE[0]+=1
                    dvG[0]-=1
                elif itemX == 'ecX':
                    dvE[0]+=1
                    dvC[0]-=1
                elif itemX == 'gcX':
                    dvG[0]+=1
                    dvC[0]-=1
            elif comparisonX[itemX]>0:
                if itemX == 'ieX':
                    dvI[0]-=1
                    dvE[0]+=1
                elif itemX == 'igX':
                    dvI[0]-=1
                    dvG[0]+=1
                elif itemX == 'icX':
                    dvI[0]-=1
                    dvC[0]+=1
                elif itemX == 'egX':
                    dvE[0]-=1
                    dvG[0]+=1
                elif itemX == 'ecX':
                    dvE[0]-=1
                    dvC[0]+=1
                elif itemX == 'gcX':
                    dvG[0]-=1
                    dvC[0]+=1
        for itemY, value in comparisonY.items():
            if comparisonY[itemY]<0:
                if itemY == 'ieY':
                    dvI[1]+=1
                    dvE[1]-=1
                elif itemY == 'igY':
                    dvI[1]+=1
                    dvG[1]-=1
                elif itemY == 'icY':
                    dvI[1]+=1
                    dvC[1]-=1
                elif itemY == 'egY':
                    dvE[1]+=1
                    dvG[1]-=1
                elif itemY == 'ecY':
                    dvE[1]+=1
                    dvC[1]-=1
                elif itemY == 'gcY':
                    dvG[1]+=1
                    dvC[1]-=1
            elif comparisonY[itemY]>0:
                if itemY == 'ieY':
                    dvI[1]-=1
                    dvE[1]+=1
                elif itemY == 'igY':
                    dvI[1]-=1
                    dvG[1]+=1
                elif itemY == 'icY':
                    dvI[1]-=1
                    dvC[1]+=1
                elif itemY == 'egY':
                    dvE[1]-=1
                    dvG[1]+=1
                elif itemY == 'ecY':
                    dvE[1]-=1
                    dvC[1]+=1
                elif itemY == 'gcY':
                    dvG[1]-=1
                    dvC[1]+=1
        for itemZ, value in comparisonZ.items():
            if comparisonZ[itemZ]<0:
                if itemZ == 'ieZ':
                    dvI[2]+=1
                    dvE[2]-=1
                elif itemZ == 'igZ':
                    dvI[2]+=1
                    dvG[2]-=1
                elif itemZ == 'icZ':
                    dvI[2]+=1
                    dvC[2]-=1
                elif itemZ == 'egZ':
                    dvE[2]+=1
                    dvG[2]-=1
                elif itemZ == 'ecZ':
                    dvE[2]+=1
                    dvC[2]-=1
                elif itemZ == 'gcZ':
                    dvG[2]+=1
                    dvC[2]-=1
            elif comparisonZ[itemZ]>0:
                if itemZ == 'ieZ':
                    dvI[2]-=1
                    dvE[2]+=1
                elif itemZ == 'igZ':
                    dvI[2]-=1
                    dvG[2]+=1
                elif itemZ == 'icZ':
                    dvI[2]-=1
                    dvC[2]+=1
                elif itemZ == 'egZ':
                    dvE[2]-=1
                    dvG[2]+=1
                elif itemZ == 'ecZ':
                    dvE[2]-=1
                    dvC[2]+=1
                elif itemZ == 'gcZ':
                    dvG[2]-=1
                    dvC[2]+=1
        print('After dV:',dvI,dvE,dvG,dvC)
        # velocityI=list(map(lambda x :x[0]+x[1] ,zip(vI,dvI)))
        vI = list(map(lambda x,y: x+y, vI, dvI))
        vE = list(map(lambda x,y: x+y, vE, dvE))
        vG = list(map(lambda x,y: x+y, vG, dvG))
        vC = list(map(lambda x,y: x+y, vC, dvC))
        print('Velocity:',vI,vE,vG,vC)
        moonI = list(map(lambda x,y: x+y, moonI, vI))
        moonE = list(map(lambda x,y: x+y, moonE, vE))
        moonG = list(map(lambda x,y: x+y, moonG, vG))
        moonC = list(map(lambda x,y: x+y, moonC, vC))
        print('Location:',moonI,moonE,moonG,moonC)
        step+=1
    else:
        break
print('\nFinal Velocity:',vI,vE,vG,vC)
print('Final Location:',moonI,moonE,moonG,moonC)
potentialEi=0
potentialEe=0
potentialEg=0
potentialEc=0
kineticEi=0
kineticEe=0
kineticEg=0
kineticEc=0
for num in moonI:
    potentialEi+=abs(num)
# print('pE for moonI',potentialEi)
for num in moonE:
    potentialEe+=abs(num)
# print('pE for moonE',potentialEe)
for num in moonG:
    potentialEg+=abs(num)
# print('pE for moonG',potentialEg)
for num in moonC:
    potentialEc+=abs(num)
# print('pE for moonC',potentialEc)
for numK in vI:
    kineticEi+=abs(numK)
# print('kE for moonI',kineticEi)
for numK in vE:
    kineticEe+=abs(numK)
# print('kE for moonE',kineticEe)
for numK in vG:
    kineticEg+=abs(numK)
# print('kE for moonG',kineticEg)
for numK in vC:
    kineticEc+=abs(numK)
# print('kE for moonC',kineticEc)

Total=potentialEi*kineticEi+potentialEe*kineticEe+potentialEg*kineticEg+potentialEc*kineticEc
print('Total energy in the system:',Total)
