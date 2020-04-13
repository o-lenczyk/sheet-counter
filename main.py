import curses
import pyfiglet
import time

screen = curses.initscr()

banner = pyfiglet.figlet_format("Sheeet", font = "5lineoblique" )

d1,d2,d3,d4,d5,d6,d7,d8,d9,d10=0,1,0,0,0,0,0,0,0,0
k=0
d5=1
screen.nodelay(1)

def formatted(number):
    if number < 10000000:
        return "{:,}".format(number).replace(',',' ').rjust(9)
    else:
        return "{:.2e}".format(number)

while (k!=ord('q')):
    d9+=d10
    d8+=d9
    d7+=d8
    d6+=d7
    d5+=d6
    d4+=d5
    d3+=d4
    d2+=d3
    d1+=d2

    screen.addstr(0,0, banner)

    screen.addstr(10, 0, "1st dim:  "+formatted(d1))
    screen.addstr(11, 0, "2nd dim:  "+formatted(d2))
    screen.addstr(12, 0, "3rd dim:  "+formatted(d3))
    screen.addstr(13, 0, "4th dim:  "+formatted(d4))
    screen.addstr(14, 0, "5th dim:  "+formatted(d5))
    screen.addstr(15, 0, "6th dim:  "+formatted(d6))
    screen.addstr(16, 0, "7th dim:  "+formatted(d7))
    screen.addstr(17, 0, "8th dim:  "+formatted(d8))
    screen.addstr(18, 0, "9th dim:  "+formatted(d9))
    screen.addstr(19, 0, "10th dim: "+formatted(d10))
    time.sleep(0.01)
    k=screen.getch()
    
curses.endwin()
