import math
## Question 1 : Complex Numbers
class ComplexNum:
    # 1.1
    def __init__(self,realPart,imagineryPart):
        self.rePart = realPart
        self.imPart = imagineryPart

    # 1.2
    def re(self):
        return self.rePart

    def im(self):
        return self.imPart

    # 1.3
    def to_tuple(self):
        return (self.rePart,self.imPart)

    # 1.4
    def __repr__(self):
        if(self.im() < 0):
            return (str(self.rePart) + " - " + str(self.imPart)[1:]+"i")
        else:
            return (str(self.rePart) + " + " + str(self.imPart)+"i")

    # 1.5
    def __eq__(self, other):
        if(isinstance(other,ComplexNum)):
            return other.re() == self.rePart and other.im() == self.imPart

    # 1.6
    def __add__(self, other):
        if (isinstance(other, ComplexNum)):
            return (ComplexNum(self.re()+other.re(),self.im()+other.im()))

    # 1.7
    def __neg__(self):
        return ComplexNum(-1*self.rePart,-1*self.imPart)

    def __sub__(self, other):       ## check how to return complex number
        if (isinstance(other, ComplexNum)):
            return (self.__add__(-other))

    # 1.8
    def __mul__(self, other):
        if (isinstance(other, ComplexNum)):
            return ComplexNum((self.rePart*other.rePart-self.imPart*other.imPart),(self.rePart*other.imPart+self.imPart*other.rePart))
        else:
            raise TypeError('Complex multiplication only defined for Complex Numbers.')

    # 1.9
    def conjugate(self):
        return ComplexNum(self.rePart,-self.imPart)

    # 1.10
    def abs(self):
        return math.sqrt((self*self.conjugate()).rePart)
#
# a = ComplexNum(3,-2)
# b = ComplexNum(3,-2)
# z = ComplexNum(1, 2)
# print (a+b+z*z)


## Question 2 : Type & Is function
def isInstancePPL(object1, classInfo):
    return (classInfo in type(object1).__mro__)

def numInstancePPL(object1, classInfo):
    if(isInstancePPL(object1,classInfo) == False):
        return 0
    count = 1
    for currClass in type(object1).__mro__:
        if(currClass == classInfo):
            return count
        count+=1

def isSubclassPPL(Class, classInfo):
    return (classInfo in Class.__bases__ or Class is classInfo)

def numSubclassPPL(Class, classInfo):
    if(isSubclassPPL(Class,classInfo) == False):
        return 0
    count = 2
    for currClass in Class.__bases__:
        if(currClass is classInfo):
            return count
        count+=1
    return 1

# class X(): pass
# class Y(X): pass
# x = X()
# y = Y()
# print("##---- 2.1 ----##")
# print (isInstancePPL(x, X)) # TRUE
# print (isInstancePPL(x, Y)) # False
# print (isInstancePPL(type(y), X)) # TRUE
# print (isInstancePPL(y, Y)) # TRUE
#
# print("##---- 2.2 ----##")
# print (numInstancePPL(x,X)) # 1
# print (numInstancePPL(y,X)) # 2
# print (numInstancePPL(2,x)) # 0
# print (numInstancePPL(x,2)) # 0
# print (numInstancePPL(x,Y)) # 0
#
#
# print("##---- 2.3 ----##")
# print(isSubclassPPL(X, X)) # TRUE
# print(isSubclassPPL(X, Y)) # FALSE
# print(isSubclassPPL(Y, X)) # TRUE
# print(isSubclassPPL(Y, Y))# TRUE
# print("-----")
# print(isSubclassPPL(type(x), X)) # TRUE
# print(isSubclassPPL(type(x), Y)) # FALSE
# print(isSubclassPPL(type(y), X)) # TRUE
# print(isSubclassPPL(type(y), Y)) # TRUE
# print("-----")
# print(isSubclassPPL(x.__class__, X)) # TRUE
# print(isSubclassPPL(x.__class__, Y)) # FALSE
# print(isSubclassPPL(y.__class__, X)) # TRUE
# print(isSubclassPPL(y.__class__, Y)) # TRUE
#
# print("##---- 2.4 ----##")
# print(numSubclassPPL(Y, Y)) # 1
# print(numSubclassPPL(X, Y)) # 0
# print(numSubclassPPL(Y, X)) # 2
# print(numSubclassPPL(y.__class__, Y)) # 1




