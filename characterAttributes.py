#Colby McClure, Paige Smith
#
#Character class 
#class for character attributes:
#   Id, steering behavior, initial position, initial velocity, initial orientation, 
#   max velocity, max acceleration, target, arrival radius, slowing radius, time to target

class character:
    def __init__(self, ID, steering, initPosition, initOrientation, maxVel, target, arrivalRadius, slowingRadius, timeTarget):
        self.ID = ID
        self.steeringBehavior = steering
        self.initialPosition = initPosition
        self.initialOrientation = initOrientation
        self.maxVelocity = maxVel
        self.target = target
        self.arrivalRadius = arrivalRadius
        self.slowingRadius = slowingRadius
        self.timeTarget = timeTarget

        