from numpy import pi, sqrt 

class vector:

    def __init__(self, x, z):
        self.x = x
        self.z = z 

    def add(self, other):
        sumVect = vector(self.x + other.x, self.z + other.z)
        return sumVect 

    def sub(self, other):
        subVect = vector(self.x - other.x, self.z - other.z)
        return subVect 

    def mul(self, other):
        mulVect = vector(self.x * other, self.z * other)
        return mulVect 

    def length(self): 
        return sqrt((self.x * self.x) + (self.z * self.z))

    def normalize(self):
        distance = self.length()
        returnVect = vector(self.x / distance, self.z / distance)
        return returnVect 

    def print(self):
        print("X: " + str(self.x) + "\nZ: " + str(self.z)) 

