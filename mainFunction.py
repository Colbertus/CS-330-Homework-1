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
import movementAlgorithms
import vectorOperations

def main():

    #open and create trajectory file for character movement updates
    trajectory = open("trajectories.txt", "w")
    #Initialize initial conditions variables
    time = 0
    timeIncrement = 0.5
    stopTime = 100


    while time <= stopTime:
        time += timeIncrement
        #insert movement algorithm? insert continue afterwords?
        #paste each update into end of txt file, end while












    main()

#End of Program