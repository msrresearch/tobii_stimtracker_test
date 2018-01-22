from pygaze import libscreen, eyetracker
import time
import argparse

parser = argparse.ArgumentParser(description='A small test for pygaze using tobii eyetracker')
parser.add_argument('-c', '--no_calibrate', default=False, action='store_true', help='skip calibration')
args = parser.parse_args()

display = libscreen.Display()
screen = libscreen.Screen()
eyetracker = eyetracker.EyeTracker(display)

if not args.no_calibrate:
    eyetracker.calibrate()

eyetracker.start_recording()

black = False

for i in range (10, 0, -1):
    if black:
        screen = libscreen.Screen(bgc='black')
        screen.draw_text('Recording data for {} seconds'.format(i), fontsize=30, colour=(255,255,255))
    else:
        screen = libscreen.Screen(bgc='white')
        screen.draw_text('Recording data for {} seconds'.format(i), fontsize=30, colour=(0,0,0))
    display.fill(screen)
    display.show()
    black = not black
    time.sleep(1)

eyetracker.stop_recording()

display.close()
