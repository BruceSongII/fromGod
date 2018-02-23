#-*- coding: utf-8 -*-
import maya.cmds as rig
import maya.mel as MEL

def SK_createMotionTrail():
    MEL.eval('doMotionTrail 1 { "snapshot  -motionTrail 1  -increment 1 -startTime `playbackOptions -query -min` -endTime `playbackOptions -query -max`", "point", "0", "animCurve"};\
    doMotionTrail 1 { "snapshot  -motionTrail 1  -increment 1 -startTime `playbackOptions -query -min` -endTime `playbackOptions -query -max`", "line", "0", "animCurve"};')

def SK_MotionTrail(num):
    LfElbow = 'Lf_elbow_drv_jnt'
    RtElbow = 'Rt_elbow_drv_jnt'
    LfKnee = 'Lf_knee_drv_jnt'
    RtKnee = 'Rt_knee_drv_jnt'
    slJnt = ''
    
    if(1 == num):
        slJnt = LfElbow
    if(2 == num):
        slJnt = RtElbow
    if(3 == num):
        slJnt = LfKnee
    if(4 == num):
        slJnt = RtKnee
    
    selObj = rig.ls(sl = True)
    if selObj:
        jntObj = selObj[0]
        if ('nurbsCurve' == rig.nodeType(rig.listRelatives(jntObj,s = True)[0])):
            if(':' in jntObj):
                objSplit = jntObj.split(':')
                prefix = jntObj.replace(objSplit[-1],'')
                
                MidTrailJnt = prefix+slJnt
                if(rig.objExists(MidTrailJnt)):           
                    TrailJnt = rig.listConnections(MidTrailJnt+'.tx',s = False,d = True)[0]
                    snapShotJnts = rig.listConnections(TrailJnt+'.selectHandle',d = True,s = False,type = 'snapshot')
                    
                    if(snapShotJnts):
                        for SnapShot in snapShotJnts:
                            trailJnts = rig.listConnections(SnapShot,d = True,s = False,type = 'snapshotShape')
                            rig.delete(trailJnts)
        
                    rig.select(TrailJnt)
                    SK_createMotionTrail()
                    
                    trailSnapShot = rig.listConnections(TrailJnt+'.selectHandle',d = True,s = False,type = 'snapshot')[0]
                    TrailHandle = rig.listConnections(trailSnapShot,d = True,s = False,type = 'snapshotShape')[0]
                    rig.rename(TrailHandle,slJnt.replace('drv_jnt','motionTrail_Line'))
                    
                    trailSnapShot = rig.listConnections(TrailJnt+'.selectHandle',d = True,s = False,type = 'snapshot')[1]
                    TrailHandle = rig.listConnections(trailSnapShot,d = True,s = False,type = 'snapshotShape')[0]
                    rig.rename(TrailHandle,slJnt.replace('drv_jnt','motionTrail_Point'))
                    rig.select(selObj)
            
            else:
                TrailJnt = rig.listConnections(slJnt+'.tx',s = False,d = True)[0]
                rig.select(TrailJnt)
                SK_createMotionTrail()
                
                trailSnapShot = rig.listConnections(TrailJnt+'.selectHandle',d = True,s = False,type = 'snapshot')[0]
                TrailHandle = rig.listConnections(trailSnapShot,d = True,s = False,type = 'snapshotShape')[0]
                rig.rename(TrailHandle,slJnt.replace('drv_jnt','motionTrail_Line'))
                
                trailSnapShot = rig.listConnections(TrailJnt+'.selectHandle',d = True,s = False,type = 'snapshot')[1]
                TrailHandle = rig.listConnections(trailSnapShot,d = True,s = False,type = 'snapshotShape')[0]
                rig.rename(TrailHandle,slJnt.replace('drv_jnt','motionTrail_Point'))
                rig.select(selObj)    
        
