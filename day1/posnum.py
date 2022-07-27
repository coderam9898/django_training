from pyparsing import Each


lst=['1','err','-1',' ',155,2,8,-7,-6]
newlst = []
for i in lst:
    try:
        if int(i) >= 0:
            newlst.append(int(i))
    except ValueError:
        pass
print(newlst)



def f1():
    lst2=['1','err','-1',' ',155,2,8,-7,-6]
    lst3 = []
    [Each for each in lst2 if type(each)==int and each>0]

f1()
