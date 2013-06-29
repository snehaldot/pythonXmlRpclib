class Parent:
    parentAttr = 100

    def __init__(self):
        print "Calling parent constructor"
 
    def parentMethod(self):
        print "calling parent mathod "

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print " Parent attribute :", Parent.parentAttr

class Child(Parent):
    def __init__(self):
       print "calling cild constructor"

    def childMethod(self):
       print "calling child method "

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

