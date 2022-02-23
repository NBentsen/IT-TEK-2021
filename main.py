import sendingdata
import _thread
import Joystick

_thread.start_new_thread(Joystick.Joystick1x,())
_thread.start_new_thread(Joystick.Joystick1y,())
_thread.start_new_thread(Joystick.Joystick1b,())
# _thread.start_new_thread(Joystick.Joystick2x,())
# _thread.start_new_thread(Joystick.Joystick2y,())
# _thread.start_new_thread(Joystick.Joystick2b,())