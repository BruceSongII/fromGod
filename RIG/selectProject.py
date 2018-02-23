#-*- coding: utf-8 -*-

import maya.cmds as rig
from RIG.face.baseClass import *
from RIG.face.controlers import CreateControler
from RIG.commonly.resetControllerDefaultPose import SK_creatConDefaultPos

def SK_SelectProject(OrigenRB,WoodliesRB,WinxTVRB):
    if rig.radioButton(OrigenRB,q = True,sl = True):
        SK_Default_config()
    elif rig.radioButton(WoodliesRB,q = True,sl = True):
        SK_Woodlies_config()
    elif rig.radioButton(WinxTVRB,q = True,sl = True):
        SK_WinxTV_config()

#===============================================================================
# 增加脚趾驱动关键帧    
#===============================================================================
def SK_AddToesetDrivenKeyframe():
    unLock = unLockAttr(False,False,False)
    Lock = LockHideAttr(False,False,False)

    footJnts = rig.ls('*_foot_drv')
    handJnts = rig.ls('*_hand_drv')
    footJnts.extend(handJnts)#增加手指驱动
    for jnt in footJnts:
        allCons = rig.listConnections(jnt+'.ctrl',s = False,d = True)#得到所有脚趾控制器
        mainCtrls = []
        if allCons:#脚趾是否有控制器
            for con in allCons:#找到脚趾的第一个控制器
                if(con[-1] == '1'):
                    mainCtrls.append(con)
        
        if mainCtrls:#是否存在脚趾控制器
            for mainCon in mainCtrls:#迭代脚趾的第一个控制器
                conPre = mainCon.replace(mainCon[-1],'')#得到脚趾的前缀，注意：不能超过10根脚趾
                relativeCons = [con for con in allCons if conPre in con]#得到脚趾的个数
                if relativeCons:
                    rig.addAttr(mainCon,at = 'float',ln = 'curl',min = -10,max = 10,dv = 0,k = True)#增加脚趾弯曲属性
                    
                    for con in relativeCons:
                        con_low = rig.listRelatives(con,p = True)[0]#得到此控制器上的组
                        unLock.unLockObj(con_low)#解开属性
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = 0,v = 0)#增加驱动关键帧
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = 10,v = -90)#增加驱动关键帧
                        rig.setDrivenKeyframe(con_low+'.rotateZ',currentDriver = mainCon+'.curl',dv = -10,v = 90)#增加驱动关键帧
                        Lock.hideAndLockObj(con_low)#锁定属性           
 
 
 
 
def SK_IKHandPivot():
    Lock = LockHideAttr(True,True,False,False)
    newcons = CreateControler()
    handIK = rig.ls('*Arm_Wrist_IK')
    
    if handIK:
        for ikcon in handIK:
            #增加旋转属性
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRX',k = True)
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRY',k = True)
            rig.addAttr(ikcon,at = 'float',ln = 'pivotIKRZ',k = True)
            
            
            val = rig.getAttr(ikcon+'.scaleVal')#获得缩放值
            newcons.setObjScale((val,val,val))
            con = newcons.SK_b01(ikcon+'_Pivot')
            jointFinger = ikcon[0:2]+'_mid2_jnt'#手指骨骼
            pos = rig.xform(jointFinger,q = True,t = True,ws = True)#旋转轴心点位置
            rig.xform(con,t = pos,ws = True)
            
            ikConChild = rig.listRelatives(ikcon,c = True,type = 'transform')#获得IK控制器下的物体
            
            rig.parent(con,ikcon)
            rig.makeIdentity(con,apply = True,t = True,s = True,r = True)
            rig.parent(ikConChild,con)  
            
            Switch = ikcon[0:2]+'Arm_Switch'
            rig.addAttr(Switch,at = 'enum',ln = 'pivotIK',en = 'OFF:ON:',k = False)
            rig.connectAttr(Switch+'.pivotIK',con+'.visibility')
            Lock.hideAndLockObj(con) 
            
            #连接旋转属性
            rig.connectAttr(ikcon+'.pivotIKRX',con+'.rx')
            rig.connectAttr(ikcon+'.pivotIKRY',con+'.ry')
            rig.connectAttr(ikcon+'.pivotIKRZ',con+'.rz')
            
#===============================================================================
# 选择配置
#===============================================================================
#缺省配置
def SK_Default_config():

    print 'Default'

#Woodlies项目配置    
def SK_Woodlies_config():
    
    SK_AddToesetDrivenKeyframe()
    SK_IKHandPivot()
    SK_creatConDefaultPos()#创建恢复初始pose
    
    

#WinxTV项目配置  
def SK_WinxTV_config():
    print 'WinTV'
    
    