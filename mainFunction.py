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
import vectorOperations as vp
import characterAttributes as ca


#open and create trajectory file for character movement updates
trajectory = open("trajectories.txt", "w")

#initiliaze characters' list and attributes
CONT = 1

#Initialize time controls
time = 0
timeIncrement = 0.5
stopTime = 50

#character 1 = continue behavior
char1 = ca.init()
char1.id = 2601
char1.steering = 1
char1.position = 
#character 2 = flee 
#character 3 = seek
#character 4 = arrive

while time < stopTime:
    time += timeIncrement

    # Loop through list of characters
    for i in characters:
        # Call each steering behavior for character
        if i.
    #paste each update into end of txt file, end while













#End of Program