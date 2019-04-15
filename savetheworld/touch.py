from functools import partial
from touchphat import *

_status = [False]*6
_names = ["BACK","A","B","C","D","ENTER"]

def _pressed(pad):
    global _status
    _status[pad] = True
    
def _released(pad):
    global _status
    _status[pad] = False
    
def touched(pad):
    """Returns True if the pad is touched
    Pad can be a number (0-5), a name ("BACK","A","B","C","D","ENTER"),
    or "ANY" (in which case it returns true if any pad is touched)"""
    if str(pad).upper()=="ANY":
        return any(_status)
    try:
        index = int(pad)
    except ValueError:
        try:
            index = _names.index(str(pad).upper())
        except ValueError:
            raise ValueError("{} is not the name of a pad".format(pad))
    return _status[index]
            
for i in range(6):
    on_touch(i+1, partial(_pressed, i))
    on_release(i+1, partial(_released, i))
        
