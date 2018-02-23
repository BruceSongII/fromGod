#-*- coding: utf-8 -*-
import sys

execfile('C:/Documents and Settings/tianwenwu/maya_py/windows/refresh.py')

rigPath = 'C:/Documents and Settings/tianwenwu/maya_py/src'
rigSyspath = sys.path

if rigPath in rigSyspath:
    pass
else:
    sys.path.append(rigPath)

import RIG   
from RIG.anim.IKFollowSwitch import SK_followToSwitch
from RIG.anim.motionTrailDisplay import SK_MotionTrail
from RIG.IKFK import SK_IKFKSwitchCommand

