with open('D8-data.txt','r') as pixels:
    pixels_data=pixels.read()

layers={}
layernum=1
layer=[]
num=1
for pixel in pixels_data:
    if num<150:
        layer.insert(num,pixel)
        num+=1
    else:
        layer.insert(num,pixel)
        layers[layernum]=layer
        layernum+=1
        num=1
        layer=[]
# print(layers)

# print('Before',layers[1])  # original layer 1
for key in range(2,101):
    for value in range(150):
        if layers[1][value]=='2':
            layers[1][value]=layers[key][value]
    
# print('After',layers[1])   # top visible pixel

for locate in range(150):
    if layers[1][locate]=='0':
        layers[1].pop(locate)
        layers[1].insert(locate,' ')

print(' '.join(layers[1][0:24]))
print(' '.join(layers[1][25:49]))
print(' '.join(layers[1][50:74]))
print(' '.join(layers[1][75:99]))
print(' '.join(layers[1][100:124]))
print(' '.join(layers[1][125:149]))

pixels.close()