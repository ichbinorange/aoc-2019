with open('D6-data.txt','r') as position:
  orbit_list=position.read().splitlines()

def ORBITS(orbits):
    for item in orbit_list:
        if item.startswith('COM'):
            startCOM=item
            print('Com is',item)
    orbit_list.remove(startCOM)
    orbit_list.insert(0,startCOM)

    P1list=[]    # P1 is A position
    P2list=[]    # P2 is B position
    Stream=[]    # For every branch, can look back later
    while len(orbit_list)!=0:
        map1=[]
        map2=[]
        for run in range(len(orbit_list)):
            for orbits in orbit_list:
                ABsplit=orbits.index(')')
                P1=str(orbits[0:int(ABsplit)])     # P1 is A position
                P2=str(orbits[int(ABsplit)+1:])    # P2 is B position
                if orbit_list.index(orbits)==0:
                    if  (P1 not in map1) and (P1 not in map1):
                        map1.append(P1)
                        map1.append(P2)
                        P1list.append(P1)
                        P2list.append(P2)
                        map2.append(orbits)
                else:
                    if (P1 in map1) and (P2 not in map1):
                        if P1 in P1list:
                            continue
                            # print('nothing1')
                        else: 
                            # print('P1 is',P1)
                            #print('insert after P1')
                            map1.insert(int(map1.index(P1)+1), P2)
                            P1list.append(P1)
                            P2list.append(P2)
                            map2.append(orbits)
                            # orbit_list.remove(orbits)
                    elif (P2 in map1) and (P1 not in map1):
                        if P2 in P2list:
                            continue
                            # print('nothing2')
                        else: 
                            # print('P2 is',P2)
                            # print('insert before P2')
                            map1.insert(int(map1.index(P2)), P1)
                            P1list.append(P1)
                            P2list.append(P2)
                            map2.append(orbits)
                            # orbit_list.remove(orbits)
                    elif  (P1 not in map1) and (P2 not in map1):
                        continue
                        # print('nothing3')    
        # print('Map1 =',map1)
        # print('Map2 =',map2)
        # print('Before removed used Orbits:',orbit_list)
        if 'COM' in map1:
            Stream.append(map1)
            # print('Main stream',Stream)
            for usedOrbits in map2:
                orbit_list.remove(usedOrbits)
            # print('After remove used Orbits:',orbit_list)       
        else:   # branch (no COM)
            Stream.append(map1)
            # print('Branch stream',Stream)
            for usedOrbits in map2:
                orbit_list.remove(usedOrbits)
    print(Stream)    # Stream length is 94            
    Bplus1CL=0
    # print(len(Stream))
    # Didn't calculate COM main stream due to first_item!=Slist
    for first_item in range(len(Stream)): # to find the 1st item in new Branch
        connector=Stream[first_item][0]   # the connector in new branch
        eachbranch=int(len(Stream[first_item]))   # the length of the new branch
        print(first_item,'stream =',Stream[first_item])
        print('The connector of',first_item,'is',connector)
        print('The length of the new branch is',eachbranch)
        Bitself=(eachbranch*(eachbranch-1))/2
        Bplus1CL+=Bitself
        print('The sum for Branch itself is',Bitself)
        for Slist in range(len(Stream)):  
            if connector in Stream[Slist]:  # to find the number of the connected Branch
                if first_item!=Slist:
                    print('Connector in stream',Slist,'is at position',Stream[Slist].index(connector))
                    ConnectL=(int(Stream[Slist].index(connector)))*(eachbranch-1) # +1 for connection zone
                    Bplus1CL+=ConnectL
                    print('The Brief sum of forward connected Branch1',Bplus1CL)
                    if 'COM' in Stream[Slist]:
                        continue
                    else:
                        connector2=Stream[Slist][0]   # the connector2 to forward branch
                        for Slist2 in range(len(Stream)): 
                            if connector2 in Stream[Slist2]:  # to find the number of the connected Branch
                                if Slist!=Slist2:
                                    print('Connector2 in stream',Slist2,'is at position',Stream[Slist2].index(connector2))
                                    ConnectL2=(int(Stream[Slist2].index(connector2)))*(eachbranch-1) 
                                    # print('Add the steps of forward connected Branch2',ConnectL2)
                                    Bplus1CL+=ConnectL2
                                    print('The Brief sum of forward connected Branch2',Bplus1CL)
                                    if 'COM' in Stream[Slist2]:
                                        continue
                                    else:
                                        connector3=Stream[Slist2][0]   # the connector2 to forward branch
                                        for Slist3 in range(len(Stream)): 
                                            if connector3 in Stream[Slist3]:  # to find the number of the connected Branch
                                                if Slist2!=Slist3:
                                                    print('Connector3 in stream',Slist3,'is at position',Stream[Slist3].index(connector3))
                                                    ConnectL3=(int(Stream[Slist3].index(connector3)))*(eachbranch-1) 
                                                    # print('Add the steps of forward connected Branch3',ConnectL3)
                                                    Bplus1CL+=ConnectL3
                                                    print('The Brief sum of forward connected Branch3',Bplus1CL)
                                                    if 'COM' in Stream[Slist3]:
                                                        continue
                                                    else:
                                                        connector4=Stream[Slist3][0]   # the connector2 to forward branch
                                                        for Slist4 in range(len(Stream)): 
                                                            if connector4 in Stream[Slist4]:  # to find the number of the connected Branch
                                                                if Slist3!=Slist4:
                                                                    print('Connector4 in stream',Slist4,'is at position',Stream[Slist4].index(connector4))
                                                                    ConnectL4=(int(Stream[Slist4].index(connector4)))*(eachbranch-1) 
                                                                    # print('Add the steps of forward connected Branch4',ConnectL4)
                                                                    Bplus1CL+=ConnectL4
                                                                    print('The Brief sum of forward connected Branch4',Bplus1CL)
                                                                    if 'COM' in Stream[Slist4]:
                                                                        continue
                                                                    else:
                                                                        connector5=Stream[Slist4][0]   # the connector2 to forward branch
                                                                        for Slist5 in range(len(Stream)): 
                                                                            if connector5 in Stream[Slist5]:  # to find the number of the connected Branch
                                                                                if Slist4!=Slist5:
                                                                                    print('Connector5 in stream',Slist5,'is at position',Stream[Slist5].index(connector5))
                                                                                    ConnectL5=(int(Stream[Slist5].index(connector5)))*(eachbranch-1) 
                                                                                    # print('Add the steps of forward connected Branch5',ConnectL5)
                                                                                    Bplus1CL+=ConnectL5
                                                                                    print('The Brief sum of forward connected Branch5',Bplus1CL)
                                                                                    if 'COM' in Stream[Slist5]:
                                                                                        continue
                                                                                    else:
                                                                                        connector6=Stream[Slist5][0]   # the connector2 to forward branch
                                                                                        for Slist6 in range(len(Stream)): 
                                                                                            if connector6 in Stream[Slist6]:  # to find the number of the connected Branch
                                                                                                if Slist5!=Slist6:
                                                                                                    print('Connector6 in stream',Slist6,'is at position',Stream[Slist6].index(connector6))
                                                                                                    ConnectL6=(int(Stream[Slist6].index(connector6)))*(eachbranch-1) 
                                                                                                    # print('Add the steps of forward connected Branch6',ConnectL6)
                                                                                                    Bplus1CL+=ConnectL6
                                                                                                    print('The Brief sum of forward connected Branch6',Bplus1CL)
ORBITS(orbit_list)

