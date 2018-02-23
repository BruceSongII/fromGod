#-*- coding: utf-8 -*-
import sys





rigPath = 'E:/rigging'
rigSyspath = sys.path

if rigPath in rigSyspath:
    pass
else:
    sys.path.append(rigPath)

import RIG   
from RIG.rigUI_00 import *
SK_RigUI()



