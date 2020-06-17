import os, sys
import ctypes
import time
import multiprocessing

# # see http://msdn.microsoft.com/en-us/library/ms646260(VS.85).aspx for details
# ctypes.windll.user32.SetCursorPos(100, 20)
# ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
# ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

# Value	Meaning
# MOUSEEVENTF_ABSOLUTE
# 0x8000
# The dx and dy parameters contain normalized absolute coordinates. If not set, those parameters contain relative data: the change in position since the last reported position. This flag can be set, or not set, regardless of what kind of mouse or mouse-like device, if any, is connected to the system. For further information about relative mouse motion, see the following Remarks section.
# MOUSEEVENTF_LEFTDOWN
# 0x0002
# The left button is down.
# MOUSEEVENTF_LEFTUP
# 0x0004
# The left button is up.
# MOUSEEVENTF_MIDDLEDOWN
# 0x0020
# The middle button is down.
# MOUSEEVENTF_MIDDLEUP
# 0x0040
# The middle button is up.
# MOUSEEVENTF_MOVE
# 0x0001
# Movement occurred.
# MOUSEEVENTF_RIGHTDOWN
# 0x0008
# The right button is down.
# MOUSEEVENTF_RIGHTUP
# 0x0010
# The right button is up.
# MOUSEEVENTF_WHEEL
# 0x0800
# The wheel has been moved, if the mouse has a wheel. The amount of movement is specified in dwData
# MOUSEEVENTF_XDOWN
# 0x0080
# An X button was pressed.
# MOUSEEVENTF_XUP
# 0x0100
# An X button was released.
# MOUSEEVENTF_WHEEL
# 0x0800
# The wheel button is rotated.
# MOUSEEVENTF_HWHEEL
# 0x01000
# The wheel button is tilted.

MOUSEEVENTF_MOVE = 0x0001 # mouse move
MOUSEEVENTF_LEFTDOWN = 0x0002 # left button down
MOUSEEVENTF_LEFTUP = 0x0004 # left button up
MOUSEEVENTF_RIGHTDOWN = 0x0008 # right button down
MOUSEEVENTF_RIGHTUP = 0x0010 # right button up
MOUSEEVENTF_MIDDLEDOWN = 0x0020 # middle button down
MOUSEEVENTF_MIDDLEUP = 0x0040 # middle button up
MOUSEEVENTF_WHEEL = 0x0800 # wheel button rolled
MOUSEEVENTF_ABSOLUTE = 0x8000 # absolute move
SM_CXSCREEN = 0
SM_CYSCREEN = 1

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

def MouseListener():
    pos = POINT()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(pos))
    x = pos.x
    y = pos.y

    while True:
        time.sleep(10/1000)
        ctypes.windll.user32.GetCursorPos(ctypes.byref(pos))
        if x != pos.x or y != pos.y:
            x, y = pos.x, pos.y
            print(x,' , ', y)

    pass

def main():

    # p = multiprocessing.Process(target=MouseListener)
    # p.start()
    dx = 5
    dy = -5
    while True:
        dx *= -1
        dy *= -1
        ctypes.windll.user32.mouse_event(MOUSEEVENTF_MOVE, dx, dy, 0, 0)
        time.sleep(2)
        # ctypes.windll.user32.keybd_event(0x31, 0, 0, 0) # Key Down
        # ctypes.windll.user32.keybd_event(0x31, 0, 0x0002, 0) # Key Up

    # p.join()
    pass

if __name__ == "__main__":
    main()
    pass