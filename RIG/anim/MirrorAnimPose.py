#-*- coding: utf-8 -*-
import maya.cmds as rig

allCtrls = rig.sets('bodySet',q = True)
LR = 'Lf'
for ctrl in allCtrls:
    if(LR in ctrl):
        ConRotate = rig.xform(ctrl,q = True,ro = True,ws = False)
        FindCon = ctrl.replace('Lf','Rt')
        if(FindCon):
            rig.xform(FindCon,ro = ConRotate,ws = False)