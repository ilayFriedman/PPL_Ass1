import math
import functools

## Question 1 : Complex Numbers
class ComplexNum:
    # 1.1
    def __init__(self,realPart,imaginaryPart):
        if(isinstance(realPart,(int, float, complex)) and isinstance(imaginaryPart,(int, float, complex))):
            self.rePart = realPart
            self.imPart = imaginaryPart
        else:
            raise TypeError("The inputs need to be a Number!\nThe complexNum didn't build.")

    # 1.2
    @property
    def re(self):
        return self.rePart

    @property
    def im(self):
        return self.imPart

    # 1.3
    def to_tuple(self):
        return (self.re,self.im)

    # 1.4
    def __repr__(self):
        if(self.im < 0):
            return (str(self.re) + " - " + str(self.im)[1:]+"i")
        else:
            return (str(self.re) + " + " + str(self.im)+"i")

    # 1.5
    def __eq__(self, other):
        if(isinstance(other,ComplexNum)):
            return other.re == self.re and other.im == self.im
        raise TypeError("expected to get a complex number")

    # 1.6
    def __add__(self, other):
        if (isinstance(other, ComplexNum)):
            return (ComplexNum(self.re+other.re,self.im+other.im))
        raise TypeError("expected to get a complex number")

    # 1.7
    def __neg__(self):
        return ComplexNum(-1*self.re,-1*self.im)

    def __sub__(self, other):
        if (isinstance(other, ComplexNum)):
            return (self.__add__(-other))
        raise TypeError("expected to get a complex number")

    # 1.8
    def __mul__(self, other):
        if (isinstance(other, ComplexNum)):
            return ComplexNum((self.re*other.re-self.im*other.im),(self.re*other.im+self.im*other.re))
        else:
            raise TypeError('Complex multiplication only defined for Complex Numbers.')

    # 1.9
    def conjugate(self):
        return (ComplexNum(self.re,-self.im))

    # 1.10
    def abs(self):
        return math.sqrt((self*self.conjugate()).re)

## Question 2 : Type & Is function

# 2.1
def isInstancePPL(object1, classInfo):
    if(object1 != None and classInfo != None):
        return (classInfo in type(object1).__mro__)
    else:
        raise TypeError ("First input has to be object and second input has to be class!")

# 2.2
def numInstancePPL(object1, classInfo):
    if(isInstancePPL(object1,classInfo) == False):
        return 0
    count = 1
    for currClass in type(object1).__mro__:
        if(currClass == classInfo):
            return count
        count+=1

# 2.3
def isSubclassPPL(Class, classInfo):
    if (Class != None and classInfo != None):
        return (classInfo in Class.__bases__ or Class is classInfo)
    else:
        raise TypeError ("First input has to be Class Type and second input has to be class!")

# 2.4
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
# print (isInstancePPL(y, X)) # TRUE
# print (isInstancePPL(y, Y)) # TRUE

# print("##---- 2.2 ----##")
# print (numInstancePPL(x,X)) # 1
# print (numInstancePPL(y,X)) # 2
# print (numInstancePPL(2,x)) # 0
# print (numInstancePPL(x,2)) # 0
# print (numInstancePPL(x,Y)) # 0


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
# print(numSubclassPPL(X, X)) # 0
# print(numSubclassPPL(Y, X)) # 2
# print(numSubclassPPL(y.__class__, Y)) # 1
#
#


#Question 3 : Higt Lever Functions

# 3.1
def count_if(lst,func):
    try:
        if(lst !=None and func != None):
            return len(list(filter(func, lst)))
    except:
       return ("Not good arguments!")
    return ("Not good arguments!")

# 3.2
def for_all(lst,func1,func2):
    try:
        if(lst !=None and func1 != None and func2 != None):
            return (len(lst) == count_if(map(func1,lst),func2))
    except:
       return ("Not good arguments!")
    return ("Not good arguments!")

# 3.3
def for_all_red(lst, func1, func2):
    try:
        return (func2(functools.reduce(func1,lst)))
    except:
       return ("Not good arguments!")
    return ("Not good arguments!")

# 3.4
def there_exists(lst, n, func1):
    if(n != None and count_if(lst,func1) >= n):
        return True
    else:
        return False
# print (count_if([1,0,8], 1))
# print (count_if([1,1,8], lambda x :x==1))
# print(for_all_red([1,0,8], lambda x,y: x*y, lambda x: x>0))
# print(for_all_red([1,1,8], lambda x,y: x*y, lambda x: x>0))

