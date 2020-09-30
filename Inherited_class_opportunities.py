
"""Create an inherited class of where you can find jobs according to country or city"""
 



class jobs:
        def __init__(self,DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst):
            self.DataEngineer=DataEngineer
            self.Datascience=Datascience
            self.DatabaseManager=DatabaseManager
            self.SoftDeveloper=SoftDeveloper
            self.Webdeveloper=Webdeveloper
            self.BusinessIntelligence=BusinessIntelligence
            self.BusinessAnalyst=BusinessAnalyst
            

        def printskills(self):
            print(self.DataEngineer, self.Datascience, self.DatabaseManager, self.SoftDeveloper,self.Webdeveloper,self.BusinessIntelligence,
         self.BusinessAnalyst)



skills=jobs("Python","mongodb","DataScraping","DataManipulation","jsonparsing","SQL","FullStackDev")
print(skills.printskills())
print("DataEngineer :",skills.DataEngineer, "Datascience :", skills.Datascience, "DatabaseManager :", skills.DatabaseManager,
"SoftDeveloper :", skills.SoftDeveloper, "Webdeveloper :", skills.Webdeveloper, "BusinessIntelligence :", skills.BusinessIntelligence,
"BusinessAnalyst :", skills.BusinessAnalyst)
#so for each job attribute, skills shows the list of skills but there's one for each still.  

class DataScience(jobs):
    def __init__(self,DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst):
        super().__init__(DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst)
        self.country=["Romania","France","UK","Netherlands","Germany","Belgium","Norway"]
        self.citys=["Boston","Lyon","London","Amsterdam","Hambourg","Ghent","Oslo"]


z=DataScience("R","DataScraping","DataManagement","DataStructures","statistics","Matlab","Algorythms")
print(z.country)
print(z.citys)


class B_Intelligence(jobs):
    def __init__(self,DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst):
        super().__init__(DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst)
        self.country=["Germany","France","UK","Netherlands","Belgium","Norway"]
        self.city=["Berlin","Paris","Dublin","Rotterdam","Luxembourg","Oslo"]
        self.skills=["python","powerbi","DataManagement","qlik","tableau","Matlab","BI"]

x=B_Intelligence("python","powerbi","DataManagement","qlik","tableau","Matlab","BI")
print(x.country)
print(x.city)
print(x.skills)

class BusinessAnalysiz(B_Intelligence):
    def __init__(self,DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst):
        super().__init__(DataEngineer,Datascience,DatabaseManager,SoftDeveloper,Webdeveloper,BusinessIntelligence,BusinessAnalyst)
        self.countrys=["Romania","Serbia","Hungary","Croatia","Germany","UK"]
        self.places=["Cluj","Timisoara","Budopesti","Dubrovnik","Belgrad","Berlin","London"]


m=BusinessAnalysiz("BusinessModelling","DataBasedDecisions","DataAnalysis","SQL","PowerBI","Tableau","Management_Leadership")
print(m.printskills)
print(m.places)
##--------------------------------------------------------------------






  

   
  








    
        
    




