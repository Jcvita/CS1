"""
jertle.py
YOUR DESCRIPTION AND NAME HERE
"""

# Notice that this program runs as is.
# It does not do anything, but that's OK.
# As you add functionality, add test functions that you call
#   instead of the main function.
# Then run main when you are ready to try some things in normal operation.
# (Remove this block of comments before submission.)

import sys
import time
import turtle

# Turtle Canvas Window Setup ######
                                  #
WORLD_SIZE = 300                  #
MARGIN = 10                       #
WINDOW_SIZE = WORLD_SIZE + MARGIN #
                                  #
###################################

SLEEP_TIME = 5

# The Set of Jertle Commands #####################################
                                                                 #
PENDOWN_CMD = "!1"  # No parameters                              #
PENUP_CMD = "!0"    # No parameters                              #
TURN_CMD = "o^"     # Parameter: angle, to the left, in degrees  #
FORWARD_CMD = "->"  # Parameter: number of units to move         #
CIRCLE_CMD = "()"   # Parameter: radius of circle                #
                                                                 #
##################################################################

### PRE-DEFINED ERROR CODES ###################################
                                                              #
ILLEGAL_COMMAND = 1  # Unrecognized command string            #
MISSING_ARGUMENT = 2 # More arguments needed for this command #
NO_ARG_END = 3       # Can't find the matching closing brace  #
                                                              #
###############################################################
def locate_beginning_of_arg(str):
    for x in range(len(str)):
        if str[x] == '{':
            return x


def locate_end_of_arg(str):
    for x in range(len(str)):
        if str[x] == '}':
            return x



def interpret(program):
    while len(program) > 0:
        if locate_end_of_arg(program) < locate_beginning_of_arg(program):
            error("Missing opening brace for argument", 1)
        else:
            program = program[locate_end_of_arg(program) + 1:]9


    while len(program) > 0:
        if program[0:2] == FORWARD_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            turtle.forward(num)
            program = program[x + 1:]
        elif program[0:2] == TURN_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            program = program[x + 1:]
        elif program[0:2] == CIRCLE_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            program = program[x + 1:]
        elif program[0:2] == PENDOWN_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            program = program[x + 1:]
        elif program[0:2] == PENUP_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            program = program[x + 1:]
        else:
            error("Illegal Command '{}'".format(program[0:2]), 1)
def error( msg, e_code ):
    """
    A fatal error has occurred.
    Print an error message and end the program.
    :param msg: the string message to print before ending the program
    :param e_code: the integer error code with which the program exits
    """
    print( msg, file=sys.stderr )
    sys.exit( e_code )


def initialize():
    """
    Set up the turtle world.
    :return: None
    """
    turtle.setup( WINDOW_SIZE, WINDOW_SIZE )
    turtle.setworldcoordinates( -MARGIN, -MARGIN, WORLD_SIZE, WORLD_SIZE )

def main():
    """
    Read Jertle program strings from a file and execute them.
    The file is provided by the user when this program runs.
    Stop when end of file is reached.
    :return: None
    """
    initialize()
    file = open(input("Jertle file? "))
    interpret(file)
    turtle.done()

if __name__ == "__main__":
    main()
