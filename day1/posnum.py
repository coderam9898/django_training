lst=['1','err','-1',' ',155,2,8,-7,-6]
newlst = []
for i in lst:
    try:
        if int(i) >= 0:
            newlst.append(int(i))
    except ValueError:
        pass
print(newlst)