class car(object):

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def getName(self):
        return self.name

    def gettype(self):
        return self.type

    def __str__(self):
        return "%s is a %s" % (self.name, self.type)

 
    def __init__(self):
        self.__updateSoftware()
 
    def drive(self):
        print 'driving'
 
    def __updateSoftware(self):
        print 'updating software'
 
    redcar = Car()
    redcar.drive()   

class Car:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print 'driving. maxspeed ' + str(self.__maxspeed)
 
    def setMaxSpeed(self,speed):
        self.__maxspeed = speed
 
redcar = Car()
redcar.drive()
redcar.setMaxSpeed(320)
redcar.drive()
class Car:
    def __init__(self, name):    
        self.name = name
 
    def drive(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
    def stop(self):             
        raise NotImplementedError("Subclass must implement abstract method")
 
class Sportscar(Car):
    def drive(self):
        return 'Sportscar driving!'
 
    def stop(self):
        return 'Sportscar breaking!'
 
class Truck(Car):
    def drive(self):
        return 'Truck driving slowly because heavily loaded.'
 
    def stop(self):
        return 'Truck breaking!'
 
 
cars = [Truck('Bananatruck'),
        Truck('Orangetruck'),
        Sportscar('Z3')]
 
for car in cars:
    print car.name + ': ' + car.drive() 
