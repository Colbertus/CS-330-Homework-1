
#Colby McClure, Paige Smith
# File contains the character attributes class, steering output class
# Character class:
# Attributes contained:
#   Id, steering behavior, initial position, initial velocity, initial orientation, 
#   max velocity, max acceleration, target, arrival radius, slowing radius, time to target
# Methods contained:
#   seek, arrive, flee, continue
#
# Steering Output class:
# Attributes contained:
#   linear, angular acceleration
#

# imports for libraries to use within methods
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
    initPosition: float
    initOrientation: float 
    maxVel: float
    maxAcc: float
    target: int 
    arrivalRadius: float 
    slowingRadius: float 
    timeTarget: float 
    linear: np.ndarray 
# TODO figure out why vector operations are not importing properly
# TODO change variable names to match our class attributes names
    def __init__(self, id, steering, positionX, positionZ, velocityX, velocityZ, 
        initPosition, initOrientation, maxVel, maxAcc, target, arrivalRadius, slowingRadius, 
        timeTarget):

        self.id = id
        self.steeringBehavior = steering
        self.initPosition = initPosition
        self.position = np.vector(positionX, positionZ) 
        self.velocity = np.vector(velocityX, velocityZ) 
        self.initOrientation = initOrientation
        self.maxVel = maxVel
        self.maxAcc = maxAcc
        self.target = target
        self.arrivalRadius = arrivalRadius
        self.slowingRadius = slowingRadius
        self.timeTarget = timeTarget

    # Function: Seek
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to move directly toward the target's position
    #   by accelerating at max rate up to the max character speed
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
    
    # Function: Arrive
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to arrive at target without overshooting target by
    #   adjusting the character's speed as it moves closer to the target
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
    # TODO add continue and flee algorithms

    # Function: Flee
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to run directly away from the target by finding the 
    #   direction to the target and accelerating opposite of that

    # Function: Continue
           
        