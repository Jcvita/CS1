"""
jertle.py
Joseph Vita

jertle.py takes in a text file written in jertle and translates it to turtle
commands. it detects various errors that can happen in jertle and throws errors
accordingly.
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


def contains(str, char):
    isin = False
    for x in range(len(str)):
        if str[x] == char:
            isin = True
    return isin


def locate_beginning_of_arg(str):
    if contains(str, '{'):
        for x in range(len(str)):
            if str[x] == '{':
                return x
    else:
        return -1


def locate_end_of_arg(str):
    if contains(str, '}'):
        for x in range(len(str)):
            if str[x] == '}':
                return x
    else:
        return -1


def interpret(program):
    """
    translates jertle text file chosen by the user. also throws 1 of 3 errors
    based on turtle syntax errors.

    precondition:file is selected
    precondition:turtle is set to a desired position

    :param program:
    :return:
    """
    split = program.split('\n')
    program = ''
    for line in split:
        program += line

    print (program)
    program_backup = program
    while len(program) > 0:
        if locate_end_of_arg(program) < locate_beginning_of_arg(program):
            error("Missing opening brace for argument", 2)
        else:
            program = program[locate_end_of_arg(program) + 1:]

    program = program_backup

    last = ''
    while len(program) > 0:
        if locate_beginning_of_arg(program) == -1 or \
            locate_end_of_arg(program) == -1:
            break
        elif last == '{' and locate_beginning_of_arg(program) < locate_end_of_arg(program):
            error("Can't find matching closing brace", 3)
        elif locate_beginning_of_arg(program) < locate_end_of_arg(program):
            last = '{'
            program = program[locate_beginning_of_arg(program) + 1:]
            # print(last)
        elif locate_beginning_of_arg(program) > locate_end_of_arg(program):
            last = '}'
            program = program[locate_end_of_arg(program) + 1:]
            # print(last)


    program = program_backup

    while len(program) > 0:
        if program[0:locate_beginning_of_arg(program)] == FORWARD_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            turtle.forward(int(float(num)))
            program = program[x + 1:]
        elif program[0:locate_beginning_of_arg(program)] == TURN_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            turtle.left(int(float(num)))
            program = program[x + 1:]
        elif program[0:locate_beginning_of_arg(program)] == CIRCLE_CMD:
            x = locate_end_of_arg(program)
            num = program[3:x]
            turtle.circle(int(float(num)))
            program = program[x + 1:]
        elif program[0:2] == PENDOWN_CMD:
            x = locate_end_of_arg(program)
            turtle.pendown()
            program = program[x + 1:]
        elif program[0:2] == PENUP_CMD:
            x = locate_end_of_arg(program)
            turtle.penup()
            program = program[x + 1:]
        else:
            error("Illegal Command '{}'".format(
                program[0:locate_beginning_of_arg(program)]), 1)


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
    file = input("Jertle file? ")
    file = open(file)
    interpret(file.read())
    turtle.done()
    time.sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
