#Colby McClure, Paige Smith
#
#Main Function
#
#what to do:
# TODO initialize variables and libraries
# TODO call movement algorithms and update at .5 increments NE-1 implementation
# TODO output movement to .txt file for plot check
# TODO paige: arrive and continue and functions
# variables to initialize: pos, vel, dir, acc, lin acc, timestep, subvariables for maxes

#import files to use in main function calls

from characterAttributes import character 
import characterAttributes as ca
import math


#open and create trajectory file for character movement updates
trajectory = open("trajectories.txt", "w")

#initiliaze characters' list and attributes
CONT = 1

#Initialize time controls
time = 0
timeIncrement = 0.5
stopTime = 50

# TODO: Create an instance of each character 
#character 1 = continue behavior
char1 = character(2601, ca.CONTINUE, 0, 0, 0, 0, 0, 0, 0, 0, 0)
char2 = character(2602, ca.FLEE, -30, -50, 2, 7, (math.pi / 4), 8, 1.5, 0, 0)
char3 = character(2603, ca.SEEK, -50, 40, 0, 8, ((3 * math.pi) / 2), 8, 2, 0, 0)
char4 = character(2604, ca.ARRIVE, 50, 75, -9, 4, math.pi, 10, 2, 0, 4)


while time < stopTime:
    time += timeIncrement

    # Loop through list of characters
    for i in characters:
        # Call each steering behavior for character
    #paste each update into end of txt file, end while













#End of Program
    