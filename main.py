def requiredarg(a,b):
    print("sum = " , a+b)

def defaultarg(name = "Stud"):
    print("HI" , name)

def keywordarg(rollno,name):
    print("ENTER ROLL NUM AND NAME" , rollno,name)

def variablearg(*sub):
    print("MY FAV SUBS ARE:", *sub)



requiredarg(3415,3454356)
defaultarg("AB")
keywordarg(2,"esadf")
variablearg("ENG","PYTHON")
variablearg("ENG","PYTHON","DT","SISM")