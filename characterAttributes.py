
#Colby McClure, Paige Smith
#
#Character class 
#class for character attributes:
#   Id, steering behavior, initial position, initial velocity, initial orientation, 
#   max velocity, max acceleration, target, arrival radius, slowing radius, time to target

import vectorOperations as vp
import numpy as np

class character:

    id: int 
    steering: int 
    inititalPosition: np.ndarray
    initialOrientation: float 
    maxVelocity: float
    target: int 
    arrivalRadius: float 
    slowingRadius: float 
    timeTarget: float 

    def __init__(self, id, steering, initPosition, initOrientation, maxVel, maxAcc, target, arrivalRadius, slowingRadius, timeTarget):
        self.id = id
        self.steeringBehavior = steering
        self.initialPosition = initPosition
        self.initialOrientation = initOrientation
        self.maxVelocity = maxVel
        self.maxAcceleration = maxAcc
        self.target = target
        self.arrivalRadius = arrivalRadius
        self.slowingRadius = slowingRadius
        self.timeTarget = timeTarget

    def seek(self, other):
        
        result = SteeringOutput()
        result.linear = other.initialPosition - self.initialPosition
        result.linear = vp.normalize(result.linear) 
        result.linear *= self.maxAcceleration

        