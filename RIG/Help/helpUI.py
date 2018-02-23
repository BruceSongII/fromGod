#-*- coding: utf-8 -*-
import maya.mel as mel
import maya.cmds as rig


def SK_helptUI():
    IDMTRigGUI='HelpUIWindow'
    if rig.window(IDMTRigGUI,exists=True):
        rig.deleteUI(IDMTRigGUI)
    rig.window(IDMTRigGUI,title= u'选择你所需要的帮助',menuBar=True,wh=  (300,80),minimizeButton=True,maximizeButton=True)
    rig.columnLayout()
    rig.button(l = u'表情',w = 295,c = "SK_openHelpDoc('face')")
    rig.button(l = u'身体',w = 295,c = "SK_openHelpDoc('body')")
    
    rig.separator(w = 325,h=5,style='in')
    rig.separator(w = 325,h=5,style='in')
    rig.rowColumnLayout(nc = 2,columnWidth = [(1,147),(2,147)])
    rig.button(l = u'WXTV',c = "SK_openHelpDoc('WXTV')")
    rig.button(l = u'RR',c = "SK_openHelpDoc('RR')")
    
    rig.window(IDMTRigGUI,e=True,wh=(305,310))
    rig.showWindow(IDMTRigGUI)  
    
def SK_openHelpDoc(project):
    mainPath = 'Z:/Resource/Groups/Production/Modeling/Rigging 2009 Development Plan/document/'
    if 'face' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'body' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'WXTV' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
    
    if 'RR' == project:
        mel.eval("system(\"load"+mainPath+project+"\")")
        
