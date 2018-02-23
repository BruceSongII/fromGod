#-*- coding: utf-8 -*-
import maya.cmds as rig

def SK_followToAuto(obj,num):
    pos = rig.xform(obj,q = True,t = True,ws = True)
    rig.setAttr(obj+'.follow',num)
    rig.xform(obj,t = pos,ws = True)

def SK_followToSwitch(num):
    selObjs = rig.ls(sl = True)
    if(selObjs):
        for switchObj in selObjs:      
            objNurbs = switchObj
            nurbsCurve = rig.listRelatives(objNurbs,s = True)
            if(nurbsCurve):
                if('nurbsCurve' == rig.nodeType(nurbsCurve[0]) and rig.attributeQuery('ctrl',node = objNurbs,ex = True)):
                    if ('_IKFK_blendCon' in rig.connectionInfo(objNurbs+'.ctrl', sfd=True)):
                        if ('_Pole_ctrl' in objNurbs):
                            SK_followToAuto(objNurbs,num)
                            


