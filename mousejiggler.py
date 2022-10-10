#!python

import ctypes
from ctypes import *
from ctypes import wintypes
from time import sleep

'''
mouse_event API documentation:
https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-mouse_event
'''
def mouse_event():
    ctypes.windll.user32.mouse_event(
        MOUSEEVENTF_MOVE,\
        0,\
        0,\
        0,\
        0\
        )

'''
SendInput API documentation:
https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-sendinput
'''
def SendFakeInput():
    fake_input = INPUT()
    fake_input.type = INPUT_MOUSE
    fake_input.mi = MOUSEINPUT(\
        0,\
        0,\
        0,\
        MOUSEEVENTF_MOVE,\
        0,\
        None
        )

    # SendInput
    ctypes.windll.user32.SendInput(
        1,\
        byref(fake_input),\
        sizeof(INPUT)
        )

'''
MOUSE INPUT
https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-mouseinput
'''
class MOUSEINPUT(Structure):
    _fields_ = [('dx',wintypes.LONG),\
                ('dy',wintypes.LONG),\
                ('mouseData',wintypes.DWORD),\
                ('dwFlags',wintypes.DWORD),\
                ('time',wintypes.DWORD),\
                ('dwExtraInfo',wintypes.PULONG),\
                ]

MOUSEEVENTF_MOVE = 0x0001

'''
INPUT
https://learn.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-input
'''
INPUT_MOUSE     = 0

class INPUT(Structure):
    _fields_ = [('type',wintypes.DWORD),\
                ('mi',MOUSEINPUT)]

'''
MAIN
'''
try:
    # Wait forever
    while True:
        SendFakeInput()
        sleep(1)

except KeyboardInterrupt:
    print("Your mouse can rest now",end='')
else:
    raise e
