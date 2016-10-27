# -*- coding: utf-8 -*-


def deep_reverse(L):
    n = len(L)
    for i in range(int(n/2)):
        temp = L[i]
        L[i] =  L[n-i-1]
        L[n-i-1] = temp
    for j in L:
        n = len(j)
        for k in range(int(n/2)):
            temp = j[k]
            j[k] = j[n-k-1]
            j[n-k-1] = temp

#L = [[1, 2], [3, 4], [5, 6, 7]]
#deep_reverse(L)
#print(L)
def f(i):
    return i + 2
def g(i):
    return i > 5
    
def dict_interdiff(d1, d2):
    inter = {}
    diff = {}
    reslt = ()
    for k in d1.keys():
        if k in d2.keys():
            fval = f(d1.get(k),d2.get(k))
            inter[k] = fval
        else:
            diff[k] = d1.get(k)
    for k in d2.keys():
        if k not in inter.keys():
            diff[k] = d2.get(k)
    reslt = (inter,diff)
    return reslt

def applyF_filterG(L, f, g):
    for item in L[:]:
        print("item: " + str(item))
        flag = g(f(item))
        if flag == False:
            print("Index of : " + str(item) + " is: " + str(L.index(item)))
            del(L[L.index(item)])
            print(L)
    if len(L) == 0:
        return -1
    else:
        return max(L)
def flattenRec(aList):
    result = []
    tempList = aList[:]
    #print(aList)
    for item in tempList:
        if type(item) is list:
            #result.append(flattenRec(item))
            subResult = flattenRec(item)
            result+= subResult
        else:
            result.append(item)
    #print("Result: " +" ".join(map(str,result)))
    return result
    
   # return result
def flatten(aList):
    result = []
    tempList = aList[:]
    stillNested = True
    while stillNested:
        stillNested = False
        if len(result) !=0:
            tempList = result[:]
            result = []
        for item in tempList:
            if type(item) is list:
                stillNested = True
                for subItem in item:
                    result.append(subItem)
            else:
                result.append(item)
    return result
L = [[1,'a',['cat'],2],[[[3]],'dog'],4,5,['rat']]

class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    def __eq__(self,obj):
        return (self.x==obj.x) and (self.y == obj.y)
    def __repr__(self):
        return "<{},{}>".format(self.x,self.y)
c = Coordinate(2,5)
d = Coordinate(1,3)
print(c==d)
cDouble = eval(repr(c))
print(c==cDouble)
print(repr(d))
#L = [[1,'a'],4,5]
#print(flattenRec(L))
#L = [0, -10, 2,8,3, 5, 6, -4]
#print(applyF_filterG(L, f, g))
#print(L)        