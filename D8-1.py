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

# print(layers) -->100 layers 
# print(len(layers[100])) --> 150 pixels per layer, ie 25*6=150

count0={}
pixel0=0
for num in range(1,101):
    # print(layers[num])
    for pixel in layers[num]:
        if pixel=='0':
            pixel0+=1
        count0[num]=pixel0
    pixel0=0
# print(count0) --> layer 11 gets five 'zero' 

count12={}
from collections import Counter
for key in range(1,101):
    count12[key]=Counter(layers[key])
print(count12)
# print(count12) --> layer 11 gets 23 'one' and 122 'two' -->23*122=2806

pixels.close()