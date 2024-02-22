#Colby McClure, Paige Smith
#
#Main Function

# variables to initialize: pos, vel, dir, acc, lin acc, timestep, subvariables for maxes

#import files to use in main function calls

from characterAttributes import character 
import characterAttributes as ca
import math


#open and create trajectory file for character movement updates
trajectory = open("trajectories.txt", "w")

#Initialize time controls
time = 0
timeIncrement = 0.5
stopTime = 50

#character 1 = continue behavior
char1 = character(2601, ca.CONTINUE, 0, 0, 0, 0, 0, 0, 0, 0, 0)
char2 = character(2602, ca.FLEE, -30, -50, 2, 7, (math.pi / 4), 8, 1.5, 0, 0)
char3 = character(2603, ca.SEEK, -50, 40, 0, 8, ((3 * math.pi) / 2), 8, 2, 0, 0)
char4 = character(2604, ca.ARRIVE, 50, 75, -9, 4, math.pi, 10, 2, 0, 4)

characters = [char1, char2, char3, char4]

#print start values
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

          

while time < stopTime:
    time += timeIncrement

    # Loop through list of characters
    for p in characters:
        # Select and call a steering behavior.
        if p.steering == ca.CONTINUE:
            steering = p.continueFunc()
        elif p.steering == ca.SEEK:
            steering = p.seek(characters[0])
        elif p.steering == ca.FLEE:
            steering = p.flee(characters[0])
        elif p.steering == ca.ARRIVE:
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
              str(p.orientation),
              str(p.steering),
              "FALSE",
              sep=',', file = trajectory)      
trajectory.close()
        # Call each steering behavior for character
    #paste each update into end of txt file, end while













#End of Program
    