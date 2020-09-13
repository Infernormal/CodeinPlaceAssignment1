from karel.stanfordkarel import * 

"""Karel finds a midpoint in any world
Pre: Karel starts at the first row of the first column facing east
Post: Karel puts beeper in the center of first row or in one of two center squares
 (depending on width of the world)
"""

def main():
    #to solve 1*1 world issue
    if front_is_blocked():
        put_beeper()
    #for all other scenarios
    else:
        make_the_row()
        turn_around()
        for i in range(2):
            sweep_the_corner()
        while beepers_present():
            sweep_the_row()
    #to solve fencepost error
        recenter()

"""Fills the row with beepers"""
def make_the_row():
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()

"""Returns one square back and marks the center"""
def recenter():
    turn_around()
    move()
    put_beeper()

"""Turns 180 degrees"""
def turn_around():
    for i in range(2):
        turn_left()

"""Picks beepers in the corner"""
def sweep_the_corner():
    while front_is_clear():
        move()
    turn_around()
    pick_beeper()
    move()

"""Takes the last beeper in the row, turns around and takes the last beeper
in the row on the other side"""
def sweep_the_row():
    while beepers_present():
        move()
    turn_around()
    move()
    pick_beeper()
    move()

if __name__ == "__main__":
    run_karel_program()
