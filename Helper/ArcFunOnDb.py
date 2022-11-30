import arcpy
import os
from arcpy import  env


class ArcFuncOnDb:
    def __init__(self,dbpath):
        self.dbpath=dbpath

    def Clip(self,ShpIN,ShpOut,ShpCliper):
        env.workspace=self.dbpath
        ShpOut=self.dbpath+"\\"+ShpOut
        arcpy.Clip_analysis(ShpIN.holepath,ShpCliper.holepath,ShpOut,"")

    def CreatDatasets(self,Setname):
        env.workspace=self.dbpath
        arcpy.CreateFeatureDataset_management(self.dbpath,Setname)



    #def GetAreaTotal(self,Shp):



