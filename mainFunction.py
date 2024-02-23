'''
Authors: Colby McClure, Paige Smith
File: mainFunction.py
Assignment: CS 330 Program 1
Date: 2/23/24
Purpose: TODO: Fill in purpose of the program

'''

# Main Function

# Needed imports for the program
from numpy import pi
import numpy as np
import math

def vector(x, z):

    return np.array([x, z])

def normalize(self):
    return self / np.linalg.norm(self, ord=2)

def length(self):
    return np.linalg.norm(self, ord=2)

class steeringOutput:
    linear : np.ndarray
    angular: float 

class character:

    id: int 
    steering: int 
    position: np.ndarray
    velocity: np.ndarray 
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
        self.position = vector(positionXInit, positionZInit) 
        self.velocity = vector(velocityX, velocityZ) 
        self.initOrientation = initOrientation
        self.maxVel = maxVel
        self.maxAcc = maxAcc
        self.target = target
        self.arrivalRadius = arrivalRadius
        self.slowingRadius = slowingRadius
        self.timeTarget = timeTarget
        self.linear = vector(0, 0)
        self.rotation = 0

    # Function: Seek
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to move directly toward the target's position
    #   by accelerating at max rate up to the max character speed
    def seek(self, target):
        
        result = steeringOutput()
        result.linear = target.position - self.position
        result.linear = normalize(result.linear) 
        result.linear = result.linear * self.maxAcc
        

        if length(self.velocity) > 0:
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
        distance = length(direction) 
        if distance < self.arrivalRadius:
            result.linear = vector(0,0)
            result.angular = 0 
            return result 
        
        elif distance > self.slowingRadius:
            targetSpeed = self.maxVel 

        else:
            targetSpeed = self.maxVel * distance / self.slowingRadius

        targetVelocity = normalize(direction) * targetSpeed 

        result.linear = targetVelocity - self.velocity 
        result.linear = result.linear / self.timeTarget 

        if length(result.linear) > self.maxAcc:
            result.linear = normalize(result.linear) * self.maxAcc 
        
        result.angular = math.atan2(-self.velocity[0], self.velocity[1])

        return result 

    # Function: Flee
    #   This function takes in the current character attributes and target attributes
    #   and sets the behavior to run directly away from the target by finding the 
    #   direction to the target and accelerating opposite of that
    def flee(self, target): 
        result = steeringOutput()
        result.linear = self.position - target.position
        result.linear = normalize(result.linear) 
        result.linear *= self.maxAcc
    
        if length(self.velocity) > 0:
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
        self.position = self.position + (self.velocity * timeIncrement)
        self.initOrientation = self.initOrientation + (self.rotation * timeIncrement)
        self.initOrientation = self.initOrientation / (2 * pi)

        # and the velocity 
        self.velocity = self.velocity + (steering.linear * timeIncrement)
        self.rotation = self.rotation + (steering.angular * timeIncrement)
    
        
        #calculate Angular
        self.linear = vector(math.cos(steering.angular), math.sin(steering.angular))
   
        # Check for speed above the max and clip
        if length(self.velocity) > self.maxVel:
            self.velocity = normalize(self.velocity) * self.maxVel
    


CONTINUE = 1 
SEEK = 6
FLEE = 7
ARRIVE = 8
        
#open and create trajectory file for character movement updates
trajectory = open("trajectories.txt", "w")

#Initialize time controls
time = 0
stopTime = 50
timeIncrement = 0.5


char1 = character(2601, CONTINUE, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
char2 = character(2602, FLEE, -30, -50, 2, 7, (pi / 4), 8, 1.5, 1, 0, 0, 0)
char3 = character(2603, SEEK, -50, 40, 0, 8, ((3 * pi) / 2), 8, 2, 1, 0, 0, 0)
char4 = character(2604, ARRIVE, 50, 75, -9, 4, pi, 10, 2, 1, 4, 32, 1)

characters = [char1, char2, char3, char4]

for p in characters:
    print(str(time), str(p.id),
          str(p.position[0]),
          str(p.position[1]),
          str(p.velocity[0]),
          str(p.velocity[1]),
          str(p.linear[0]),
          str(p.linear[1]),
          str(p.initOrientation),
          str(p.steering),
          "FALSE",
          sep=',', file=trajectory)

          

while time < stopTime:
    time += timeIncrement

    # Loop through list of characters
    for p in characters:
        # Select and call a steering behavior.
        if p.steering == CONTINUE:
            steering = p.continueFunc()
        elif p.steering == SEEK:
            steering = p.seek(characters[0])
        elif p.steering == FLEE:
            steering = p.flee(characters[0])
        elif p.steering == ARRIVE:
            steering = p.arrive(characters[0])
        p.update(steering)

    # print values each time step
    for p in characters:
        print(str(time),str(p.id),
              str(p.position[0]),
              str(p.position[1]),
              str(p.velocity[0]),
              str(p.velocity[1]),
              str(p.linear[0]),
              str(p.linear[1]),
              str(p.initOrientation),
              str(p.steering),
              "FALSE",
              sep=',', file = trajectory)      
trajectory.close()
        # Call each steering behavior for character
    #paste each update into end of txt file, end while













#End of Program
    