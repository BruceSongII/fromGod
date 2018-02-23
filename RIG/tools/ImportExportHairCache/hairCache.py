#-*- coding: utf-8 -*-
from maya.cmds import *


class GenraterCurve():
    def __init__(self,inputType, slObjs):
        self.type = inputType#现在的类型
        self.selectObjs = slObjs
        self.allFollicles = []#所有毛囊
        
        
    def getAllFollicls(self):
        if self.selectObjs:
            for obj in self.selectObjs:
                self.getSingleFollicle(obj)
        else:
            return None
        
        
    def getSingleFollicle(self, obj):
        if 'mesh' == self.type:
            folSign = listConnections(obj, s = False, d = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'follicle' == self.type:
            self.allFollicles.extend(obj)
                
        elif 'pfxHair' == self.type:
            folSign = listConnections(obj, d = False, s = True, type = 'hairSystem')
            if folSign:
                for hs in folSign:
                    fols = listConnections(hs, d = Fasle, s = True, type = 'follicle')
                    if fols:
                        self.allFollicles.extend(fols)
                
        elif 'nurbsCurve' == self.type:
            folSign = listConnections(obj, s = False, d = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'hairSystem' == self.type:
            folSign = listConnections(obj, s = True, d = False, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
        elif 'nurbsSurface' == self.type:
            folSign = listConnections(obj, s = False, d = True, type = 'follicle')
            if folSign:
                self.allFollicles.extend(folSign)
                
                
                
    def createCurve(self):
        self.getAllFollicls()
        fols = self.allFollicles
        if fols:
            allFols = set(fols)
            for fol in allFols:
                print fol
    
    
    
    