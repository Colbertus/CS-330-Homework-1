
#Colby McClure, Paige Smith
#
#Character class 
#class for character attributes:
#   Id, steering behavior, initial position, initial velocity, initial orientation, 
#   max velocity, max acceleration, target, arrival radius, slowing radius, time to target

import vectorOperations as vp
import numpy as np
import math 

class steeringOutput:
    linear : np.ndarray
    angular: float 

class character:

    id: int 
    steering: int 
    position: np.ndarray
    velocity: np.ndarray 
    initialOrientation: float 
    maxVelocity: float
    target: int 
    arrivalRadius: float 
    slowingRadius: float 
    timeTarget: float 
    linear: np.ndarray 

    def __init__(self, id, steering, positionX, positionZ, velocityX, velocityZ, initPosition, initOrientation, maxVel, maxAcc, target, arrivalRadius, slowingRadius, timeTarget):
        self.id = id
        self.steeringBehavior = steering
        self.initialPosition = initPosition
        self.position = np.vector(positionX, positionZ) 
        self.velocity = np.vector(velocityX, velocityZ) 
        self.initialOrientation = initOrientation
        self.maxVelocity = maxVel
        self.maxAcceleration = maxAcc
        self.target = target
        self.arrivalRadius = arrivalRadius
        self.slowingRadius = slowingRadius
        self.timeTarget = timeTarget

    def seek(self, target):
        
        result = steeringOutput()
        result.linear = target.initialPosition - self.initialPosition
        result.linear = vp.normalize(result.linear) 
        result.linear *= self.maxAcceleration

        if vp.normalize(self.maxVelocity) > 0:
            result.angular = math.atan2(-self.velocity[0], self.velocity[1])

        else:
            result.angular = 0
        
        return result 
    
    def arrive(self, target):

        result = steeringOutput() 
        direction = target.position - self.position 
        distance = vp.normalize(direction) 
        if distance < self.arrivalRadius:
            result.linear = vp.vector(0,0)
            result.angular = 0 
            return result 
        elif distance > self.slowingRadius:
            targetSpeed = self.maxVelocity 
        else:
            targetSpeed = self.maxVelocity * distance / self.slowingRadius

        targetVelocity = vp.normalize(direction) * targetSpeed 

        result.linear = targetVelocity - self.velocity 
        result.linear = result.linear / self.timeToTarget 

        if vp.normalize(result.linear) > self.maxAcceleration:
            result.linear = vp.normalize(result.linear) * self.maxAcceleration 
        
        result.angular = math.atan2(-self.velocity[0], self.velocity[1])

        return result 
           
        