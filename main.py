# coding=utf-8
import arcpy
from arcpy import env
import os
from  tqdm import tqdm
import time
from Helper.ArcFunOnDb import ArcFuncOnDb
import DataModel
import CountBag


if __name__ == '__main__':
    #load db
    dbpath="F:\BigdipperDesktop\work\Bigdipper\cityClassify\DB\CityClassify.gdb"
    Datasets=["Model","Basic"]
    env.workspace=(dbpath)
    #view content
    print "******************************************************************************"
    print arcpy.ListDatasets("*","ALL")
    print "*******************"
    for item in Datasets:
        env.workspace=dbpath+"\\"+item
        ListGEDI = arcpy.ListFeatureClasses()
        print item,ListGEDI
        for i in ListGEDI:
            print i
        print "*******************"
    print "******************************************************************************"


    #Arcmanager=ArcFuncOnDb(dbpath)
    #Arcmanager.CreatDatasets("test") #success

    #SZbuilding=DataModel.ShpData("SZ_building_block",dbpath+"\\"+Datasets[1])
    #print SZbuilding.getCountbyId("fclass","subsect_id",20021,"allotments") #success
    #print SZbuilding.getSumCouAvebyId("Shape_Area","subsect_id",11001) #success
    #print SZbuilding.getSumCouAcebyIdType("Shape_Area","fclass","subsect_id",20021,"allotments") #success
    #SZbuilding.AddField("test","Double") #success

    # SZ_block=DataModel.ShpData("SZ_block",dbpath+"\\"+Datasets[0])
    # SZ_building_block = DataModel.ShpData("SZ_building_block", dbpath + "\\" + Datasets[1])
    # CountBag.CountTest(SZ_block,SZ_building_block,"subsect_id")

    SZ_block=DataModel.ShpData("SZ_block",dbpath+"\\"+Datasets[0])
    idfield="subsect_id"
    Areafield="Shape_Area"

    #regist Index
    SZ_block.AddField("Ave_Ab","double")
    SZ_block.AddField("Per_Ab","double")
    SZ_block.AddField("Max_Ab", "double")
    SZ_block.AddField("Ave_Hb", "double")
    SZ_block.AddField("Std_Hb", "double")
    SZ_block.AddField("Ave_Sb", "double")
    SZ_block.AddField("Std_Sb", "double")
    SZ_block.AddField("Denb", "double")
    SZ_block.AddField("Denf", "double")
    SZ_block.AddField("Divf", "double")
    SZ_block.AddField("Lenr", "double")
    SZ_block.AddField("Denr", "double")
    SZ_block.AddField("Per_Ag", "double")
    SZ_block.AddField("Std_Ag", "double")
    SZ_block.AddField("Std_Lg", "double")
    SZ_block.AddField("Per_Aw", "double")
    SZ_block.AddField("Std_Aw", "double")
    SZ_block.AddField("Std_Lw", "double")
    SZ_block.AddField("Per_Ao", "double")
    SZ_block.AddField("Leno", "double")

    SZ_building_block = DataModel.ShpData("SZ_building_block", dbpath + "\\" + Datasets[1])
    SZ_water_block = DataModel.ShpData("SZ_water_block", dbpath + "\\" + Datasets[1])
    SZ_pois_block = DataModel.ShpData("SZ_pois_block", dbpath + "\\" + Datasets[1])
    SZ_roads_block = DataModel.ShpData("SZ_roads_block", dbpath + "\\" + Datasets[1])
    SZ_landuse_block = DataModel.ShpData("SZ_landuse_block", dbpath + "\\" + Datasets[1])
    SZ_height_block = DataModel.ShpData("SZ_height_block", dbpath + "\\" + Datasets[1])

    rows = arcpy.UpdateCursor(SZ_block.holepath,sort_fields=idfield+" A")
    num=0
    for row in rows:
        num+=1
    rows = arcpy.UpdateCursor(SZ_block.holepath,sort_fields=idfield+" A")
    for row in tqdm(rows,total=num):
        id=row.getValue(idfield)
        BlockArea=row.getValue(Areafield)

        # if(id<19076):
        #     continue

        #count Index
        Ave_Ab=CountBag.Count_AveAb(SZ_height_block,idfield,id)
        Per_Ab=CountBag.Count_PerAb(SZ_height_block,idfield,id,BlockArea)
        Max_Ab=CountBag.Count_MaxAb(SZ_height_block,idfield,id,BlockArea)
        Ave_Hb = CountBag.Count_AveHb(SZ_height_block, idfield, id)
        Std_Hb = CountBag.Count_StdHb(SZ_height_block, idfield, id)
        Ave_Sb=CountBag.Count_AveSb(SZ_height_block, idfield, id)
        Std_Sb=CountBag.Count_StdSb(SZ_height_block, idfield, id)
        Denb = CountBag.Count_Denb(SZ_building_block, idfield, id,BlockArea)
        Denf = CountBag.Count_Denf(SZ_pois_block, idfield, id,BlockArea)
        Divf = CountBag.Count_Divf(SZ_pois_block, idfield, id)
        Lenr = CountBag.Count_Lenr(SZ_roads_block, idfield, id)
        Denr = CountBag.Count_Denr(SZ_roads_block, idfield, id,BlockArea)
        Per_Ag = CountBag.Count_PerAg(SZ_landuse_block, idfield, id,BlockArea)
        Std_Ag = CountBag.Count_StdAg(SZ_landuse_block, idfield, id)
        Std_Lg = CountBag.Count_StdLg(SZ_landuse_block, idfield, id)
        Per_Aw = CountBag.Count_PerAw(SZ_water_block, idfield, id,BlockArea)
        Std_Aw = CountBag.Count_StdAw(SZ_water_block, idfield, id)
        Std_Lw = CountBag.Count_StdLw(SZ_water_block, idfield, id)
        Per_Ao = CountBag.Count_PerAo(SZ_landuse_block, idfield, id,BlockArea)
        Leno = CountBag.Count_Leno(SZ_landuse_block, idfield, id)
        #see see Index
        print id,"Ave_Ab",Ave_Ab,"Per_Ab", Per_Ab,"Max_Ab", Max_Ab,"Ave_Hb", Ave_Hb,"Std_Hb",\
            Std_Hb,"Ave_Sb", Ave_Sb,"Std_Sb", Std_Sb,"Denb", Denb,"Denf", Denf,"Divf", Divf,"Lenr",Lenr,"Denr", Denr, \
            "Per_Ag", Per_Ag,"Std_Ag", Std_Ag,"Std_Lg", Std_Lg,"Per_Aw", Per_Aw,"Std_Aw", Std_Aw, \
            "Std_Lw", Std_Lw,"Per_Ao", Per_Ao,"Leno", Leno

        #writein Index
        row.setValue("Ave_Ab",Ave_Ab)
        row.setValue("Per_Ab", Per_Ab)
        row.setValue("Max_Ab", Max_Ab)
        row.setValue("Ave_Hb", Ave_Hb)
        row.setValue("Std_Hb", Std_Hb)
        row.setValue("Ave_Sb", Ave_Sb)
        row.setValue("Std_Sb", Std_Sb)
        row.setValue("Denb", Denb)
        row.setValue("Denf", Denf)
        row.setValue("Divf", Divf)
        row.setValue("Lenr", Lenr)
        row.setValue("Denr", Denr)
        row.setValue("Per_Ag", Per_Ag)
        row.setValue("Std_Ag", Std_Ag)
        row.setValue("Std_Lg", Std_Lg)
        row.setValue("Per_Aw", Per_Aw)
        row.setValue("Std_Aw", Std_Aw)
        row.setValue("STd_Lw", Std_Lw)
        row.setValue("Per_Ao", Per_Ao)
        row.setValue("Leno", Leno)
        rows.updateRow(row)
        #time.sleep(0.01)