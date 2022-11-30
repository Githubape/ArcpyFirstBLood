import arcpy
import math
from collections import Counter

class ShpData:
    def __init__(self,shpname,dbpath):
        self.shpname=shpname
        self.dbpath=dbpath
        self.holepath=dbpath+"\\"+shpname

    def getUpCursor(self,fields,sortfields):
        return  arcpy.UpdateCursor(dataset=self.dbpath+"\\"+self.shpname,fields=fields,sort_fields=sortfields)

    def getMacbyId(self, Maxfield, Idfield, Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Maxfield + ";" + Idfield,
                                  sort_fields=Idfield + " A")
        max=0
        count=0
        for row in rows:
            if (row.getValue(Idfield) == Id):
                if max<float(row.getValue(Maxfield)):
                    max=float(row.getValue(Maxfield))
                    count +=1
            else:
                if (count != 0):
                    break
        return max

    def getSumCouAvebyId(self,Sumfield,Idfield,Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Sumfield+";"+Idfield,
                                  sort_fields=Idfield+" A")
        sum=0
        count=0
        for row in rows:
            # print("Sum{0}, ById {1}, ".format(
            #     row.getValue(Sumfield),
            #     row.getValue(Idfield)))
            if(row.getValue(Idfield)==Id):
                #print row.getValue(Sumfield)
                sum += float(row.getValue(Sumfield))
                count+=1
            else:
                if(sum != 0):
                    break
        return sum,count

    def getSumCouAcebyIdType(self,Sumfield,Typefield,Idfield,Id,Type):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Sumfield+";"+Idfield+";"+Typefield,
                                  sort_fields=Idfield+" A"+";"+Typefield+" A")
        sum=0
        count=0
        for row in rows:
            # print("Sum{0}, ById {1}, ".format(
            #     row.getValue(Sumfield),
            #     row.getValue(Idfield)))
            if(row.getValue(Idfield)==Id and row.getValue(Typefield)==Type):
                #print row.getValue(Sumfield)
                sum += float(row.getValue(Sumfield))
                count+=1
            else:
                if(sum != 0):
                    break
        return sum,count

    def getCountbyId(self,Coufield,Idfield,Id,Name):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield,
                                  sort_fields=Idfield+" A"+";"+Coufield+" A")
        count=0
        for row in rows:
            # print("Sum{0}, ById {1}, ".format(
            #     row.getValue(Sumfield),
            #     row.getValue(Idfield)))
            if(row.getValue(Idfield)==Id and row.getValue(Coufield)==Name):
                count+=1
            else:
                if(count != 0):
                    break
        return count

    def AddField(self,name,type):
        fields=arcpy.ListFields(self.holepath)
        for field in fields:
             if field.name==name:
                 return
            # print("{0} is a type of {1} with a length of {2}"
            #       .format(field.name, field.type, field.length))
        arcpy.AddField_management(self.holepath,name, type)

    def getSquareDecbyId(self,Coufield,Idfield,Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield,
                                  sort_fields=Idfield+" A")
        count=0
        num=[]
        for row in rows:
            if(row.getValue(Idfield)==Id):
                num.append(float(row.getValue(Coufield)))
                count+=1
            else:
                if(count != 0):
                    break
        if(len(num)==0):
            return 0
        return math.sqrt(sum([(float(x)-math.fsum(num)/len(num) )** 2 for x in num]) / len(num))

    def getElmNum(self,Coufield,Idfield,Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield,
                                  sort_fields=Idfield+" A")
        count=0
        num=[]
        for row in rows:
            if(row.getValue(Idfield)==Id):
                num.append(row.getValue(Coufield))
                count+=1
            else:
                if(count != 0):
                    break
        return Counter(num),count

    def getElm(self,Coufield,Idfield,Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield,
                                  sort_fields=Idfield+" A")
        count=0
        num=[]
        for row in rows:
            if(row.getValue(Idfield)==Id):
                num.append(row.getValue(Coufield))
                count+=1
            else:
                if(count != 0):
                    break
        return num,count

    def getTwoElm(self,Coufield,Coufield2,Idfield,Id):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield+";"+Coufield2,
                                  sort_fields=Idfield+" A")
        count=0
        num=[]
        num2=[]
        for row in rows:
            if(row.getValue(Idfield)==Id):
                num.append(float(row.getValue(Coufield)))
                num2.append(float(row.getValue(Coufield2)))
                count+=1
            else:
                if(count != 0):
                    break
        return num,num2,count

    def getElmbyType(self,Coufield,Typefield,Idfield,Id,Type):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Coufield+";"+Idfield+";"+Typefield,
                                  sort_fields=Idfield+" A"+";"+Typefield+" A")
        count=0
        num=[]
        for row in rows:
            if(row.getValue(Idfield)==Id and row.getValue(Typefield)==Type):
                num.append(row.getValue(Coufield))
                count+=1
            else:
                if(count != 0):
                    break
        return num,count

    def getSumCouAcebyIdOpType3(self,Sumfield,Typefield,Idfield,Id,Type,Type2,Type3):
        rows = arcpy.SearchCursor(self.holepath,
                                  fields=Sumfield+";"+Idfield+";"+Typefield,
                                  sort_fields=Idfield+" A"+";"+Typefield+" A")
        sum=0
        count=0
        for row in rows:
            # print("Sum{0}, ById {1}, ".format(
            #     row.getValue(Sumfield),
            #     row.getValue(Idfield)))
            if(row.getValue(Idfield)==Id and row.getValue(Typefield)!=Type and  row.getValue(Typefield)!=Type2 and row.getValue(Typefield)!=Type3):
                #print row.getValue(Sumfield)
                sum += float(row.getValue(Sumfield))
                count+=1
            else:
                if(sum != 0):
                    break
        return sum,count
