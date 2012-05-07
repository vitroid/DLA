from math import *
zoom=5
w=100
size(w*zoom,w*zoom)
background(0)

class vector():
    def __init__(self,x,y=None):
        if y==None:
            self.x = x.x
            self.y = x.y
        else:
            self.x = x
            self.y = y
#dx,dy are unit vector
def fly(i,d,map):
    last = vector(i)
    i.x += d.x
    i.y += d.y
    if i.y >= w:
        return False
    if d.x < 0 and i.x < 0:
        return False
    if d.x > 0 and i.x >= w:
        return False
    if 0 <= i.x < w and map[int(i.x)][int(i.y)]:
        if 0 <= last.x < w:
            map[int(last.x)][int(last.y)] = 1
        return False
    return True

def initparticle():
    target=vector(int(random()*w),int(random()*w))
    theta = random()*pi
    d=vector(cos(theta),sin(theta))
    i=vector(int(target.x - target.y*d.x/d.y),0)
    if i.x < 0:
        i.y = (-1 - i.x)*d.y/d.x
        i.x = -1
    if i.x >= w:
        i.y = (w - i.x)*d.y/d.x
        i.x = w
    return i,d

map=[[0]*w for i in range(w)]
for i in range(w):
    map[i][w-1] = 1

#先に目的地を決め、そこから逆行してスタート地点を決める。
i,d = initparticle()

fill(1,1,1)
speed(100)

i0 = vector(i)
d0 = vector(d)
nloop = 2.0
brightness = 1.0
def draw():
    background(0)
    colormode(HSB)
    global i,d,map,nloop,i0,d0,brightness
    hist = [(i0,d0)]
    for loop in range(int(nloop)):
        if not fly(i,d,map):
            i,d = initparticle()
            i0 = vector(i)
            d0 = vector(d)
            hist.append((i0,d0))
    if FRAME % 10 == 0:
        nloop *= 1.4
        brightness *= 0.95
    print nloop,FRAME
    stroke(1,0,brightness)
    for i0,d0 in hist:
        end = vector(i0.x + (w-i0.y)*d0.x/d0.y,w)
        line((i0.x+0.5)*zoom,(i0.y+0.5)*zoom,(end.x+0.5)*zoom,(end.y+0.5)*zoom)
    nostroke()
    fill(1,0,1)
    for y in range(w):
        for x in range(w):
            if map[x][y]:
                rect(x*zoom,y*zoom,zoom,zoom)
    oval(i.x*zoom,i.y*zoom,zoom*1.8,zoom*1.8)


    

    

