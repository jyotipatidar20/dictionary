a={'r':2,'e':3,'s':4,'a':5,'b':{'p':6,'i':8},'l':10,'c':{'q':11},'w':13}
sum=0
for i in a:
    if type(a[i]) == dict:
        for j in a[i]:
            sum=sum+(a[i][j])
    else:
        sum=sum+a[i]
print(sum)