
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
from vectorOperations import vector 
import numpy as np
import math 
import mainFunction as mf


CONTINUE = 1
SEEK = 6
FLEE = 7
ARRIVE = 8  



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

    def __init__(self, id, steering, positionXInit, positionZInit, velocityX, velocityZ, 
        initOrientation, maxVel, maxAcc, target, arrivalRadius, slowingRadius, 
        timeTarget):

        self.id = id
        self.steering = steering
        self.initPosition = vector(positionXInit, positionZInit) 
        self.velocity = vector(velocityX, velocityZ) 
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
        result.linear = target.initPosition - self.initPosition
        result.linear = vector.normalize(result.linear) 
        result.linear *= self.maxAcc

        if vector.normalize(self.maxVel) > 0:
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
        #TODO fix target.position
        direction = target.position - self.position 
        distance = vector.normalize(direction) 
        if distance < self.arrivalRadius:
            result.linear = vp.vector(0,0)
            result.angular = 0 
            return result 
        
        elif distance > self.slowingRadius:
            targetSpeed = self.maxVel 

        else:
            targetSpeed = self.maxVel * distance / self.slowingRadius

        targetVelocity = vector.normalize(direction) * targetSpeed 

        result.linear = targetVelocity - self.velocity 
        result.linear = result.linear / self.timeTarget 

        if vector.normalize(result.linear) > self.maxAcc:
            result.linear = vector.normalize(result.linear) * self.maxAcc 
        
        result.angular = math.atan2(-self.velocity[0], self.velocity[1])

        return result 

    # Function: Flee
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to run directly away from the target by finding the 
    #   direction to the target and accelerating opposite of that
    def flee(self, target): 
        result = steeringOutput()
        result.linear = self.position - target.position
        result.linear = vector.normalize(result.linear) 
        result.linear *= self.maxAcc
        #TODO fix target.position 
        if vector.normalize(self.maxVel) > 0:
            result.angular = math.atan2(-self.velocity[0], self.velocity[1])

        else:
            result.angular = 0

        return result

    # Function: Continue
    def continueFunc(self):
        result = steeringOutput()
        result.linear = self.velocity
        result.angular = 0
        return result
    
    # Function: Update
    def update(self, steering: steeringOutput):
        
        # Update the position and orientation
        # Face in the direction we want to move
        self.position = self.position + (self.velocity * mf.timeIncrement)
        self.orientation = self.orientation + (self.rotation * mf.timeIncrement)
        self.orientation = self.orientation / (2 * math.pi)

        # and the velocity and rotation
        self.velocity = self.velocity + (steering.linear * mf.timeIncrement)
        self.rotation = self.rotation + (steering.angular * mf.timeIncrement)

        #calculate Angular
        #self.linear = vector(math.cos(steering.angular), math.sin(steering.angular))
   

        # Check for speed above the max and clip
        if vector.normalize(self.velocity) > self.maxVel:
            self.velocity = vector.normalize(self.velocity) * self.maxVel
        