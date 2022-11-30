import math

from Helper.ArcFunOnDb import ArcFuncOnDb
import DataModel
import arcpy
from  tqdm import tqdm
import time
from Helper.ArcFunOnDb import ArcFuncOnDb
import DataModel

def CountTest(Blockshp,ContShp,blockId):
    Blockshp.AddField("Ave_Ab","double")
    rows = arcpy.UpdateCursor(Blockshp.holepath,sort_fields=blockId+" A")
    for row in tqdm(rows):
        id=row.getValue(blockId)
        sca=ContShp.getSumCouAvebyId("Shape_Area", blockId, id)
        print  id
        if(sca[1]!=0):
            row.setValue("Ave_Ab",sca[0]/sca[1])
        else:
            row.setValue("Ave_Ab",0)
        rows.updateRow(row)
        time.sleep(0.1)


def Count_AveAb(ContShp,blockId,Id):
        sca=ContShp.getSumCouAvebyId("Shape_Area", blockId, Id)
        if(sca[1]!=0):
            return sca[0]/sca[1]
        else:
            return 0

def Count_PerAb(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAvebyId("Shape_Area", blockId, Id)
    if (BlockArea!= 0):
        return sca[0] / BlockArea
    else:
        return 0

def Count_MaxAb(ContShp,blockId,Id,BlockArea):
    max = ContShp.getMacbyId("Shape_Area", blockId, Id)
    if (BlockArea != 0):
        return max / BlockArea
    else:
        return 0

def Count_AveHb(ContShp,blockId,Id):
        sca=ContShp.getSumCouAvebyId("floor", blockId, Id)
        if(sca[1]!=0):
            return sca[0]*3/sca[1]
        else:
            return 0

def Count_StdHb(ContShp,blockId,Id):
        std=ContShp.getSquareDecbyId("floor", blockId, Id)
        return 3*std

def Count_AveSb(ContShp,blockId,Id):
        nc=ContShp.getTwoElm("Shape_Area","floor",blockId,Id)
        pi=[]
        for i in range(0,len(nc[0])):
            #print nc[0][i],nc[1][i]
            pi.append(float(nc[0][i])/float(nc[1][i]))
        if(nc[2]==0):
            return 0
        return math.fsum(pi)/nc[2]

def Count_StdSb(ContShp,blockId,Id):
        nc=ContShp.getTwoElm("Shape_Area","floor",blockId,Id)
        pi=[]
        for i in range(0,len(nc[0])):
            pi.append(nc[0][i]/nc[1][i])
        if(len(pi)==0):
            return 0
        return math.sqrt(sum([(float(x)-math.fsum(pi)/len(pi) )** 2 for x in pi]) / len(pi))

def Count_Denb(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAvebyId("Shape_Area", blockId, Id)
    if (BlockArea!= 0):
        return sca[1] / BlockArea
    else:
        return 0

def Count_Denf(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAvebyId("code", blockId, Id)
    if (BlockArea!= 0):
        return sca[1] / BlockArea
    else:
        return 0

def Count_Divf(ContShp,blockId,Id):
    nc = ContShp.getElmNum("fclass", blockId, Id)
    num=0
    #print nc
    for item in nc[0].values():
        if nc[1]!=0:
            pi=float(item)/nc[1]
        else:
            continue
        if pi==0 :
            continue
        #print pi
        #print pi,math.log(pi)
        num+=pi*math.log(pi)
    return -1*num

def Count_Lenr(ContShp,blockId,Id):
    sc = ContShp.getSumCouAvebyId("Shape_Length", blockId, Id)
    return sc[0]

def Count_Denr(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAvebyId("Shape_Length", blockId, Id)
    if (BlockArea!= 0):
        return sca[1] / BlockArea
    else:
        return 0

def Count_PerAg(ContShp,blockId,Id,BlockArea):
    scp = ContShp.getSumCouAcebyIdType("Shape_Area","fclass",blockId, Id,"park")
    scf = ContShp.getSumCouAcebyIdType("Shape_Area","fclass",blockId, Id,"forest")
    scg = ContShp.getSumCouAcebyIdType("Shape_Area","fclass",blockId, Id,"grass")

    if (BlockArea!= 0):
        return scp[0]+scf[0]+scg[0] / BlockArea
    else:
        return 0

def Count_StdAg(ContShp,blockId,Id):
    scp = ContShp.getElmbyType("Shape_Area","fclass",blockId, Id,"park")
    scf = ContShp.getElmbyType("Shape_Area","fclass",blockId, Id,"forest")
    scg = ContShp.getElmbyType("Shape_Area","fclass",blockId, Id,"grass")
    pi=[]
    for item in scp[0]:
        pi.append(item)
    for item in scf[0]:
        pi.append(item)
    for item in scg[0]:
        pi.append(item)
    if(len(pi)==0):
        return  0
    return math.sqrt(sum([(float(x) - math.fsum(pi) / len(pi)) ** 2 for x in pi]) / len(pi))

def Count_StdLg(ContShp,blockId,Id):
    scp = ContShp.getElmbyType("Shape_Length","fclass",blockId, Id,"park")
    scf = ContShp.getElmbyType("Shape_Length","fclass",blockId, Id,"forest")
    scg = ContShp.getElmbyType("Shape_Length","fclass",blockId, Id,"grass")
    pi=[]
    for item in scp[0]:
        pi.append(item)
    for item in scf[0]:
        pi.append(item)
    for item in scg[0]:
        pi.append(item)
    if(len(pi)==0):
        return  0
    return math.sqrt(sum([(float(x) - math.fsum(pi) / len(pi)) ** 2 for x in pi]) / len(pi))

def Count_PerAw(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAvebyId("Shape_Area", blockId, Id)
    if (BlockArea!= 0):
        return sca[0] / BlockArea
    else:
        return 0

def Count_StdAw(ContShp, blockId, Id):
    std = ContShp.getSquareDecbyId("Shape_Area", blockId, Id)
    return std

def Count_StdLw(ContShp, blockId, Id):
    std = ContShp.getSquareDecbyId("Shape_Length", blockId, Id)
    return std

def Count_PerAo(ContShp,blockId,Id,BlockArea):
    sca = ContShp.getSumCouAcebyIdOpType3("Shape_Area","fclass",blockId, Id,"park","forest","grass")
    if (BlockArea!= 0):
        return sca[0] / BlockArea
    else:
        return 0

def Count_Leno(ContShp,blockId,Id):
    sc = ContShp.getSumCouAcebyIdOpType3("Shape_Area","fclass",blockId, Id,"park","forest","grass")
    return sc[0]